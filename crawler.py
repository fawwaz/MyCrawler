from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


access_token = "470084145-mYUzguiOMVfPBYjEtvdgNZ8kYpHHX40UTG3nMmXE"
access_token_secret = "Xn1aywLNyHgN5WmKV17rs1844zxS2xWZqvPEFJnLbYhGj"
consumer_key = "AF0EH8cPj4RyolkNTLOzsc2Lj"
consumer_secret = "BlfXl9LjnPgsL0i0wt7ky3IRxdP8927nXHrP3D2h9FAGiqOjZ7"

class StdOutListener(StreamListener):
	i=0
	def on_data(self, data):
		decoded = json.loads(data)
		if('event' in decoded['text'].split()):
			print '[%d] @%s: %s' % (self.i,decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
		else:
			print '[%d]' % (self.i)
		# Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
		print ''
		self.i=self.i+1
		return True
		
	def on_error(self, status):
		print status

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	stream = Stream(auth, l)
	
	#stream.filter(track=['event'],locations=[6.00000000,11.00000000,95.00000000,141.00000000])
	stream.filter(locations=[95.01,-11.01,141.02,6.08])