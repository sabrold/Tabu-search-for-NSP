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

def main():
    n = 3
    original_schedule=[[1,1,0,2,0],[0,1,2,0,0],[2,0,0,1,1]]
    print(fitness(original_schedule,n))

if __name__ == "__main__":
    main()