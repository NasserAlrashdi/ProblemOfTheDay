# -*- coding: utf-8 -*-
"""
@author: NasserAlrashdi
"""




"""
function to rotate the matrix clock wise by creating new rows and add the
correct elemnts to them (e.g. first row contain first elemnts from the
rows in decreasing order (3,2,1,..), second row contain second elemnts from... and so on.)
"""
def rotateMatrix(matrix,n):
    #create empty matrix
    newMatrix=[]
    #loop for number of rows
    for i in range(n):
        #create new roe
        newRow = []
        #loop from last row until first row (n-1,n-2,...,1) 
        for j in range(n-1,-1,-1):
            #add the element [j][i] from the matrix to the row
            newRow.append(int(matrix[j][i]))
        #add the new row to the matrix
        newMatrix.append(newRow)
    
    return newMatrix    

##########################Test 1#############################
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
n1 = 3
print("Test 1")
print(rotateMatrix(matrix1, n1))
print()
##########################Test 2#############################
matrix2 = [[5,1,9,11],[2,4,8,18],[13,3,6,7],[15,14,12,16]]
n2 = 4
print("Test 2")
print(rotateMatrix(matrix2, n2))
print()
##########################Test 3#############################
print("Test 3")
n0 = int(input("Enter the n value: "))
matrix0=[]
for i in range(n0):
    row = input(f"Enter {n0} values for the row number {i+1} (seperated by spaces, like 1 2 3): ")
    matrix0.append(row.split())
print(rotateMatrix(matrix0, n0))