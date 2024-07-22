# -*- coding: utf-8 -*-
"""
@author: NasserAlrashdi
"""


class Building:
    
    def __init__(self, left=None, right=None, height=None):
        self.height = height
        self.left = left
        self.right = right
        self.next = None
        self.prev = None
        
    def add_next(self, building):
        self.next = building
        building.prev = self
    

def sizeOfBuilding(buildings):
    i = 0
    output = []
    
    while i < len(buildings):
        current = buildings[i]
        if i == 0:
            output.append([current.left, current.height])
        elif i == len(buildings)-1:
            output.append([current.right, 0])
            
        elif i < len(buildings) - 1:
            next_building = buildings[i+1]
            
            if current.height != next_building.height:
                
                if current.right>=next_building.left :
                    output.append([current.left, current.height])
                    output.append([current.right, next_building.height])
                
                else:
                    output.append([current.right, 0])          
        i+=1         
    return output

def createBuildingsObjects(dimensionsList):
    buildingsObjects=[]
    for l,r,h in dimensionsList:           
        buildingsObjects.append(Building(l, r, h))
    for i in range(len(dimensionsList)-1):
        buildingsObjects[i].add_next(buildingsObjects[i+1])
    return buildingsObjects
    
################################Test 1#################################
builds=[[2, 9, 10],[3, 7, 15],[5, 12, 12],[15, 20, 10],[19, 24, 8]]
objects=createBuildingsObjects(builds)
print("Test 1\nInput:",builds)
print("Output:",sizeOfBuilding(objects))
################################Test 2#################################
builds=[[0,2,3],[2,5,3]]
objects=createBuildingsObjects(builds)
print("\nTest 2\nInput:",builds)
print("Output:",sizeOfBuilding(objects))
################################Test 3#################################
builds=[[1,5,7],[4,8,10],[8,10,15],[9,15,9]]
objects=createBuildingsObjects(builds)
print("\nTest 3\nInput:",builds)
print("Output:",sizeOfBuilding(objects))




