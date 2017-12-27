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
    allLocationRecords = json.load(f)
    print(len(allLocationRecords))

for i in range(len(allLocationRecords)):
	# skip the first
	if i == 0:
		continue
	else:
		print(i)
		# get the city 
		city = allLocationRecords[i]['FIELD13']

		# get the state
		state = allLocationRecords[i]['FIELD14']

		# get the sap
		sap = allLocationRecords[i]['FIELD4']

		# if sap is only 3 digits prepend 0
		if (len(allLocationRecords[i]['FIELD4']) < 4):
			sap = '0' + sap
			#print("record", i+1)
			print("PREPENDINGGGGGGGGGGGGGGGGGGGGGGGGGGG")
			print(sap)

		print(sap)