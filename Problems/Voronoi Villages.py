amountOfIterations = int(input())
VillageList = []
for i in range(amountOfIterations):
    VillageList.append(int(input()))

VillageList.sort

Neighborhoods = []
for i in range(1, amountOfIterations - 1):
    currentPosition = VillageList[i]
    leftVillage = VillageList[i - 1]
    rightVillage = VillageList[i + 1]

    leftNeighborhoodLimit = (leftVillage + currentPosition)/2
    rightNeighborhoodLimit = (rightVillage + currentPosition)/2

    NeighborhoodSize = rightNeighborhoodLimit - leftNeighborhoodLimit
    Neighborhoods.append(NeighborhoodSize)
    
print(min(Neighborhoods))
