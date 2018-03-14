import time
import sys
import os
import glob

import MySQLdb

import praw
import urllib


# Open database connection
db = MySQLdb.connect("localhost","root","tupac21","myDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
sql = "INSERT INTO urls(url) VALUES (%s)" % "url"
#sql = "SELECT * FROM urls"
cursor.execute(sql);

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
for d in data:
    print d
#print "Database version : %s " % data

# disconnect from server
db.close()

'''
from instabot import Bot

reddit = praw.Reddit('instabot')
subreddit = reddit.subreddit("memes")

bot = Bot()
bot.login()

global post_to_upload
for submission in subreddit.hot(limit=20):
    
    try:
        if not submission.over_18 and submission.score > post_to_upload.score: 
            post_to_upload = submission
        print "upload test"
    except NameError:
        print "NAME ERROR"
        post_to_upload = submission
    print("Title: ", submission.title)
    print("Score: ", submission.score)
    print("URL: ", submission.url)
    print("NSFW: ", submission.over_18)
    print("---------------------------------\n")
print("FINAL: ", post_to_upload.title)
timeout = 20#24 * 60 * 60  # pics will be posted every 24 hours 
img = urllib.urlretrieve(post_to_upload.url, "img.jpg")
print img

while True:
    pics = glob.glob("./img.jpg")
    print "len " ,len(pics)
    try:
        if img != None:
            bot.uploadPhoto(pics[0], caption="test")
    except Exception as e:
        print(str(e))
    time.sleep(timeout)
'''