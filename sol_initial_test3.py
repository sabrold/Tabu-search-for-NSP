import numpy as np
import random as rd

'''
2(a+b)+(n-(a+b)+1)/2=n --> 4(a+b)+n-(a+b)+1=2n --> 3(a+b)=n-1 --> a+b=(n-1)/3 
2(a+b): représente deux colonnes j et j-1 pour savoir combien de 1 ou 2 qu'il faut mettre ou qu'il existe
(n-(a+b)+1)/2 : pour savoir combien d'infirmiers qui ont terminé leurs 40heures à la fin de semaine

a+b=(n-1)/3 est l'estimation de combien il faut que a et b égale pour qu'on se trouve pas dans une boucle infinie, si a+b prend plus que (n-1)/3
il y'aura une chance de rentrer dans une boucle infinie même si elle trops petite

le principe de l'heursitique constructive qu'on a adapté dans ce programme : c'est que le remplissage de planning s'effectue par colonne
et chaque colonne doit vérifier les contraintes de besoin journalier avant de remplir la colonne qui suit, lorsque une colonne j est rempli,
la colonne j+1 commence à vérifier les contraintes sur les lignes 

'''

n = 16                                  #total of nurses
a = 3                                   #number of nurses needed in the "day" team
b = 2                                   #number of nurses in the "night" team
planning = np.zeros((n,28),dtype=int)    #the planning dimension          

'''
format des compteurs : vecteurs selon la longeur des lignes 
'''
nightCounter = np.zeros(n,dtype=int)                 #counter for know how much 2 i can put in the week
nextNightIdnex = np.zeros(n,dtype=int)               #counter for know if i can put 2  
nightIsDone = np.full(n, False,dtype=bool)
workTimeLeft = np.full(n,40,dtype=int)

j = 0  
'''
j<29 : pour pouvoir vérifier la dernière colonne 28
'''
while j<29:              #28 days   
    '''
    vérification des contraintes de besoin journalier
    '''
    if j!=0:
        print(planning)
        print("\n next iteration")
        numOfDays = np.count_nonzero(planning[:,j-1] == 1)
        numOfNights = np.count_nonzero(planning[:,j-1] == 2)
        if numOfDays!=a or numOfNights!=b:
            isRepeated = True
            j -= 1    
            
        else:
            isRepeated = False
            if j==28:
                j += 1
                continue

    if ((j % 7)-1==0) and j!=1:  
                
        nightCounter = np.zeros(n,dtype=int)    # counter bach na3arfo chehal derna men 2 f smana
        # nextNightIdnex=np.zeros((1,14))    # counter bach na3arfou wa9tach n9dro ndiro 2
        nightIsDone = np.full(n, False,dtype=bool)
        workTimeLeft = np.full(n,40,dtype=int) 
    ''''
    vérification des contraintes du personnel, de séquence, d'espacement et d'équilibre
    '''
    i = 0
    while i<n:        #number of nurses  
        
        if j==0: 
            planning[i][0] = rd.randint(0,2)      #first day of the month 
         
        else:  
            
            if planning[i][j-1]==1 and isRepeated==False:             
                
                workTimeLeft[i] -= 10
                
            if planning[i][j-1]==2:
                planning[i][j] = 0 
                if isRepeated==False:    
                    
                    workTimeLeft[i] -= 14              #after a night there's a rest
                    nextNightIdnex[i] = j+3             #at least two days without rank between two nights   
                  
               
                    nightCounter[i] += 1   
                    if nightCounter[i]==2:
                        nightIsDone[i] = True            
            
            elif j>=2 and planning[i][j-1]==1 and planning[i][j-2]==1:         
                planning[i][j] = 0            #after two dayWork, there's a dayRest
                                    
            elif nextNightIdnex[i]<=j and nightIsDone[i] != True and workTimeLeft[i] >= 14:
                
                planning[i][j] = rd.randint(0,2)
                
            elif workTimeLeft[i] >=10 :
                planning[i][j] = rd.randint(0,1) 
                
            else:
                planning[i][j] = 0

        i += 1    
    j += 1 

print(planning)       