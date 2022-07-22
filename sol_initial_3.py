import numpy as np
import random as rd

def intiialize(A, B, n):
    """
    intiialize the schedule
    """
    
    original_schedule = np.zeros((n,28)) 

    nb = 0
    for i in range(nb): #line
        v = 0
        for j in range(4): #column
            original_schedule[i][0+v] = 2
            original_schedule[i][2+v] = 1            
            v += 7
    nb += B

    for i in range(nb,nb+B):
        v = 0
        for j in range(4):
            original_schedule[i][1+v] = 2
            original_schedule[i][3+v] = 1
            v += 7
    nb += B

    for i in range(nb,nb+B):
        v = 0
        for j in range(4):    
            original_schedule[i][2+v] = 2
            original_schedule[i][4+v] = 1
            v += 7
    nb += B 

    for i in range(nb,nb+B):
        v = 0
        for j in range(4):     
            original_schedule[i][3+v] = 2
            original_schedule[i][5+v] = 1       
            v += 7
    nb += B 

    for i in range(nb,nb+B):
        v = 0
        for j in range(4):     
            original_schedule[i][4+v] = 2
            original_schedule[i][6+v] = 1
            v += 7
    nb += B 


    for i in range(nb,nb+B):
        v = 0
        for j in range(4):     
            original_schedule[i][5+v] = 2
            original_schedule[i][0+v] = 1
            v += 7
    nb += B 

    for i in range(nb,nb+B):
        v = 0
        for j in range(4):     
            original_schedule[i][6+v] = 2
            original_schedule[i][1+v] = 1
            v += 7

    nb = 0
    diff = A-B

    for i in range(diff):
        v = 0
        for j in range(4):
            original_schedule[i][6+v] = 1       
            v += 7
    nb += B

    for i in range(diff):
        v = 0
        for j in range(4):
            original_schedule[nb+i][0+v] = 1
            v += 7
    nb += B 

    for i in range(diff):
        v = 0
        for j in range(4):    
            original_schedule[nb+i][1+v] = 1
            v += 7
    nb += B 

    for i in range(diff):
        v = 0
        for j in range(4):     
            original_schedule[nb+i][2+v] = 1       
            v += 7
    nb += B 

    for i in range(diff):
        v = 0
        for j in range(4):     
            original_schedule[nb+i][3+v] = 1
            v += 7
    nb += B 

    for i in range(diff):
        v = 0
        for j in range(4):     
            original_schedule[nb+i][4+v] = 1
            v += 7
    nb += B 

    for i in range(diff):
        v = 0
        for j in range(4):     
            original_schedule[nb+i][5+v] = 1
            v += 7
    nb += B 

    return original_schedule

def fitness(original_schedule,n):
    """
    calculate the workload of each nurse over the 28-day horizon through shift penalties
    """
    hardship = [0]*n
    for i in range(0,n,1):
        Nb1, Nb2 = 0, 0
        for j in range(0,5,1):
            if original_schedule[i][j] == 1: # determine the number of "day" shifts for each nurse
                Nb1 = Nb1+1
            elif original_schedule[i][j] == 2: # determine the number of "night" shifts for each nurse
                Nb2 = Nb2+1

        hardship[i] = Nb1*1 + Nb2*2 # Store the total penalties for each nurse in a table of dimension n
    return hardship_max(hardship, n) - hardship_min(hardship, n) 

def hardship_min(hardship, n):
    """
    find the least busy nurse's hardship
    """
    hardship_min_ = hardship[0]
    for i in range(n):
        if hardship[i] < hardship_min_:
            hardship_min_ = hardship[i]
    return hardship_min_

def hardship_max(hardship, n):
    """
    find the hardest working nurse
    """
    hardship_max_ = hardship[0]
    for i in range(n):
        if hardship[i]>hardship_max_:
            hardship_max_ = hardship[i]
    return hardship_max_

def main():
    A = 4 #number of nurses needed in the "day" team
    B = 2 #number of nurses in the "night" team, which must be greater than or equal to half of A
    n = B*7 #total of nurses

    original_schedule = intiialize(A, B, n)
    ValueObjectufFunction = fitness(original_schedule, n)

    print(original_schedule)
    print("La valeur de la fonction objectif relié à cette solution est : ",ValueObjectufFunction)

if __name__ == "__main__":
    main()