import random
import math

lower = int(input("Enter lower bound - "))
upper = int(input("enter upper bound - "))

rannum = random.randint(lower, upper)
print("\n\t you've only", round(math.log(upper - lower + 1, 2)),"chances to guess the Integer! \n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number -"))

    if rannum == guess:
        print("congratulations you did it in",count,"try")
        break
    elif rannum > guess:
        print("Try again, You guessed too small")
    elif rannum < guess:
        print("Try again, You guessed too high")


if count >= math.log(upper - lower + 1, 2):
    print("\n The number is %d" % rannum)
    print("\t Better Luck Next Time!")

