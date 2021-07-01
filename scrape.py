import ibm_cloud_sdk_core
import snscrape.modules.twitter as sntwitter
import pandas as pd
import numpy as np

from watson import *

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:SenSanders').get_items()):
    if i>100:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above 
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

#tweets_df1.to_html('temp.html')
#just_text = tweets_df1['Text']

emote_arr = np.zeros(5)
for i in range(50, 100):
    
    tweet_emotes = analyze(tweets_df1.loc[i, "Text"])
    
    emote_arr += np.array([tweet_emotes[emote] for emote in tweet_emotes])
    
    #print(emote_arr)
    print("Tweet {} Processed".format(i+1))


emote_arr = emote_arr/50
print(emote_arr)