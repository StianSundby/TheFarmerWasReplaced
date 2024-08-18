def moveInDirection(direction):
    if direction == North:
        return (get_pos_x(), get_pos_y() + 1)  # north/up increases y
    elif direction == South:
        return (get_pos_x(), get_pos_y() - 1)  # south/down decreases y
    elif direction == East:
        return (get_pos_x() + 1, get_pos_y())  # east/right increases x
    elif direction == West:
        return (get_pos_x() - 1, get_pos_y())  # west/left decreases x


def oppositeDirection(direction):
    if direction == North:
        return South
    elif direction == South:
        return North
    elif direction == East:
        return West
    elif direction == West:
        return East


def moveToOrigin():  # move to origin (x0,y0)
    while get_pos_x() != 0:
        move(West)
    while get_pos_y() != 0:
        move(South)


def moveToPosition(targetX, targetY):
    currentX, currentY = get_pos_x(), get_pos_y()
    while currentX < targetX:
        move(East)
        currentX += 1
    while currentX > targetX:
        move(West)
        currentX -= 1
    while currentY < targetY:
        move(North)
        currentY += 1
    while currentY > targetY:
        move(South)
        currentY -= 1


def moveRowWest(size):  # move along a row to the first tile
    for _ in range(size - 1):
        move(West)
