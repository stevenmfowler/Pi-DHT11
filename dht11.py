#!/usr/bin/python
import sys, datetime, json
import Adafruit_DHT

from util import *

sbs = createSBS()
iD = getId()

while True:

	# get timestamp
	dt = str(datetime.datetime.now())

	# get sensor 11 data on pin 4
	h, t = Adafruit_DHT.read_retry(11, 4)

	# convert C to F
	f = t * 9. / 5. + 32 # from C to F

	# create json message
	d = {
	'DeviceID': iD,
	'Temperature': f,
	'Humidity': h,
	'Time': dt
	}
	msg = json.dumps(d)

	print(msg)

	#sbs.send_event('your queue name here',msg)
