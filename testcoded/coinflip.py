from random import randint

def cointoss(tosser):
    tot = 0
    flips = 0
    for toss in range (1, tosser):
        flips += 1
        if randint(0, 1) == 0:
            while randint(0, 1) == 0:
                flips += 1
            flips +=1
        else:
            while randint(0, 1) == 1:
                flips += 1
            flips += 1
    return (flips, tosser, flips / tosser)

print (cointoss(int(input("How many tosses would you like?"))))
