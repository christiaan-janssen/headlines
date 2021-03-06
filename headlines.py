import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
def get_news():
    query = request.args.get("publications")
    if not query or query.to_lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.to_lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

# Bogus route to fix favicon error
@app.route("/favicon.ico")
def favicon():
    return ""

if __name__ == '__main__':
    app.run(debug=True)
