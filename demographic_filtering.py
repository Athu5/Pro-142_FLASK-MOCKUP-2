import pandas as pd
import numpy as np

df1 = pd.read_csv('shared_articles.csv')
df2 = pd.read_csv('users_interactions.csv')

df1_function = df1[df1["eventType"] == "CONTENT SHARED"]


def find_total_events(df1_row):
    total_likes = df2[(df2["contentId"] == df1_row["contentId"])
                      & (df2["eventType"] == "LIKE")].shape[0]
    total_views = df2[(df2["contentId"] == df1_row["contentId"])
                      & (df2["eventType"] == "VIEW")].shape[0]
    total_bookmarks = df2[(df2["contentId"] == df1_row["contentId"]) & (
        df2["eventType"] == "BOOKMARK")].shape[0]
    total_follows = df2[(df2["contentId"] == df1_row["contentId"]) & (
        df2["eventType"] == "FOLLOW")].shape[0]
    total_comments = df2[(df2["contentId"] == df1_row["contentId"]) & (
        df2["eventType"] == "COMMENT CREATED")].shape[0]
    return total_likes + total_views + total_bookmarks + total_follows + total_comments


df1_function["total_events"] = df1_function.apply(find_total_events, axis=1)

df1_function = df1_function.sort_values(['total_events'], ascending=[False])

output = df1_function[df1_function['lang'] == "en"]
print(output.head(10))
# done
