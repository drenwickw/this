def invest(amount, rate, time):
    print ("principal amount: ${}".format(amount))
    print ("annual rate of return: {}%".format(rate))
    for t in range(1, time + 1):
        amount = amount * (1 + rate)
        print ('year {}: $ {}'.format(t, (str(amount)))) 
    print ()

amount = float(input("How much?"))
rate = float(input('What rate?'))
time = int(input('For how long?'))

invest(amount, rate, time)