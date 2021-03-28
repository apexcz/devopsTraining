import argparse
from flask import Flask

app = Flask(__name__)

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--filmName', action='store', type=str, required=True)
my_parser.add_argument('--stars', action='store', type=int, required=True)

args = my_parser.parse_args()
film_name = args.filmName
stars = args.stars

@app.route("/",methods=["POST"])
def submit_review():
    film = request.form.get('film-name', '')

file = open('reviews.txt', mode='a')
file.write('{0}, {1}\n'.format(film_name, stars))
file.close()


with open('reviews.txt', 'r') as file_reader:
    all_reviews = file_reader.read()


print(all_reviews)