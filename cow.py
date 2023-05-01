def cow(randomNum, inputNum):
    cowCount = 0
    for num in inputNum:
        if num in randomNum:
            cowCount += 1
            randomNum.remove(num)
    return cowCount
