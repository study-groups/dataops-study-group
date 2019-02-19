# Project Overview:
This is a simple spark streaming example with twitter. It is **currently incomplete.**

It provides a simple server, taken from the Thinkful curriculum, and streams tweets to spark. A small inclusion to the stream, the create date in addition to tweet text, causes a complete data leakage. 

# How to set up and replicate

Start a docker network 
`docker network create --driver bridge thinkful-net`

Start a shell for your server. I based it on the docker image provided by the curriculum, `thinkfulstudent/simple_server`

In this shell, open `workingtweet_server.py` and run after saving your twitter app credentials as environment variables. It will begin "waiting" for a receiver.

Next, start a shell for spark. I based it on the docker image `jupyter/pyspark-notebook`. create a directory called `cps`, which is what spark will use for checkpoints. Then, run `stream.py`. You should see tweets streaming from the server, and appearing in 2-second clumps in RDDs within spark. 

## Error: Adding dates
After killing those processes, run `brokentweet_server.py` in the server shell and then rerun `stream.py` in the other shell just as before. You will continue seeing the tweets stream, but this time with the create date as well. Although the server is still sending `type: bytes`, the spark shell never receives anything. 
