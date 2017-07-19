class Move:
    """
    Class that stores data about movement between two slots.
    """
    def __init__(self, _from, _to):
        self._from = _from
        self._to = _to

    def __eq__(self, other):
        return self._from == other._from and self._to == other._to

    def __str__(self):
        return "Move the car from slot {} to splot {}.".format(self._from,
                                                                self._to)


def rearrangingCars(initalState, desiredState, toPrint = False):
    """
    There is a parking lot with N spaces and N-1 cars in it. The parking lot is
    described by an array of numbers, where numbers from 1 to N-1 mean cars, and
    the number 0 means an empty parking space. Only one car can be moved at a
    time to the empty slot.
    This functions can rearrange cars from inital state of parking lot to
    desired state of parking lot.

    Input:
        initalState:  list of integers, a permutation of the numbers 0 to N.
                      Inital state of parking lot.
        desiredState: list of integers, a permutation of the numbers 0 to N.
                      State of parking lot that we want to get by moving cars.
        toPrint:      a boolean, True if function should print the sequence of
                      moves from initalState to desiredState,
                      and False otherwise.

    Return:
        list of Move, sequence of moves from state initalState
        to state desiredState.
    """
    slotNums = len(initalState)
    car2slot = [0] * slotNums

    # create a set of cars that stand on wrong slot, comparing to desiredState
    # and create map car2slot
    wrongCars = set()
    for pos in range(slotNums):
        # first condition skips 0 because it isn't a car
        if initalState[pos] and initalState[pos] != desiredState[pos]:
            wrongCars.add(initalState[pos])
        car2slot[initalState[pos]] = pos

    currentState = initalState
    moves = list()

    # while we have at least one car that stands on a wrong position
    while wrongCars:
        zeroPos = car2slot[0]

        # choose a car that we will move at this step
        if desiredState[zeroPos] == 0:
            # Positions of empty slots match with each other. In that case, we
            # can pick up any wrong car. But we wont fix its position, so we
            # need to return it to the set
            car = wrongCars.pop()
            wrongCars.add(car)
        else:
            # everything is okey, so we can move a car that should stay at
            # zeroPos in desiredState
            car = desiredState[zeroPos]
            wrongCars.remove(car)

        # move chosen car
        carPos = car2slot[car]
        currentState[carPos] = 0
        currentState[zeroPos] = car
        car2slot[car] = zeroPos
        car2slot[0] = carPos
        moves.append(Move(carPos, zeroPos))

    if toPrint:
        for m in moves:
            print(m)
        print("{} moves in total.".format(len(moves)))

    return moves
