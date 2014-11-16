from flask import Flask
app = Flask(__name__)
from operator import itemgetter

import json,httplib


def pullData():
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('GET', '/1/classes/Post', '', {
	       "X-Parse-Application-Id": "mfqIsrGX0ZACy5kZhI4xBJjgPAQKXJnZiioRACBR",
	       "X-Parse-REST-API-Key": "SHwLikHNsVpvVnSzmqep4AAUbbEIQ4ja0LL2QUwf"
	     })
	result = json.loads(connection.getresponse().read())
	# print result.values()[0]

	newlist = sorted(result.values()[0], key=itemgetter('createdAt')) #put everythign in order so the most recent is at the bottom
	# print newlist
	#  right now its a list of 2 dictionaries, need to sort by createdAt
	newlist.reverse()
	return newlist[0].values()[0]


@app.route('/')
def hello_world():
    return pullData()

if __name__ == '__main__':
    app.run()