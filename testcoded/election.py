from random import random



def election(number):
    A_elections = 0
    B_elections = 0
    
    for election in range(1, number+1):
        A_wins = 0
        B_wins = 0
        if random() < 0.87:
            A_wins += 1
        else: 
            B_wins += 1
        if random() < 0.65:
            A_wins +=1
        else:
            B_wins += 1
        if random() < 0.17:
            A_wins += 1
        else:
            B_wins += 1
        if A_wins > B_wins:
            A_elections += 1
        else:
            B_elections += 1
   
    print (A_elections)
    
    print (B_elections)

    return (A_elections/number, B_elections/number, (A_elections/number) + (B_elections/number), A_elections, B_elections, A_elections + B_elections)



print(election(int(input("How many elections?"))))


