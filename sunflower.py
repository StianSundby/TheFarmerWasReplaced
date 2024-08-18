from movement import moveToOrigin, moveRowWest, moveToPosition


def harvestSunflower(size):
    # upgrade speed if possible
    if get_cost(Unlocks.Speed)[Items.Power] <= num_items(Items.Power):
        unlock(Unlocks.Speed)
    moveToOrigin()

    highestValue = 7  # min - 15 is max
    highestPosX = 0
    highestPosY = 0

    for x in range(size):  # row
        for y in range(size):  # column
            value = measure()

            if value == None:
                continue

            if value == 15:  # max value
                harvest()
                break

            if value > highestValue:
                highestValue = (
                    value  # update highest value sunflower and its coordinates
                )
                highestPosX = x
                highestPosY = y

            if y < size - 1:
                move(East)

            else:
                if x < size - 1:
                    move(South)  # next row
                    moveRowWest(size)  # back to start of row
        if value == 15:
            break

    if highestValue != 15:
        moveToPosition(highestPosX, highestPosY)
        harvest()
