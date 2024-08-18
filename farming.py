from builtins import range
from inventory import checkSeedCount
from pumpkin import farmPumpkins
from polyculture import polyculture
from sunflower import harvestSunflower
from cactus import sortCacti


def prepareFarm(size):  # harvesting and till each cell in a grid
    for _ in range(size):
        for _ in range(size):
            if can_harvest():
                harvest()
                till()
            move(North)  # next tile in column
        move(East)  # next column


def farmingCycle(size, entity, waterLevel, poly):
    checkSeedCount(size, entity)

    if entity == Entities.Pumpkin:
        farmPumpkins(size)  # special conditions
    else:
        farm(size, entity, waterLevel)  # regular planting

    if poly:
        polyculture(size, waterLevel)  # switch to poly after initial planting
    elif entity == Entities.Sunflower:
        harvestSunflower(size)  # special conditions


def checkWater(waterLevel):
    if waterLevel > 0 and get_water() <= waterLevel:
        if num_items(Items.Water_Tank) == 0:
            trade(Items.Empty_Tank, 1)
        else:
            use_item(Items.Water_Tank)


def farm(size, entity, waterLevel):
    for _ in range(size):
        for _ in range(size):
            if (
                can_harvest()
                and entity != Entities.Sunflower
                and entity != Entities.Cactus
            ):
                harvest()  # harvest if crop is ready and not a Sunflower or Cactus

            if entity == Entities.Tree:
                if (get_pos_x() + get_pos_y()) % 2 == 0:  # gap between trees
                    plant(entity)
            else:
                if entity != Entities.Grass:
                    plant(entity)

            checkWater(waterLevel)

            move(North)  # next tile in column
        move(East)  # next column

    if entity == Entities.Cactus:
        sortCacti(size)  # sort before harvesting
    if entity != Entities.Sunflower:
        harvest()
