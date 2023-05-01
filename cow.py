def cow(randomNum, inputNum):
    count = 0
    for num in inputNum:
        if num in randomNum:
            count += 1
    return count
