from builtins import range
from movement import moveToOrigin


def farmPumpkins(size):
    for _ in range(size):  # row
        for _ in range(size):  # column
            plant(Entities.Pumpkin)
            move(North)  # next tile
        move(East)  # next column

    while True:
        moveToOrigin()
        missing = False

        for _ in range(size):  # row
            for _ in range(size):  # column
                if get_entity_type() != Entities.Pumpkin:
                    missing = True
                    plant(Entities.Pumpkin)
                move(North)  # next tile
            move(East)  # next column

        if not missing:
            break

    moveToOrigin()
    harvest()
