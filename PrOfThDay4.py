# -*- coding: utf-8 -*-
"""
@author: NasserAlrashdi
"""


def pathCrossItSelf(distances):
    
    #save all visited points in list
    visited = [(0,0)]
    n=len(distances)-1
    ndx=0
    current=(0,0)
    
    #loop for all distances
    while ndx <= n:
        
        #go up
        for i in range(distances[ndx]):
            current=(current[0],current[1]+1)
            if current in visited and ndx != 0: return True
            visited.append(current)
        ndx+=1
        if ndx > n : break
        
        #go left
        for i in range(distances[ndx]):
            current=(current[0]-1,current[1])
            if current in visited : return True
            visited.append(current)
        ndx+=1
        if ndx > n : break
    
        #go down
        for i in range(distances[ndx]):
            current=(current[0],current[1]-1)
            if current in visited : return True
            visited.append(current)
        ndx+=1
        if ndx > n : break
    
        #go right
        for i in range(distances[ndx]):
            current=(current[0]+1,current[1])
            if current in visited : return True
            visited.append(current)
        ndx+=1
        if ndx > n : break
    
    return False
    

##########################Test 1#############################
distances = [2,1,1,2]
print("Distances:",distances)
print("Output :",pathCrossItSelf(distances))
print()
##########################Test 2#############################
distances = [1,2,3,4]
print("Distances:",distances)
print("Output :",pathCrossItSelf(distances))
print()
##########################Test 3#############################
distances = [1,1,1,2,1]
print("Distances:",distances)
print("Output :",pathCrossItSelf(distances))
print()
##########################Test 4#############################
distances = input("Enter the distances seperated by spaces (e.g 1 2 3 4) : ")
distances=distances.split()
#convert the string numbers to integer
for i in range(len(distances)):
    distances[i] = int(distances[i])
    
print("Distances:",distances)
print("Output :",pathCrossItSelf(distances))
print()

