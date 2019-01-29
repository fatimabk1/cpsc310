from flask import Flask
import tweepy

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

consumer_key = 'zQ2pSFqGXx49LqwPO4kyOYXMa'
consumer_secret = 'PmeCf772l8mmAQ6qgXJT7Pe4fBQC8BVSEOyqz1uUr7WWB7DZUa'
access_token = '1088528600729571329-d5TG9WKYIIoy0OgoyB7wqQKq3prf4H'
access_token_secret = 'GjZAetIOqJaXUjcM07STLIL2fxMQgOMuqUJSy0j4ac05D'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if __name__ == '__main__':
    app.run()
