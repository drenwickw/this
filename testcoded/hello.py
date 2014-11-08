'''
phrase = input("Let's have a phrase, then")
print (phrase * 10) # this is a comment in here
print ("Your phrase is {} characters long".format(len(phrase)))

print (phrase[3:12])


def square(number): #this defines the function and specifies the argument that it will allow
    sqr_num = number ** 2
    return sqr_num

input_num = len(phrase)
#int(input('Please provide a number'))
output_num = square(input_num)

print ("The length of your word in characters squared is", output_num)


def cube(num1):
    answer = num1 ** 3
    return answer

num1 = int(input("Please enter an integer"))
num2 = cube(num1)

print ("your number cubed is {}.".format(num2))


def multiply(num3, num4):
    mult = num3 * num4
    return mult

num3 = int(input('Please enter your first number: '))
num4 = int(input("Please enter your second number: "))

twat = multiply(num3, num4)

print ('Your two numbers ({} and {}) multiplied equals: {}'.format(num3, num4, twat))
'''

print ('***' * 10)
print ('\n\n\n')
print ('***' * 10)

print ('Now it\'s time for some temperature conversion:')

def cel_to_far(cel):
    far = cel * 9/5 + 32
    return far

cel = int(input("Enter your celcius figure"))
converted1 = cel_to_far(cel)
print ('Your celcius figure in fahrenheit is {}'.format(int(converted1)))


def far_to_cel(far):
    cel = (far1 - 32) * 5/9
    return cel

far1 = int(input('Now enter a fahrenheit figure'))
converted2 = far_to_cel(far1)
print ('Your fahrenheit figure in celcius is {}'.format(int(converted2)))
