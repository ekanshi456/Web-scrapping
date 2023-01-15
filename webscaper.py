import pandas as pd
import praw

reddit = praw.Reddit(client_id="VVIT6S7PhWAETg8gYFJl2w",         # my client id
                               client_secret="pTj8s5aK1Z3wVqjDzFV_hHvTidSKgg",      # my client secret
                               user_agent="Ekanshi_Katiyar")
alls = reddit.subreddit("all")

titles=[]
scores=[]
ids=[]
comments=[]


for submission in alls.search("tata consultancy services"):
    titles.append(submission.title)
    scores.append(submission.score)
    ids.append(submission.id)
    comments.append(submission.num_comments)
df = pd.DataFrame()

df['Title'] = titles
df['Id'] = ids
df['Upvotes'] = scores
df['comments'] = comments

katiyar = df

print(katiyar)
katiyar.to_csv("katiyar.csv", index=True)