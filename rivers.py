streams = []
initialAmount = int(input())
for i in range(0, initialAmount):
    streams.append(int(input()))

while True:
    actionInput = input()
    if actionInput == "99":
        streamSplit = int(input()) - 1
        splitPercent = int(input())
        streamFlow = streams[streamSplit]
        del streams[streamSplit]
        streams.insert(streamSplit, round(streamFlow * (splitPercent/100)))
        streams.insert(streamSplit + 1, round(streamFlow * ((100 - splitPercent)/100)))

    elif actionInput == "88":
        streamMerged = int(input()) - 1
        streamFlow = streams[streamMerged]
        streams[streamMerged] = streamFlow + streams[streamMerged + 1]
        del streams[streamMerged + 1]
    else:
        break
        
print(streams)