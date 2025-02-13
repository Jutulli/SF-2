ianInfo = input().split()
eventDays = input().split()

totalShirts = int(ianInfo[0])
dayAmount = int(ianInfo[2])

currentShirts = totalShirts
laundryAmount = 0

for currentDay in range(1,dayAmount+1):

    if currentShirts == 0:
        laundryAmount += 1
        currentShirts = totalShirts 

    for currentEvent in eventDays:
        if currentDay == int(currentEvent):
            totalShirts += 1
            currentShirts += 1

    currentShirts -= 1

print(laundryAmount)