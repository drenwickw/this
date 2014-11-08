'''
repeat = True

while repeat:
    try:
        my_input = input('Type an integer here -->')
        print (int(my_input))
        repeat = False

    except ValueError:
        print ("try again")

'''
from random import randint


def coin_flip(number):
    heads = 0
    tails = 0
    for trial in range(0, number):
        while randint(0, 1) == 0:
            heads += 1
        tails += 1
    return heads / tails
print (coin_flip(100000))


print (randint(0, 6))

print ('\n\n\n')

def dice(rolls):
    tot = 0
    try:
        for i in range (1, rolls + 1):
            roll = randint(1, 6)
            tot = tot + roll
        return tot / rolls
    except rolls > 1000000:
        print ('Too many rolls, mate')
rolls = int(input("how many times?"))
print (dice(rolls))