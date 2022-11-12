import json, tweepy
from auth import credentials

#authenticating to twitter
client = tweepy.Client(credentials['bearer_token'],credentials['api_key'], credentials['api_secret'], credentials['access_token'], credentials['access_token_secret'])
auth = tweepy.OAuth1UserHandler(credentials['api_key'], credentials['api_secret'], credentials['access_token'], credentials['access_token_secret'])
api = tweepy.API(auth)

#opening news!
b = True
while b:
    with open("news.json", "r") as f:
        a = json.load(f)
        titlu = a[0]['titlu']
        sursa = a[0]['sursa']
        link = a[0]['link']
    b = False
#print(titlu, sursa, link)

#creating tweet
tweet = f"#crypto #bitcoin #altcoin #NFTs #btc #eth #xrp\n" \
        f"{titlu}" \
        f"Source : {sursa}" \
        f"Link : {link}" \
        f"For latest crypto news press Follow!"

#checking if tweet is the right length
if len(tweet) > 10 and len(tweet) < 280:
    try:
        #posting tweet
        client.create_tweet(text = tweet)

    except Exception as e:
        #catching "double post in 15 minutes" error
        print(e)
        pass