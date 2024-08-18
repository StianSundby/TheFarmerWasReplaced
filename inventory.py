def checkSeedCount(size, entity):
    if num_items(Items.Fertilizer) < 10:
        printMessage(Items.Fertilizer, size)  # always stock up on fertilizer

    if entity == Entities.Carrots:
        if num_items(Items.Carrot_Seed) < size:
            printMessage(Items.Carrot_Seed, size)

    elif entity == Entities.Pumpkin:
        if num_items(Items.Pumpkin_Seed) < size:
            printMessage(Items.Pumpkin_Seed, size)

    elif entity == Entities.Sunflower:
        if num_items(Items.Sunflower_Seed) < size:
            printMessage(Items.Sunflower_Seed, size)

    elif entity == Entities.Cactus:
        if num_items(Items.Cactus_Seed) < size:
            printMessage(Items.Cactus_Seed, size)


def printMessage(itemToBuy, size):
    currentStock = num_items(itemToBuy)
    priceOfOneItem = get_cost(itemToBuy)
    currencyEntity = list(priceOfOneItem)[0]
    currencyNeededForOneItem = priceOfOneItem[currencyEntity]
    amountToBuy = ((size * size) * 8) - currentStock
    totalPrice = amountToBuy * currencyNeededForOneItem
    currentCurrency = num_items(currencyEntity)
    currencyNeededForAllItems = totalPrice - currentCurrency

    if currentCurrency < totalPrice:
        print(
            "Can't afford ",
            amountToBuy,
            " ",
            itemToBuy,
            "(s). You need a total of ",
            currencyNeededForAllItems,
            " more ",
            currencyEntity,
            "(s).",
        )
    else:
        trade(itemToBuy, amountToBuy)

        bought = num_items(itemToBuy) - currentStock
        spent = currentCurrency - (totalPrice - num_items(currencyEntity))

        print(
            "Bought ",
            bought,
            " ",
            itemToBuy,
            "(s) for ",
            spent,
            " ",
            {currencyEntity},
            "(s).",
        )
