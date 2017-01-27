from azure.servicebus import ServiceBusService
from azure.servicebus import Message

def createSBS():
	service_namespace = 'your namespace here'
	key_name = 'your event hub here' # SharedAccessKeyName
	key_value = 'mKG+x1xmMHso/ZdL/nZkJHhg6rt3MeiMqVXz+HQQjHp98=' # SharedAccessKey

	sbs = ServiceBusService(service_namespace,
		shared_access_key_name=key_name,
		shared_access_key_value=key_value)
	return sbs

def getId():
	iD = "0000000000000000"
	try:
		f = open('/proc/cpuinfo','r')
		for line in f:
			if line[0:6]=='Serial':
				iD = line[10:26]
		f.close()
	except:
		iD = "ERROR00000000000"
		f.close()
	return iD
