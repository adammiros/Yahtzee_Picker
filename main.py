

def determineBestToKeep(dice1, dice2, dice3, dice4, dice5, dice6):
    # Arrays of each type of value possible (Used to keep track of how many of each type of die
    OnesCount = []
    TwosCount = []
    ThreesCount = []
    FoursCount = []
    FivesCount = []
    SixesCount = []

    # Values Of Each Of The Lists
    OnesValue = 0
    TwosValue = 0
    ThreesValue = 0
    FoursValue = 0
    FivesValue = 0
    SixesValue = 0



    # Checking The First Dices Value
    if dice1 == 1:
        OnesCount.append("Dice_1")

    if dice1 == 2:
        TwosCount.append("Dice_1")

    if dice1 == 3:
        ThreesCount.append("Dice_1")

    if dice1 == 4:
        FoursCount.append("Dice_1")

    if dice1 == 5:
        FivesCount.append("Dice_1")

    if dice1 == 6:
        SixesCount.append("Dice_1")

    # Checking The Second Dices Value
    if dice2 == 1:
        OnesCount.append("Dice_2")

    if dice2 == 2:
        TwosCount.append("Dice_2")

    if dice2 == 3:
        ThreesCount.append("Dice_2")

    if dice2 == 4:
        FoursCount.append("Dice_2")

    if dice2 == 5:
        FivesCount.append("Dice_2")

    if dice2 == 6:
        SixesCount.append("Dice_2")

    # Checking The Third Dices Value
    if dice3 == 1:
        OnesCount.append("Dice_3")

    if dice3 == 2:
        TwosCount.append("Dice_3")

    if dice3 == 3:
        ThreesCount.append("Dice_3")

    if dice3 == 4:
        FoursCount.append("Dice_3")

    if dice3 == 5:
        FivesCount.append("Dice_3")

    if dice3 == 6:
        SixesCount.append("Dice_3")

    # Checking The Fourth Dices Value
    if dice4 == 1:
        OnesCount.append("Dice_4")

    if dice4 == 2:
        TwosCount.append("Dice_4")

    if dice4 == 3:
        ThreesCount.append("Dice_4")

    if dice4 == 4:
        FoursCount.append("Dice_4")

    if dice4 == 5:
        FivesCount.append("Dice_4")

    if dice4 == 6:
        SixesCount.append("Dice_4")

    # Checking The Fifth Dices Value
    if dice5 == 1:
        OnesCount.append("Dice_5")

    if dice5 == 2:
        TwosCount.append("Dice_5")

    if dice5 == 3:
        ThreesCount.append("Dice_5")

    if dice5 == 4:
        FoursCount.append("Dice_5")

    if dice5 == 5:
        FivesCount.append("Dice_5")

    if dice5 == 6:
        SixesCount.append("Dice_5")

    # Checking The Sixth Dices Value
    if dice6 == 1:
        OnesCount.append("Dice_6")

    if dice6 == 2:
        TwosCount.append("Dice_6")

    if dice6 == 3:
        ThreesCount.append("Dice_6")

    if dice6 == 4:
        FoursCount.append("Dice_6")

    if dice6 == 5:
        FivesCount.append("Dice_6")

    if dice6 == 6:
        SixesCount.append("Dice_6")

    OnesValue = 1 * len(OnesCount)
    TwosValue = 2 * len(TwosCount)
    ThreesValue = 3 * len(ThreesCount)
    FoursValue = 4 * len(FoursCount)
    FivesValue = 5 * len(FivesCount)
    SixesValue = 6 * len(SixesCount)

    print("Current State Of Lists: \n")
    print("Ones: " + str(OnesCount) + " -- Length: " + str(len(OnesCount)) + " -- Final Value: " + str(OnesValue))
    print("Twos: " + str(TwosCount) + " -- Length: " + str(len(TwosCount)) + " -- Final Value: " + str(TwosValue))
    print("Threes: " + str(ThreesCount) + " -- Length: " + str(len(ThreesCount)) + " -- Final Value: " + str(ThreesValue))
    print("Fours: " + str(FoursCount) + " -- Length: " + str(len(FoursCount)) + " -- Final Value: " + str(FoursValue))
    print("Ones: " + str(FivesCount) + " -- Length: " + str(len(FivesCount)) + " -- Final Value: " + str(SixesValue))





#Calling main function
determineBestToKeep(1,1,3,4,5,6)


