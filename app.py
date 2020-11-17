from flask import Flask
from flask import render_template
from news import get_articles
app = Flask(__name__)

@app.route('/')
def hello_world():
    articles = get_articles()
    return render_template("index.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)