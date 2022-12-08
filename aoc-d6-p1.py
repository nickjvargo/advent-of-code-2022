#! python

dataStreamTransmission = open("./inputs/aoc-d6.txt")
dataStream = dataStreamTransmission.read()
startOfPacketEnd = -1

for i in range(len(dataStream)):
    first = dataStream[i]
    second = dataStream[i+1]
    third = dataStream[i+2]
    fourth = dataStream[i+3]
    if first != second and first != third and first != fourth:
        if second != third and second != fourth:
            if third != fourth:
                startOfPacketMarkerEnd = i+4
                break 

print(startOfPacketMarkerEnd)
dataStreamTransmission.close()