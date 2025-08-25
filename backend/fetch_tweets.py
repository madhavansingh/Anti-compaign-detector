import snscrape.modules.twitter as sntwitter
import pandas as pd
import sys

query = "India OR #India OR #Kashmir"
max_tweets = 100

tweets_list = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i > max_tweets:
        break
    tweets_list.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets_list, columns=["date", "username", "content"])
df.to_csv("data/tweets.csv", index=False)
print("Tweets saved to data/tweets.csv")
