from movement import moveToPosition


def sortCacti(size):
    # Rows
    for y in range(size):
        while True:
            sorted_row = True
            for x in range(size - 1):  # loop until the second last element in the row
                moveToPosition(x, y)
                current_cactus = measure()
                east_cactus = measure(East)

                if current_cactus > east_cactus:
                    swap(East)
                    sorted_row = False  # a swap was made
                    move(West)

            if sorted_row:
                break

    # Columns
    for x in range(size):
        while True:
            sorted_column = True
            for y in range(
                size - 1
            ):  # Loop until the second last element in the column
                moveToPosition(x, y)
                current_cactus = measure()
                south_cactus = measure(North)

                if current_cactus > south_cactus:
                    swap(North)
                    sorted_column = False  # a swap was made
                    move(North)

            if sorted_column:
                break
