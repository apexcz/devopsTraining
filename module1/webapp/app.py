from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/films/table",methods=["GET"])
def show_reviews():
    stars = request.args.get('stars', None)
    return render_template("index.html",reviews=get_reviews(stars))

@app.route("/films/submit",methods=["GET", "POST"])
def submit_review():
    if request.method == "POST":
        title = request.form['title']
        ratings = request.form['stars']
        add_review(title, ratings)
        return redirect(url_for('show_reviews'))
    return render_template("submit.html")

@app.route("/films",methods=["GET", "POST"])
def api_channel():
    if request.method == "POST":
        print(request.json)
        title = request.json.get('filmname', '')
        ratings = request.json.get('stars', 0)
        add_review(title, ratings)
        return {'status': 'Works'}
    else:
        stars = request.args.get('stars', None)
        return {'response' : get_reviews(stars)}

def get_reviews(stars=None):
    reviews = []
    with open('reviews.txt', 'r') as file_reader:
        reviews = file_reader.read().splitlines()
    
    if stars == None:
        return reviews
    else:
        return [review for review in reviews if  float(review.split(',')[1]) == float(stars)]

def add_review(title, ratings):
    file = open('reviews.txt', mode='a')
    file.write('{0},{1}\n'.format(title, ratings))
    file.close()

if __name__ == "__main__":
    app.run(debug=True)