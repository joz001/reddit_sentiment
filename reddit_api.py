import praw
import pandas as pd

s_and_p = list(pd.read_csv("symbols.csv"))[1:-1]
stonk_dict = dict()
[stonk_dict.update({ticker: 0}) for ticker in s_and_p]


reddit = praw.Reddit("bot1", user_agent='script:reddit_sentiment:v1 (by /u/zo_keeper)')

count = 0
for submission in reddit.subreddit("wallstreetbets").new(limit=500):
    count += 1
    # print(submission.title, submission.score)
    for word in submission.title.split(' '):
        if stonk_dict.get(word) is not None:
            stonk_dict[word] += 1
print(count)

for ticker in stonk_dict.keys():
    if stonk_dict[ticker] > 0:
        print(ticker, stonk_dict[ticker])

# for ticker in s_and_p:
#     for submission in reddit.subreddit("wallstreetbets").search(ticker):
#         print(submission.title)
