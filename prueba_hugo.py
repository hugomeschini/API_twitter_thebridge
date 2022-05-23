#This code does not work with the twitter API, this is another way to get data from twitter
#  (although working with the API is the recommended)

#In order to run the following attributes, is necessary to have an updated python version installed

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "TheBridge_Tech until:2022-05-22 since:2022-01-01"
tweets = []
limit = 5000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content, tweet.likeCount, tweet.retweetCount, tweet.replyCount])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Likes', 'Retweets', 'Replies'])
print(df)
df.to_csv('tweets_hm.csv')

