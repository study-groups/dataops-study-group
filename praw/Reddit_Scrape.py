import praw
import os
#from dotenv import load_dotenv

#load_dotenv()
reddit = praw.Reddit(client_id=os.environ.get('client_id'),
                     client_secret=os.environ.get('client_secret'),
                     username=os.environ.get('username'),
                     password=os.environ.get('password'),
                     user_agent=os.environ.get('user_agent'))

subreddits = ['aws', 'bigdatajobs', 'computervision', 'datacleaning',
              'dataisbeautiful', 'datasciencejobs', 'datasciencenews',
              'deeplearning', 'deeplearningpapers', 'django',
              'djangolearning', 'flask', 'git', 'inventwithpython',
              'learnmachinelearning', 'learnmath', 'learnpython',
              'linux4noobs', 'linuxmasterrace', 'linuxquestions',
              'mlclass', 'mlpapers', 'mlquestions', 'neuralnetworks',
              'pystats', 'python', 'pythoncoding', 'pythontips', 'pytorch',
              'spacynlp', 'scikitlearn', 'tensorflow', 'textdatamining', 'vim']

for category in subreddits:
    sub = reddit.subreddit(category)
    hot_python = sub.hot(limit=20)
    with open('comments_12-18.csv', 'a') as file:
        for submission in hot_python:
            if not submission.stickied:
                file.write(str(submission.id) + '\t')
                file.write(str(submission.subreddit_name_prefixed) + '\t')
                file.write(str(submission.author) + '\t')
                file.write(str(submission.title) + '\t')
                file.write(str(submission.created_utc) + '\t')
                file.write(str(submission.num_comments) + '\t')
                file.write(str(submission.ups) + '\t')
                file.write(str(submission.downs) + '\n')

