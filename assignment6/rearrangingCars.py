def rearrangingCars(startPositions, endPositions):
    slotNums = len(startPositions)
    car2slot = [0] * slotNums
    wrongCars = set()
    for i in range(slotNums):
        if startPositions[i] and startPositions[i] != endPositions[i]:
            wrongCars.add(startPositions[i])
        car2slot[startPositions[i]] = i
    curPositions = startPositions
    stepsNum = 0
    while wrongCars:
        stepsNum += 1
        zeroPos = car2slot[0]
        if endPositions[zeroPos] == 0:
            car = wrongCars.pop()
            wrongCars.add(car)
        else:
            car = endPositions[zeroPos]
            wrongCars.remove(car)
        carPos = car2slot[car]
        print("move from {} to {}".format(carPos, zeroPos))
        curPositions[carPos] = 0
        curPositions[zeroPos] = car
        car2slot[car] = zeroPos
        car2slot[0] = carPos
    if curPositions != endPositions:
        raise Exception("Wrong answer!")
    print("{} moves in total".format(stepsNum))
    return stepsNum

rearrangingCars([1, 2, 0, 3], [3, 1, 2, 0])
print()
rearrangingCars([1, 2, 3, 0], [3, 1, 2, 0])
