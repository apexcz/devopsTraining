from flask import Flask, request
# import argparse

app = Flask(__name__)

#my_parser = argparse.ArgumentParser()
#my_parser.add_argument('--filmName', action='store', type=str, required=True)
#my_parser.add_argument('--stars', action='store', type=int, required=True)

#args = my_parser.parse_args()
#film_name = args.filmName
#stars = args.stars

@app.route("/films",methods=["GET"])
def displays_reviews():
    with open('reviews.txt', 'r') as file_reader:
        return {'response' : file_reader.read().splitlines()}


@app.route("/films",methods=["POST"])
def submit_review():
    print(request.json)
    title = request.json.get('filmname', '')
    ratings = request.json.get('stars', 0)
    file = open('reviews.txt', mode='a')
    file.write('{0}, {1}\n'.format(title, ratings))
    file.close()
    return {'status': 'Works'}


if __name__ == "__main__":
    app.run(debug=True)