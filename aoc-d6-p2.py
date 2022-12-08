#! python

dataStreamTransmission = open("./inputs/aoc-d6.txt")
dataStream = dataStreamTransmission.read()
uniqueDataArray = []
lengthOfMessage = 14
startOfMessage_End = 0

def recursion(i):
    global startOfMessage_End
    if uniqueDataArray.count(dataStream[i]) > 0:
        uniqueDataArray.clear()
    else:
        uniqueDataArray.append(dataStream[i])
        if len(uniqueDataArray) == lengthOfMessage:
            startOfMessage_End = i+1
        else:
            recursion(i+1)
    return len(uniqueDataArray)

for i in range(len(dataStream)):
    if recursion(i) > 0:
        break
 
print(startOfMessage_End)
dataStreamTransmission.close()