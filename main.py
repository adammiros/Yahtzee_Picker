

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

    EligibleFor35Bonus = False

    ThreeOfAKindPresent = False
    FourOfAKindPresent = False

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

    #Calculate the values of each type of dice rolled all toghether
    OnesValue = 1 * len(OnesCount)
    TwosValue = 2 * len(TwosCount)
    ThreesValue = 3 * len(ThreesCount)
    FoursValue = 4 * len(FoursCount)
    FivesValue = 5 * len(FivesCount)
    SixesValue = 6 * len(SixesCount)

    #Calculating final score of the upper section
    TotalCombinedValue = OnesValue + TwosValue + ThreesValue + FoursValue + FivesValue + SixesValue


    #Checking for 35 point bonus
    if TotalCombinedValue > 63:
        EligibleFor35Bonus = True
        TotalCombinedValue += 35

    #Checking for three of a kind
    if len(OnesCount) == 3:
        ThreeOfAKindPresent = True

    if len(TwosCount) == 3:
        ThreeOfAKindPresent = True

    if len(ThreesCount) == 3:
        ThreeOfAKindPresent = True

    if len(FoursCount) == 3:
        ThreeOfAKindPresent = True

    if len(FivesCount) == 3:
        ThreeOfAKindPresent = True

    if len(SixesCount) == 3:
        ThreeOfAKindPresent = True

    # Checking for four of a kind
    if len(OnesCount) == 4:
        FourOfAKindPresent = True

    if len(TwosCount) == 4:
        FourOfAKindPresent = True

    if len(ThreesCount) == 4:
        FourOfAKindPresent = True

    if len(FoursCount) == 4:
        FourOfAKindPresent = True

    if len(FivesCount) == 4:
        FourOfAKindPresent = True

    if len(SixesCount) == 4:
        FourOfAKindPresent = True









    print("Current State Of Lists: \n")
    print("35 Point Bonus?: " + str(EligibleFor35Bonus))
    print("Total Value Of All Rolled Dice (Upper): " + str(TotalCombinedValue) + "\n")
    print("-------")
    print("3 Of A Kind?: " + str(ThreeOfAKindPresent))
    print("4 Of A Kind?: " + str(FourOfAKindPresent))
    print("Full House?: ")
    print("Ones: " + str(OnesCount) + " -- Length: " + str(len(OnesCount)) + " -- Final Value: " + str(OnesValue))
    print("Twos: " + str(TwosCount) + " -- Length: " + str(len(TwosCount)) + " -- Final Value: " + str(TwosValue))
    print("Threes: " + str(ThreesCount) + " -- Length: " + str(len(ThreesCount)) + " -- Final Value: " + str(ThreesValue))
    print("Fours: " + str(FoursCount) + " -- Length: " + str(len(FoursCount)) + " -- Final Value: " + str(FoursValue))
    print("Ones: " + str(FivesCount) + " -- Length: " + str(len(FivesCount)) + " -- Final Value: " + str(SixesValue))





#Calling main function
determineBestToKeep(0,3,3,3,2,4)


