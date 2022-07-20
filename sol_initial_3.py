import numpy as np
import random as rd
#initialization
A = 4 #number of nurses needed in the "day" team
B = 2 #number of nurses in the "night" team, which must be greater than or equal to half of A
nb = B
n = B*7 #total of nurses
original_schedule = np.zeros((n,28)) #the planning dimension

'''the principle of  : '''
for i in range (nb): #line
   v = 0
   for j in range(4): #column
       original_schedule[i][0+v] = 2
       original_schedule[i][2+v] = 1            
       v += 7
   
for i in range (nb,nb+B):
   v = 0
   for j in range(4):
       original_schedule[i][1+v] = 2
       original_schedule[i][3+v] = 1
       v += 7
nb += B

for i in range (nb,nb+B):
   v = 0
   for j in range(4):    
       original_schedule[i][2+v] = 2
       original_schedule[i][4+v] = 1
       v += 7
nb += B 

for i in range (nb,nb+B):
   v = 0
   for j in range(4):     
       original_schedule[i][3+v] = 2
       original_schedule[i][5+v] = 1       
       v += 7
nb += B 

for i in range (nb,nb+B):
   v = 0
   for j in range(4):     
       original_schedule[i][4+v] = 2
       original_schedule[i][6+v] = 1
       v += 7
nb += B 


for i in range (nb,nb+B):
   v = 0
   for j in range(4):     
       original_schedule[i][5+v] = 2
       original_schedule[i][0+v] = 1
       v += 7
nb += B 

for i in range (nb,nb+B):
   v = 0
   for j in range(4):     
       original_schedule[i][6+v] = 2
       original_schedule[i][1+v] = 1
       v += 7


nb = B
diff = A-B

for i in range (diff):
   v = 0
   for j in range(4):
       original_schedule[i][6+v] = 1       
       v += 7
   
for i in range (diff):
   v = 0
   for j in range(4):
       original_schedule[nb+i][0+v] = 1
       v += 7
nb += B 

for i in range (diff):
   v = 0
   for j in range(4):    
       original_schedule[nb+i][1+v] = 1
       v += 7
nb += B 

for i in range (diff):
   v = 0
   for j in range(4):     
       original_schedule[nb+i][2+v] = 1       
       v += 7
nb += B 

for i in range (diff):
   v = 0
   for j in range(4):     
       original_schedule[nb+i][3+v] = 1
       v += 7
nb += B 

for i in range (diff):
   v = 0
   for j in range(4):     
       original_schedule[nb+i][4+v] = 1
       v += 7
nb += B 


for i in range (diff):
   v = 0
   for j in range(4):     
       original_schedule[nb+i][5+v] = 1
       v += 7
nb += B 
#calculate the workload of each nurse over the 28-day horizon through shift penalties
hardship = [0]*n
for i in range(0,n,1):
    Nb0 = 0
    Nb1 = 0
    Nb2 = 0
    for j in range(0,28,1):
        if original_schedule[i][j]==0: #determine the number of days off for each nurse over the same horizon
            Nb0 = Nb0+1
        elif original_schedule[i][j]==1: #determine the number of "day" shifts for each nurse
            Nb1 = Nb1+1
        elif original_schedule[i][j]==2: #determine the number of "night" shifts for each nurse
            Nb2 = Nb2+1
    hardship[i] = Nb0*0 + Nb1*1 + Nb2*2 #Store the total penalties for each nurse in a table of dimension n

#find the least busy nurse's hardship
def hardship_min(hardship):
    hardship_min = hardship[0]
    for i in range(n):
        if hardship[i]<hardship_min:
            hardship = hardship[i]
    return hardship_min
#find the hardest working nurse
def hardship_max(hardship):
    hardship_max = hardship[0]
    for i in range(n):
        if hardship[i]>hardship_max:
            hardship_max = hardship[i]
    return hardship_max

ValueObjectufFunction = hardship_max(hardship)-hardship_min(hardship)

print(original_schedule)
print("La valeur de la fonction objectif relié à cette solution est : ",ValueObjectufFunction)

        




