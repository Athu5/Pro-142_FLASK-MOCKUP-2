import csv

all_articles = []
# two main lists...!!!
liked_articles = []
not_liked_articles = []

with open('shared_articles.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
