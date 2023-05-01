def bulls(answer, user_input):
    count = 0
    for i in range(4):
        if answer[i] == user_input[i]:
            count += 1
    return count

