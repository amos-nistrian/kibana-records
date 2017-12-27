# Get records
import json

with open('dec13.txt', 'r') as f:
    recordOfTheDay = json.load(f)

arrayOfAllPhoneEventsForTheDay = []

for i in range(len(recordOfTheDay)):	
	# make a phone event array
	phoneEvent = []

	sourceDict = recordOfTheDay[i]["_source"]

	# getting device type
	if 'device_type' in sourceDict:
  		phoneEvent.append(sourceDict["device_type"])
	else:
  		phoneEvent.append("Android")
	
	# getting make
	if 'make' in sourceDict:
		phoneEvent.append(sourceDict["make"])
	else:
		phoneEvent.append("unknown")

	# getting recieved time
	phoneEvent.append(sourceDict["received_at"])

	# getting imei
	if 'imei' in sourceDict:
  		phoneEvent.append("yes")
	else:
		phoneEvent.append("no")

	# getting sap
	message = recordOfTheDay[i]["_source"]["message"]
  	#message = sourceDict["message"]

	if "sap=" not in message:  
  		phoneEvent.append(0)
	else:
		startIndex = (message.index("sap="))
		startIndex += 3
		#print(message[startIndex])
		sapVal = "" 
		for i in range (4):
			sapVal += message[i+1+startIndex]
			phoneEvent.append(sapVal)
		
	# getting coupler_id
	if 'coupler_id' not in sourceDict:	
		phoneEvent.append(0)
	else:
		phoneEvent.append(sourceDict["coupler_id"])

	# get city and state
	# export as csv
with open('locations.txt', 'r') as f:
    locationRecords = json.load(f)
    print(len(locationRecords))



