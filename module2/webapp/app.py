from flask import Flask, request, render_template, redirect, url_for
import requests


API_KEY = 'YOUR TRANSPORT API API_KEY HERE'
APP_ID = 'YOUR TRANSPORT API APP_ID HERE'

app = Flask(__name__)

@app.route("/hello",methods=["GET"])
def hello():
    return "hello from us"

@app.route("/",methods=["GET"])
def home():
    post_code = request.args.get('postcode', 'NW5 1TL')
    postcode_result = requests.get(f'http://api.postcodes.io/postcodes/{post_code}').json()
    latitude = postcode_result['result']['latitude']
    longitude = postcode_result['result']['longitude']
    transport_params = {'lat': latitude, 'lon': longitude, 'type': 'bus_stop', 'api_key': API_KEY, 'app_id': APP_ID}
    transport_result = requests.get('http://transportapi.com/v3/uk/places.json', params=transport_params)
    first_two_busstops = transport_result.json()['member'][0:2]
    busstops = []

    for busstop in first_two_busstops:
        bsustop_time_url = f'http://transportapi.com/v3/uk/bus/stop/{busstop["atcocode"]}/live.json?api_key={API_KEY}&app_id={APP_ID}'
        busstop_times_result = requests.get(bsustop_time_url).json()

        buses = []
        bus_departures = busstop_times_result['departures']
        for departure in bus_departures.keys():
            busstop_times = {
                'busstop_name': busstop['name'],
                'bus_name': departure,
                'aimed_departure_time': bus_departures[departure][0]['aimed_departure_time']
            }
            busstops.append(busstop_times)
    
    return {'result': busstops}

if __name__ == "__main__":
    app.run(debug=True)