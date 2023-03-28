from flask import Flask, jsonify, request
from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import output
from content_based_filtering import get_recommendations
import csv

app = Flask(__name__)


@app.route("/get-articles")
def get_article():
    articles_data = {
        "title": all_articles[0][10],
        "url": all_articles[0][9],
        "lang": all_articles[0][12],
        "contentId": all_articles[0][2],
        "text": all_articles[0][11]
    }
    return jsonify({
        "data": articles_data,
        "status": "success"
    })


@app.route("/liked-articles", methods=["POST"])
def liked_article():
    with open('shared_articles.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        data = list(reader)
        all_articles = data[1:]

    articles = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201


@app.route("/not-liked-articles", methods=["POST"])
def unliked_articles():
    with open('shared_articles.csv', encoding="utf8") as f:
        reader = csv.reader(f)
        data = list(reader)
        all_articles = data[1:]

    articles = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201


@app.route("/popular-articles")
def popular_movies():
    articles_data = []
    for articles in output:
        _d = {
            "url": articles[9],
            "title": articles[10],
            "text": articles[11],
            "lang": articles[12],
            "total_events": articles[13]
        }
        articles_data.append(_d)
    return jsonify({
        "data": articles_data,
        "status": "success"
    }), 200


@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[11])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,
                           _ in itertools.groupby(all_recommended))
    articles_data = []
    for recommended in all_recommended:
        _d = {
            "url": recommended[0],
            "title": recommended[1],
            "text": recommended[2],
            "lang": recommended[3],
            "total_events": recommended[4]
        }
        articles_data.append(_d)
    return jsonify({
        "data": articles_data,
        "status": "success"
    }), 200


if __name__ == "__main__":
    app.run()
# done
