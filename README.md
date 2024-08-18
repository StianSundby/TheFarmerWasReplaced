
# The Farmer Was Replaced - Code

This is all the code I wrote for [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/). It includes functionalities for farming all crops (including special logic for pumpkins, sunflowers and cacti), solving mazes, and the dinosaur shenanigans. The code is modularized into different files, each handling specific tasks within the game.

![The Farmer Was Replaced](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2060160/capsule_616x353.jpg?t=1704041534)

## Algorithms used

- Bubble Sort: Used in cactus.py to sort cacti in rows and columns.
- Depth-First Search (DFS): Used in treasurehunt.py for solving mazes.
- Greedy Approach: Used in sunflower.py to harvest the highest-value sunflowers.
## Modules

1. `main.py`

The entry point of the application. It initializes the game environment, sets up farming parameters, and manages the main farming loop.
Key Functions:
- init(): Initializes the game environment.
- start(): Starts the farming process based on the specified parameters.

2. `farming.py`

Description: Contains core farming functionalities.
Key Functions:
- `prepareFarm()`: Prepares the farm by harvesting the grass and then tilling
- `farmingCycle()`: Manages the farming cycle for various entities and conditions.
- `checkWater()`: Checks and manages the water level. Ensuring the field is watered to the threshold set in `main.py`

3. `inventory.py`

Description: Handles inventory checks and item management.
Key Functions:
- `checkSeedCount(entity)`: Ensures adequate seeds are available for farming.
- `printMessage()`: Prints messages regarding item purchases.

4. `movement.py`

Description: Manages movement within the game world.
Key Functions:
- `moveInDirection(direction)`: Moves in a specified direction.
- `oppositeDirection(direction)`: Returns the opposite direction.
- `moveToOrigin()`: Moves to the origin (0,0) position.
- `moveToPosition(x, y)`: Moves to a specific position.

5. `pumpkin.py`

Description: Manages pumpkin farming.
Key Functions:
`farmPumpkins()`: Ensures that you grow the largest pumpkin possible before harvesting.

6. `treasurehunt.py`

Description: Manages treasure hunting tasks.
Key Functions:
- `treasureHunt()`: Uses a Depth-First Search (DFS) algorithm to locate treasure. An algorithm like A* would be better suited here, and I never got around to implementing the reuse of mazes.
- `plantMaze(plant_maze)`: Generates the maze by fertilizing a fully grown bush.

7. `polyculture.py`

Description: Implements polyculture farming techniques.
Key Functions:
- `fieldGrid()`: Creates a grid the same size as the field with specified entities.
- `polyculture()`: Performs polyculture farming, planting and harvesting based on conditions.

8. `sunflower.py`
Description: Contains logic for harvesting sunflowers.
Key Functions:
- `harvestSunflower()`: Harvests sunflowers based on their value, prioritizing the highest-value sunflowers.

9. `cactus.py`

Description: Contains logic for sorting cacti in the game world.
Key Functions:
- `sortCacti()`: Sorts cacti in both rows and columns using a bubble sort-like algorithm.

10. `dinosaur.py`

Description: Manages dinosaur-related farming tasks.
Key Functions:
- `dinosaurFarming()`: Handles the spawning and harvesting of dinosaurs.
- `spawnDinos(sze)`: Spawns dinosaurs on the farm.
- `harvestDinosaurs()`: Harvests groups of dinosaurs of the same type.
- `randomEntitySwap()`: Randomly swaps entities to optimize the farm.
## License

This code is provided as-is. Feel free to modify and adapt it for personal use or within the bounds of the game’s terms of service.
