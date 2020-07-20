def parse(value):
    # inputVals = set(value)
    # if( value == "I"):
    #     return 1
    # elif (value == "II"):
    #     return 2
    # elif (value == "III"):
    #     return 3
    # elif (value == "IV"):
    #     return 4
    # elif (value == "V"):
    #     return 5
    # elif (value == "VI"):
    #     return 6
    # elif (value == "VII"):
    #     return 7
    # elif (value == "VIII"):
    #     return 8
    number =0

    if (value == "IV"):
        return 4
    if (value == "IX"):
        return 9

    for i in value:
        if i == "I":
            number +=1
        elif i == "V":
            number +=5
        elif i == "X":
            number +=10

    return number
