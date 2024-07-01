# -*- coding: utf-8 -*-
"""
@author: NasserAlrashdi
"""


"""Function that find the hight of the triangle given the color of starting
ball , number of black balls , number of white balls """
def findTriangleHight(startingColor,black,white):
    
    #initalize hight
    hight = 0
    ##initalize level
    lvl=1
    
    #initalize the turns
    if startingColor == 'black' :
        firstTurnBalls = black
        secondTurnBalls = white
    else:
        firstTurnBalls = white
        secondTurnBalls = black
        
        
    #loop until no more rows of balls can be added
    while True :
        
        #check if there is enough balls in first turn for this level 
        if firstTurnBalls-lvl >= 0:
            #update the number of balls for this turn
            firstTurnBalls-=lvl
            #increment the hight
            hight+=1
            
            #increment the level
            lvl +=1 
            
            #check if there is enough balls in second turn for this level 
            if secondTurnBalls-lvl >= 0:
                #update the number of balls for this turn
                secondTurnBalls-=lvl
                #increment the hight
                hight+=1
                
                #increment the level
                lvl+=1
            #return the hight if there is no enough balls
            else: return hight
        #return the hight if there is no enough balls
        else : return hight


#############################TEST#############################

while True:

    black = int(input("Enter the number of black balls: "))
    white = int(input("Enter the number of white balls: "))

    if black + white < 1 :
        print("Error!! Try another input.")
    else: break
    
#print the maximum hight between the hights of the two triangles
print("\nThe maximum hight of the traingle : ",max(findTriangleHight("white",black,white),findTriangleHight("black",black,white)))