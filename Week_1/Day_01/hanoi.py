#Towers of Hanoi game

#Wikipedia:
# "The objective of the puzzle is to move the entire stack to another
# rod, obeying the following simple rules:
# "1. Only one disk can be moved at a time.
# "2. Each move consists of taking the upper disk from one of the stacks
# and placing it on top of another stack i.e. a disk can only be moved if
# it is the uppermost disk on a stack.
# "3. No disk may be placed on top of a smaller disk."

#Rods labeled R_1,...,R_m.
#Disks labeled D_1,...D_n.
#Each rod has slots S_1,...,S_n for disks.

#Winning condition: all slots occupied on non-starting rod.

#Operation User Can Perform: move disk D_k from slot (R_i, S_k) to slot
# (R_j, S_k)
#Restriction: (R_i,S_K) and (R_j,S_K) must be unoccupied for K < k. 

#Rule 1 is satisfied by definition of Operation User Can Perform.
#Rule 2 is satisfied by Restriction.
#Rule 3 is satisfied by having designated slots on each rod for each
# disk.

#Game setup:
#Prompt: "Enter number of rods." 
#Prompt: "Enter number of disks."
#Prompt: "Enter starting rod."

#Game status:
#List of occupied slots.
#Display: "Rod i: [list slot numbers]"

#Game play:
#Prompt: "Choose a rod to move disk from."
#Prompt: "Choose a rod to move disk to."

import listoperations

number_of_rods = int(raw_input("Enter number of rods.\n"))
number_of_disks = int(raw_input("Enter number of disks. \n"))
starting_rod = int(raw_input("Enter starting rod.\n")) - 1

#Inital setup:
rods = []
for i in range(number_of_rods):
    rods.append([])
    for k in range(number_of_disks):
        if i == starting_rod:
            rods[i].append(1)
        else:
            rods[i].append(0)
            
#result of removing starting rod from rod list            
other_rods = listoperations.removeitemindex(starting_rod, rods) 



            
def off_of_starting_rod():
   #Tests whether disks have been removed from starting rod.
    status = True
    for k in range(number_of_disks):
        if rods[starting_rod][k] == 1:
            status = False
            break            
        else:
            continue
    return status
    
    
def winning_condition():    
    if off_of_starting_rod() == True:             
        for i in range(len(other_rods)):       
            status = True
            current_candidate = other_rods[i]
            other_other_rods = listoperations.removeitemindex(
                i, other_rods
            )            
            for k in range(number_of_disks):
                
                if current_candidate[k] == 0:
                    
                    status = False                        
            if status == True:
                
                for j in range(len(other_other_rods)):
                    
                    for k in range(number_of_disks):
                        
                        if other_other_rods[j][k] == 1:
                            #
                            status = False
                            break
                            break 
                break
        
        return status
                       
     
          
    else:             
        return False  
               
        
            
while winning_condition() == False:       
    for i in range(len(rods)):
        j = i+1
        print "Rod %s :" %j + " " + str(
            [k+1 for k in range(number_of_disks) if rods[i][k] == 1]
            )
    origin_rod = int(raw_input("Choose a rod to move disk from. \n")) - 1   
    topdisk = None
    for K in range(number_of_disks):
        if rods[origin_rod][K] == 1:
            topdisk = K
            break
    if topdisk == None:
        print "Sorry, no disks on that rod."        
    else:        
        destination_rod = int(
            raw_input("Choose a rod to move disk to. \n")
            ) - 1
        eligible = True
        for K in [K for K in range(number_of_disks) if K < topdisk]:
            if rods[destination_rod][K] == 1:
                eligible = False
                print "Sorry, no disk can be placed on top of a \
smaller disk."
                break
            else:
                continue
        if eligible == True:
            rods[origin_rod][topdisk] = 0
            rods[destination_rod][topdisk] = 1 
            
print "Congratulations, you've won!"







