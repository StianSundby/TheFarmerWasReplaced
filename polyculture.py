from builtins import range
from movement import moveToPosition
from inventory import checkSeedCount


def fieldGrid(size, initialEntity):
    # create a grid of the given size
    grid = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(initialEntity)
        grid.append(row)
    return grid


# this sucks and should be improved
def polyculture(size, water):
    field = fieldGrid(size, Entities.Grass)  # initialize the field grid with Grass
    while True:
        for x in range(size):
            for y in range(size):
                moveToPosition(x, y)
                if get_ground_type() == Grounds.Soil:
                    entity = field[x][y]
                    if can_harvest():
                        harvest()
                        if entity == Entities.Carrots:
                            till()
                            checkSeedCount(size, entity)
                        plant(entity)

                        if water > 0 and get_water() <= water:
                            if num_items(Items.Water_Tank) == 0:
                                trade(Items.Empty_Tank, 1)
                            else:
                                use_item(Items.Water_Tank)

                    companion = get_companion()
                    if companion != None:
                        companionEntity, cx, cy = companion
                        if (
                            get_ground_type() == Grounds.Soil
                            and field[cx][cy] == Entities.Grass
                        ):
                            field[cx][cy] = companionEntity  # set companion entity
                            plant(companionEntity)

                else:
                    plant(Entities.Grass)

                move(North)  # next tile in row
            move(East)  # next row
