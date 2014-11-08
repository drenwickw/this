input("Enter your word here")
while True:
    my_input = input('Type q or Q to quit: ')
    if my_input.upper() == 'Q':
        break

for i in range(1, 51):
    if i % 3 == 0:
        continue
    else:
        print (i)

try:
    number = int(input("Enter a non zero integer here"))
    print ("10 / {} = {}".format(number, 10.0 / number))
except ValueError:
    print ("You didn't enter an integer.")
except ZeroDivisionError:
    print ('You can\'t enter a zero')


for i in range(0, 4):
    if i == 2:
        continue
    print (i)

print ('finished with i = {}'.format(str(i)))

for i in range(0, 4):
    if i == 2:
        break
    print (i)

print ('finished with i = {}'.format(str(i)))



''' def this(number):
    for i in range (1, number + 1):
        if number % i == 0:
            print ("{} is a divisor of {}".format(i, number))

number = int(input("Enter a positive integer: "))

this(number)
'''