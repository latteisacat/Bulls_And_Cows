def cow(randomNum, inputNum):
    count = 0
    for i in range(4):
        if inputNum[i] in randomNum:
            if inputNum[i] != randomNum[i]:
                count += 1
    return count
