import numpy as np
import random as rd

# a = 6 
# b = 3
planning = np.zeros((14,28))  #initialization of a void planning

for i in range (14):         #number of nurses  
    
    
    daySequenceCounter = 0   #counter for know how much 1 are successives   
    nightCounter = 0           #counter for know how much 2 i can put in the week    
    nextNightIdnex = 0         #counter for know if i can put 2       
    nightIsDone = False      #boolean for know if i can put 2 or no
    workTimeLeft = 40
    j = 0
    while j<28:        # 28 days
        
        if ((j % 7)-1 == 0) and j!=1:  
            if  nightCounter == 0:
                j -= 8
                daySequenceCounter = 0
                nextNightIdnex = 0
                nightCounter = 0  
                nightIsDone = False 
                workTimeLeft = 40
                continue
                
            nightCounter = 0  
            nightIsDone = False 
            workTimeLeft = 40 


        if j == 0: 
            planning[i][0] = rd.randint(0,2)      #fist day of the month 

            
        else:  
            
            if planning[i][j-1] == 1:             
                daySequenceCounter += 1
                workTimeLeft -= 10
            else:
                daySequenceCounter = 0

            if planning[i][j-1] == 2:   
               workTimeLeft -= 14
               planning[i][j] = 0       #after a night there's a rest
               nextNightIdnex = j+3     #at least two days without rank between two nights  
                  
               
               nightCounter += 1   
               if nightCounter == 2:
                   nightIsDone = True            
            
            elif planning[i][j-1] == 1 and daySequenceCounter == 2:         
                planning[i][j] = 0         #after two dayWork, there's a dayRest
                daySequenceCounter = 0  
                
                     
            elif nextNightIdnex <= j and   nightIsDone != True and workTimeLeft >= 14:
                
                planning[i][j] = rd.randint(0,2)
                

            elif workTimeLeft >= 10 :
                planning[i][j] = rd.randint(0,1) 
                
            else:
                planning[i][j] = 0

        j += 1    
            
def hardship_min(hardship,n):
    '''
        find the least busy nurse's hardship
    '''

    hardship_min_ = hardship[0]
    for i in range(14):
        if hardship[i] < hardship_min_:
            hardship_min_ = hardship[i]
    return hardship_min_

def hardship_max(hardship,n):
    """
    find the hardest working nurse
    """
    hardship_max_ = hardship[0]
    for i in range(14):
        if hardship[i]>hardship_max_:
            hardship_max_ = hardship[i]
    return hardship_max_

'''
objective function : maximizing workload euity =minimise the hardship of the least and most loaded nurse
'''
def objective_function(planning):
    """
    calculate the workload of each nurse over the 28-day horizon through shift penalties
    """
    hardship = [0]*14
    for i in range(0,14,1):
        Nb1, Nb2 = 0, 0
        for j in range(0,5,1):
            if planning[i][j] == 1: # determine the number of "day" shifts for each nurse
                Nb1 = Nb1+1
            elif planning[i][j] == 2: # determine the number of "night" shifts for each nurse
                Nb2 = Nb2+1

        hardship[i] = Nb1*1 + Nb2*2 # Store the total penalties for each nurse in a table of dimension n
    return hardship_max(hardship, 14) - hardship_min(hardship, 14)

def main():
    
    print(planning)
    print("The value of objective function equal to :",objective_function(planning))

if __name__ == "__main__":
    main()