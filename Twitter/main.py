import snscrape.modules.twitter as sntwitter
import pandas as pd
tweetlist=[]

for i,tweet in enumerate(sntwitter.TwitterHashtagScraper("Minyak Goreng Mahal since:2022-01-01 until:2022-07-01").get_items()):
    if i>1000:
        break
    # print([tweet.date,tweet.id,tweet.user.username,tweet.content])
    tweetlist.append([tweet.date,tweet.id,tweet.user.username,tweet.content])

    labelframe = ["datetime","Tweet id","Username","Text"]
    datatwitter = pd.DataFrame(tweetlist,columns=labelframe)
    print(datatwitter)
    datatwitter.to_csv("datatwittereminyak.csv")

