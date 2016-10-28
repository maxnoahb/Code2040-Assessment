# importing library to encode data for post request
from urllib import urlencode
# importing library to open url and send post request
from urllib2 import Request, urlopen
import requests


# STEP 1

# set destination url and json dictionary
url = 'http://challenge.code2040.org/api/register'
dictionary = {'token': '08f41562c746804013f29d78d0233b2e', 'github': 'https://github.com/maxnoahb/Code2040-Assessment.git'}

# make post request and print json
request = Request(url, urlencode(dictionary).encode())
json = urlopen(request).read().decode()

# STEP 2

# url and json dictionary to get string
url2 = 'http://challenge.code2040.org/api/reverse'
dictionary2 = {'token': '08f41562c746804013f29d78d0233b2e'}

# post request to get string
request2 = Request(url2, urlencode(dictionary2).encode())
t = urlopen(request2).read().decode()

# convert given text to string, reverse it
string_of_text = str(t)
reversed_string = string_of_text[::-1]

# url and json dictionary to send reversed string
url3 = 'http://challenge.code2040.org/api/reverse/validate'
dictionary3 = {'token': '08f41562c746804013f29d78d0233b2e', 'string': reversed_string}

# post request to send reversed string
request3 = Request(url3, urlencode(dictionary3).encode())
json3 = urlopen(request3).read().decode()

# STEP 3

# url and post request to get needle and haystack
url4 = 'http://challenge.code2040.org/api/haystack'
request4 = Request(url4, urlencode(dictionary2).encode())
json4 = urlopen(request4).read().decode()

# importing library to parse json
import json
# parse json, separate haystack and needle
data = json.loads(json4)
haystack = data['haystack']
needle = data['needle']

# locate index of the needle in haystack array
index = haystack.index(needle)

# url and json dictionary to submit result
url5 = 'http://challenge.code2040.org/api/haystack/validate'
dictionary5 = {'token': '08f41562c746804013f29d78d0233b2e', 'needle': index}
request5 = Request(url5, urlencode(dictionary5).encode())
json5 = urlopen(request5).read().decode()

# STEP 4

# url and post request to get prefix and string array
url6 = 'http://challenge.code2040.org/api/prefix'
request6 = Request(url6, urlencode(dictionary2).encode())
json6 = urlopen(request6).read().decode()

# parse json, separate into prefix and array
data = json.loads(json6)
prefix = data['prefix']
array = data['array']

# define an empty array, add strings if they do not begin with the prefix
new_array = []
for elt in array:
	if not elt.startswith(prefix):
		new_array.append(str(elt))

# post request to submit resulting array
# note: here, I begin experimenting with different ways to approach
# post requests in Python. I realized this is a cleaner way to do it,
# but chose to leave the earlier methods to show the thought progression
request7 = requests.post('http://challenge.code2040.org/api/prefix/validate', json = {'token': '08f41562c746804013f29d78d0233b2e', 'array': index})

# STEP 5

# importing libraries to handle date functions
from iso8601 import parse_date
from datetime import timedelta

# post request to get datestamp and interval 
data = requests.post('http://challenge.code2040.org/api/dating', json = dictionary2).json()

# separate the datestamp and interval from json
datestamp = data['datestamp']
interval = data['interval']

# parse the iso8601 datetime format 
date_initial = parse_date(datestamp)

# add the seconds given in interval to given date
date_new = timedelta(seconds=interval) + date_initial

# format datetime back to iso8601 to match original form (eliminate characters off the end and add a Z)
date_formatted = date_new.isoformat()[:-6] + "Z"

# submit result
requests.post('http://challenge.code2040.org/api/dating/validate', json = {'token': '08f41562c746804013f29d78d0233b2e', 'datestamp': date_formatted})





