from builtins import range
from movement import moveInDirection, oppositeDirection, moveToOrigin


# Depth-First-Search
def treasureHunt(visited):
    currentX, currentY = get_pos_x(), get_pos_y()  # current position

    if get_entity_type() == Entities.Treasure:
        harvest()
        return True

    addToVisited(currentX, currentY, visited)  # mark current position as visited

    directions = [North, East, South, West]
    for direction in directions:
        nextX, nextY = moveInDirection(direction)
        if not isVisited(nextX, nextY, visited) and move(direction):
            if treasureHunt(visited):  # recursively search from the new position
                return True
            move(oppositeDirection(direction))  # return to the previous position

    return False  # No treasure found in any direction from this position


def plantMaze(plant_maze):
    visited = []  # keep track of visited positions

    if plant_maze:
        moveToOrigin()  # [x0, y0]

        plant(Entities.Bush)
        for _ in range(5):  # wait for bush to grow
            do_a_flip()

        while get_entity_type() == Entities.Bush:
            use_item(Items.Fertilizer)
            if num_items(Items.Fertilizer) == 0:
                trade(Items.Fertilizer, 10)

    treasureHunt(visited)


def isVisited(x, y, visited):
    return (x, y) in visited  # check if the given position has already been visited


def addToVisited(x, y, visited):
    visited.append((x, y))  # add the given position to the list of visited positions
