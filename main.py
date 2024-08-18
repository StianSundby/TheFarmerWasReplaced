from inventory import checkSeedCount
from farming import farmingCycle, prepareFarm
from treasureHunt import plantMaze


def init():
    clear()
    do_a_flip()


def start():
    init()
    size = get_world_size()
    maze = False  # enable or diable Maze (will override poly and regular farming)
    poly = (
        False  # enable or disable Polyculture farming (will override regular farming)
    )
    entity = Entities.Cactus  # specify which plant to farm
    waterLevel = 0.3  # minimum water level threshold

    # Prepare the farming area if necessary
    if (
        entity not in [Entities.Grass, Entities.Bush]
        and get_ground_type() != Grounds.Soil
        and not maze
    ):
        prepareFarm(size)

    # Main farming loop
    while True:
        checkSeedCount(size, entity)

        if maze:
            plantMaze(True)
        else:
            farmingCycle(size, entity, waterLevel, poly)


start()  # entry
