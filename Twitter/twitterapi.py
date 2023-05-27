import tweepy



accessToken = "1239147541708472323-9vmQGLYyAzXe1WP9aC0ppaHc4M2LxK"
accessTokenSecret = "yE9xvmZTshlBAArhAtaumGR5XKGL7Y66zEVgSTASNlOqQ"
consumerKey = "tANH2j19JJTWjHeXKOdYErAIx"
consumerSecret = "XL8bvrEXIZnBagDqS654keYSHGy05VyOt2F409mgyIaa3fonTl"
auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth,wait_on_rate_limit=True)
search_key = "Minyak Goreng Mahal"
for tweet in tweepy.Cursor(api.search_tweets,q=search_key,count=5,lang="id").items():
    print(tweet.text)