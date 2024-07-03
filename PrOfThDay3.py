# -*- coding: utf-8 -*-
"""
@author: NasserAlrashdi
"""




def findAreaOfLargestRectangle(heights):
    n=len(heights)
    
    #convet the string numbers to integer
    for i in range(n):
        heights[i] = int(heights[i])

    areas=[]
    
    #nested loops to find all possible rectangles configurations
    for i in range(n):
        for j in range(n-1,-1,-1):
            if i<=j:

                currConfig=heights[i:j+1]
                width=len(currConfig)
                height=min(currConfig)
                
                #add the area of current configuration to a list of areas
                areas.append(width*height)
                
    #return tha maximum area only
    return max(areas)


##########################Test 1#############################
heights1 = [2,1,5,6,2,3]
print("heights :",heights1)
print("The area of largest rectangle =",findAreaOfLargestRectangle(heights1))
print()
##########################Test 2#############################
heights2 = [2,4]
print("heights :",heights2)
print("The area of largest rectangle =",findAreaOfLargestRectangle(heights2))
print()
##########################Test 3#############################

heights = input("Enter the heights of rectangles seperated by spaces (e.g 1 2 3 4) : ")
print("The area of largest rectangle =",findAreaOfLargestRectangle(heights.split()))