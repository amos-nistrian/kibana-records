# Get records
import json
import time

date = "10-16"
arrayOfAllPhoneEventsForTheDay = []

with open( date + 'PhoneEventsWithoutLocation.txt', 'r') as f:
    recordOfTheDay = json.load(f)

for i in range(len(recordOfTheDay)):
    # make a phone event array
    phoneEvent = ['f']

    sourceDict = recordOfTheDay[i]["_source"]

    # getting device type
    if 'device_type' in sourceDict:
        phoneEvent.append(sourceDict["device_type"]) #iphone or android
    else:
        phoneEvent.append("Android")

    # getting make
    if 'make' in sourceDict:
        phoneEvent.append(sourceDict["make"]) # samsung, lg, htc, apple
    else:
        phoneEvent.append("unknown")

    # getting recieved time, split it up
    incorrectTime = sourceDict["received_at"]

    # date, dont include the T
    date = incorrectTime[0:10] + ','

    # dont include the z
    time = incorrectTime[11:len(incorrectTime)-1]

    date = date + time

    phoneEvent.append(date)

    #phoneEvent.append(time)

    # getting imei
    if 'imei' in sourceDict:
        phoneEvent.append("yes")
    else:
        phoneEvent.append("no")

    # getting sap
    message = recordOfTheDay[i]["_source"]["message"]
    #message = sourceDict["message"]

    if "sap=" not in message:
        phoneEvent.append('nil')
    else:
        startIndex = (message.index("sap="))
        startIndex += 3

        sapVal = ""
        for j in range (4):
            sapVal += message[j+1+startIndex]

        phoneEvent.append(sapVal.upper())
        #print("the sapval at", i+1, "is", sapVal)

	# getting coupler_id
    if 'coupler_id' not in sourceDict:
        phoneEvent.append('nil')
    else:
        phoneEvent.append(sourceDict["coupler_id"])

    # add the phoneEvent to arrayOfAllPhoneEventsForTheDay
    arrayOfAllPhoneEventsForTheDay.append(phoneEvent)

# append city and state
with open('locations.txt', 'r') as f:
    allLocationRecords = json.load(f)
    #print(len(allLocationRecords))

# go through locations file
for i in range(len(allLocationRecords)):
    # skip the first
    if i == 0:
        continue
    else:
        # get the city
        city = allLocationRecords[i]['FIELD13']

        # get the state
        state = allLocationRecords[i]['FIELD14']

        # get the sap
        sap = allLocationRecords[i]['FIELD4']

        # if sap is only 3 digits prepend 0
        if (len(allLocationRecords[i]['FIELD4']) < 4 and len(allLocationRecords[i]['FIELD4']) > 2 ):
            sap = '0' + sap

        # find the matching saps in arrayOfAllPhoneEventsForTheDay and
        if sap != '0' and sap != '':
            # append city and state to all of them if city and state are empty
            for i in range(len(arrayOfAllPhoneEventsForTheDay)):
                if arrayOfAllPhoneEventsForTheDay[i][5] == sap and arrayOfAllPhoneEventsForTheDay[i][0] == 'f':
                    arrayOfAllPhoneEventsForTheDay[i].append(city)
                    arrayOfAllPhoneEventsForTheDay[i].append(state)
                    arrayOfAllPhoneEventsForTheDay[i][0] = 't'

# export arrayOfAllPhoneEventsForTheDay as csv

# create file to write to
file = open("10-16PhoneEventsAddedLocation.txt","w+")

for i in range(len(arrayOfAllPhoneEventsForTheDay)):
    print(i+1)
    for j in range(len(arrayOfAllPhoneEventsForTheDay[i])):
        #print (len(arrayOfAllPhoneEventsForTheDay[i]))
        # get that value and append comma and newline at end
        if j == 0:
            continue
        else:
            if j+1 == len(arrayOfAllPhoneEventsForTheDay[i]):
                print("appending", arrayOfAllPhoneEventsForTheDay[i][j] + '\n')
                file.write(arrayOfAllPhoneEventsForTheDay[i][j] + "\n")
            else:
                print("appending", arrayOfAllPhoneEventsForTheDay[i][j] + ';')
                file.write(arrayOfAllPhoneEventsForTheDay[i][j] + ';')
