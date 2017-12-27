# Get records
import json

with open('dec13.txt', 'r') as f:
    recordOfTheDay = json.load(f)

arrayOfAllPhoneEventsForTheDay = []

for i in range(len(recordOfTheDay)):	
	# make a phone event array
	phoneEvent = []
	print(i+1)

	sourceDict = recordOfTheDay[i]["_source"]

	# getting device type
	if 'device_type' in sourceDict:
  		print(sourceDict["device_type"])
  		phoneEvent.append(sourceDict["device_type"])
	else:
  		print ("NO DEVICE_TYPE FOUND, adding Android instead")
  		phoneEvent.append("Android")
	
	# getting make
	if 'make' in sourceDict:
		phoneEvent.append(sourceDict["make"])
	else:
		print("make was unknown")
		phoneEvent.append("unknown")

	








