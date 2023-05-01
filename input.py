import bulls
import bulls_and_cows_answer
import cow

randomNum = bulls_and_cows_answer.create_answer()

guessNum = list(input("Guess your number:" ))

bullsCount = bulls.bulls()
cowsCount = cow.cow()

print(f'bulls: {bullsCount} cows: {cowsCount}')


