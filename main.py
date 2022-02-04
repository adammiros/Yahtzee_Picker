def determineBestToKeep(dice1, dice2, dice3, dice4, dice5):
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

    EligibleFor35Bonus = False

    ThreeOfAKindPresent = False
    FourOfAKindPresent = False
    FullHousePresent = False
    SmallStaightPresent = False
    LargeStraightPresent = False

    ThreeOrFourOfAKindDiceTypesPresent = []

    ListOfDiceInTheOrderRolled = []


    ListOfDiceInTheOrderRolled.append(dice1)
    ListOfDiceInTheOrderRolled.append(dice2)
    ListOfDiceInTheOrderRolled.append(dice3)
    ListOfDiceInTheOrderRolled.append(dice4)
    ListOfDiceInTheOrderRolled.append(dice5)


    #Checking for small straight
    if ListOfDiceInTheOrderRolled[0] == 0:
        if ListOfDiceInTheOrderRolled[0] == 0 and ListOfDiceInTheOrderRolled[1] == 1 and ListOfDiceInTheOrderRolled[2] == 2 and ListOfDiceInTheOrderRolled[3] == 3 and ListOfDiceInTheOrderRolled[4] == 4:
            SmallStaightPresent = True

        if ListOfDiceInTheOrderRolled[0] == 0 and ListOfDiceInTheOrderRolled[1] == 2 and ListOfDiceInTheOrderRolled[2] == 3 and ListOfDiceInTheOrderRolled[3] == 4 and ListOfDiceInTheOrderRolled[4] == 5:
            SmallStaightPresent = True

        if ListOfDiceInTheOrderRolled[0] == 0 and ListOfDiceInTheOrderRolled[1] == 3 and ListOfDiceInTheOrderRolled[2] == 4 and ListOfDiceInTheOrderRolled[3] == 5 and ListOfDiceInTheOrderRolled[4] == 6:
            SmallStaightPresent = True

    #Checking for large straight
    if ListOfDiceInTheOrderRolled[0] != 0:
        if ListOfDiceInTheOrderRolled[0] == 1 and ListOfDiceInTheOrderRolled[1] == 2 and ListOfDiceInTheOrderRolled[2] == 3 and ListOfDiceInTheOrderRolled[3] == 4 and ListOfDiceInTheOrderRolled[4] == 5:
            LargeStraightPresent = True

        if ListOfDiceInTheOrderRolled[0] == 2 and ListOfDiceInTheOrderRolled[1] == 3 and ListOfDiceInTheOrderRolled[2] == 4 and ListOfDiceInTheOrderRolled[3] == 5 and ListOfDiceInTheOrderRolled[4] == 6:
            LargeStraightPresent = True



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

    # Checking For A Full House. If Full house is detected, then there is no need to perform additional computations as the score is determined to be 25.
    if LargeStraightPresent != True and SmallStaightPresent != True:
        if len(OnesCount) == 3:
            if len(TwosCount) == 2:
                FullHousePresent = True
            elif len(ThreesCount) == 2:
                FullHousePresent == True
            elif len(FoursCount) == 2:
                FullHousePresent == True
            elif len(FivesCount) == 2:
                FullHousePresent == True

        if len(TwosCount) == 3:
            if len(OnesCount) == 2:
                FullHousePresent = True
            elif len(ThreesCount) == 2:
                FullHousePresent == True
            elif len(FoursCount) == 2:
                FullHousePresent == True
            elif len(FivesCount) == 2:
                FullHousePresent == True

        if len(ThreesCount) == 3:
            if len(OnesCount) == 2:
                FullHousePresent = True
            elif len(TwosCount) == 2:
                FullHousePresent == True
            elif len(FoursCount) == 2:
                FullHousePresent == True
            elif len(FivesCount) == 2:
                FullHousePresent == True

        if len(FoursCount) == 3:
            if len(OnesCount) == 2:
                FullHousePresent = True
            elif len(TwosCount) == 2:
                FullHousePresent == True
            elif len(ThreesCount) == 2:
                FullHousePresent == True
            elif len(FivesCount) == 2:
                FullHousePresent == True

        if len(FivesCount) == 3:
            if len(OnesCount) == 2:
                FullHousePresent = True
            elif len(TwosCount) == 2:
                FullHousePresent == True
            elif len(ThreesCount) == 2:
                FullHousePresent == True
            elif len(FoursCount) == 2:
                FullHousePresent == True
            print("---")
            print("Full House?: " + str(FullHousePresent))

        if FullHousePresent == False:
            #Calculate the values of each type of dice rolled all toghether
            OnesValue = 1 * len(OnesCount)
            TwosValue = 2 * len(TwosCount)
            ThreesValue = 3 * len(ThreesCount)
            FoursValue = 4 * len(FoursCount)
            FivesValue = 5 * len(FivesCount)

            #Calculating final score of the upper section
            TotalCombinedValue = OnesValue + TwosValue + ThreesValue + FoursValue + FivesValue


            #Checking for 35 point bonus
            if TotalCombinedValue > 63:
                EligibleFor35Bonus = True
                TotalCombinedValue += 35

            #Checking for three of a kind
            if len(OnesCount) == 3:
                ThreeOfAKindPresent = True
                ThreeOrFourOfAKindDiceTypesPresent.append(("Ones"))

            if len(TwosCount) == 3:
                ThreeOfAKindPresent = True
                ThreeOrFourOfAKindDiceTypesPresent.append(("Tows"))

            if len(ThreesCount) == 3:
                ThreeOfAKindPresent = True
                ThreeOrFourOfAKindDiceTypesPresent.append(("Threes"))

            if len(FoursCount) == 3:
                ThreeOfAKindPresent = True
                ThreeOrFourOfAKindDiceTypesPresent.append(("Fours"))

            if len(FivesCount) == 3:
                ThreeOfAKindPresent = True
                ThreeOrFourOfAKindDiceTypesPresent.append(("Fives"))

            # Checking for four of a kind
            if len(OnesCount) == 4:
                FourOfAKindPresent = True
                ThreeOrFourOfAKindDiceTypesPresent.append(("Ones"))

            if len(TwosCount) == 4:
                FourOfAKindPresent = True
                ThreeOrFourOfAKindDiceTypesPresent.append(("Tows"))

            if len(ThreesCount) == 4:
                FourOfAKindPresent = True
                ThreeOrFourOfAKindDiceTypesPresent.append(("Threes"))

            if len(FoursCount) == 4:
                FourOfAKindPresent = True
                ThreeOrFourOfAKindDiceTypesPresent.append(("Fours"))

            if len(FivesCount) == 4:
                FourOfAKindPresent = True
                ThreeOrFourOfAKindDiceTypesPresent.append(("Fives"))



        print("Current State Of Lists: \n")
        if FullHousePresent == False:
            print("35 Point Bonus?: " + str(EligibleFor35Bonus))
            print("Total Value Of All Rolled Dice (Upper): " + str(TotalCombinedValue) + "\n")
            print("3 Of A Kind?: " + str(ThreeOfAKindPresent))
            print("4 Of A Kind?: " + str(FourOfAKindPresent))
        print("------")

        # Checking wether to keep the upper value score or to utilize three / four of a kind score
        if ThreeOfAKindPresent != False or FourOfAKindPresent != False:
            if ThreeOrFourOfAKindDiceTypesPresent[0] == "Ones":
                if OnesValue > TotalCombinedValue:
                    print("Do not go with one of a kind!!! Ones have a total combined " + str(OnesValue) + " versus the one of a kind total score of " + str(TotalCombinedValue))
                else:
                    print("Go with one of a kind!! Sixes have a total combined " + str(OnesValue) + " versus the one of a kind total score of " + str(TotalCombinedValue))

        if ThreeOfAKindPresent != False or FourOfAKindPresent != False:
            if ThreeOrFourOfAKindDiceTypesPresent[0] == "Tows":
                if TwosValue > TotalCombinedValue:
                    print("Do not go with one of a kind!!! Tows have a total combined " + str(TwosValue) + " versus the one of a kind total score of " + str(TotalCombinedValue))
                else:
                    print("Go with one of a kind!! Tows have a total combined " + str(TwosValue) + " versus the one of a kind total score of " + str(TotalCombinedValue))

        if ThreeOfAKindPresent != False or FourOfAKindPresent != False:
            if ThreeOrFourOfAKindDiceTypesPresent[0] == "Threes":
                if ThreesValue > TotalCombinedValue:
                    print("Do not go with one of a kind!!! Threes have a total combined " + str(ThreesValue) + " versus the one of a kind total score of " + str(TotalCombinedValue))
                else:
                    print("Go with one of a kind!! Threes have a total combined " + str(ThreesValue) + " versus the one of a kind total score of " + str(TotalCombinedValue))

        if ThreeOfAKindPresent != False or FourOfAKindPresent != False:
            if ThreeOrFourOfAKindDiceTypesPresent[0] == "Fours":
                if FoursValue > TotalCombinedValue:
                    print("Do not go with one of a kind!!! Fours have a total combined " + str(FoursValue) + " versus the one of a kind total score of " + str(TotalCombinedValue))
                else:
                    print("Go with one of a kind!! Fours have a total combined " + str(FoursValue) + " versus the one of a kind total score of " + str(TotalCombinedValue))


        if ThreeOfAKindPresent != False or FourOfAKindPresent != False:
            if ThreeOrFourOfAKindDiceTypesPresent[0] == "Fives":
                if FivesValue > TotalCombinedValue:
                    print("Do not go with one of a kind!!! Fives have a total combined " + str(FivesValue) + " versus the one of a kind total score of " + str(TotalCombinedValue))
                else:
                    print("Go with one of a kind!! Fives have a total combined " + str(FivesValue) + " versus the one of a kind total score of " + str(TotalCombinedValue))






        if FullHousePresent == False:
            print("------")
        print("Ones: " + str(OnesCount) + " -- Length: " + str(len(OnesCount)) + " -- Final Value: " + str(OnesValue))
        print("Twos: " + str(TwosCount) + " -- Length: " + str(len(TwosCount)) + " -- Final Value: " + str(TwosValue))
        print("Threes: " + str(ThreesCount) + " -- Length: " + str(len(ThreesCount)) + " -- Final Value: " + str(ThreesValue))
        print("Fours: " + str(FoursCount) + " -- Length: " + str(len(FoursCount)) + " -- Final Value: " + str(FoursValue))
        print("Fives: " + str(FivesCount) + " -- Length: " + str(len(FivesCount)) + " -- Final Value: " + str(FivesValue))
    else:
        if LargeStraightPresent == True:
            print("Large Straight Present. The final score is 40")

        elif SmallStaightPresent == True:
            print("Small Straight Present. The final score is 30")





#Calling main function
determineBestToKeep(1,2,3,4,5)


