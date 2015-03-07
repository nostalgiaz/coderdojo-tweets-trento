from bottle import route, run, static_file
import tweepy

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')
api = tweepy.API(auth)

@route('/')
def index():
    return static_file('index.html', root='.')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

@route('/api/search/<search>')
def search(search):
    tweets = api.search(q=search, count=20)
    return {'data': [
        {'text': tweet.text, 'id': tweet.id_str} for tweet in tweets
    ]}


run(host='localhost', port=8123, debug=True)

