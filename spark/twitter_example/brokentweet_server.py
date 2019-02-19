import json
import os
import requests
import requests_oauthlib
import socket
import sys


def get_tweets(auth_object):
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    query_data = [('language', 'en'),
                  ('track', 'trump'),
                  ('tweet_mode','extended')]
    query_url = url + '?' + \
        '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
    response = requests.get(query_url, auth=auth_object, stream=True)
    print(f"Query: {query_url}")
    print(f"Response: {response}")
    return response


def send_tweets_to_spark(http_resp, tcp_connection):
    for line in http_resp.iter_lines():
        try:
            full_tweet = json.loads(line)
            timestamp = full_tweet['created_at'].encode('utf-8')
            #ensure full text of tweet is collected:
            if full_tweet['truncated']:
                #print('truncated')
                tweet_text = full_tweet['extended_tweet']['full_text'].encode('utf-8')
            else:
                #print('not truncated')
                tweet_text = full_tweet['text'].encode('utf-8')
            print(f"Created at: {timestamp}")
            print(f"Tweet Text: {tweet_text}")
            print("------------------------------------------")
            tweet_info = json.dumps({
                            'timestamp':str(timestamp),
                            'text':str(tweet_text),
                            }).encode('utf-8')
            print(type(tweet_info))
            print(len(tweet_info))
            #print("to send:",tweet_info)
            tcp_connection.send(tweet_info)
        except Exception as e:
            e = sys.exc_info()[1]
            print(f"Errored without sending: {e}")


if __name__ == "__main__":
    my_auth = requests_oauthlib.OAuth1(os.environ["CONSUMER_KEY"],
                                       os.environ["CONSUMER_SECRET"],
                                       os.environ["ACCESS_TOKEN"],
                                       os.environ["ACCESS_SECRET"])

    TCP_IP = socket.gethostbyname(socket.gethostname())
    TCP_PORT = 9009

    print(f"Host: {TCP_IP} :: Port {TCP_PORT}")
    conn = None
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print(f"Waiting for TCP connection...")
    conn, addr = s.accept()
    print(f"Connected... Starting getting tweets.")
    resp = get_tweets(my_auth)
    send_tweets_to_spark(resp, conn)
