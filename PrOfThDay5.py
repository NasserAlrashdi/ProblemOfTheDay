# -*- coding: utf-8 -*-
"""
@author: NasserAlrashdi
"""

class LinkedList:
    
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def addValue(self, newValue):
        newNode = LinkedList(newValue)
        currentNode = self
        if currentNode.value == None:
            currentNode.value=newValue
        else:
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
    
def sumAsLinkedList(integer1,integer2):
    
    result=LinkedList()
    
    while integer1 and integer2:
        r=integer1.value+integer2.value
        result.addValue(r%10)
        if r>9:
            if integer1.next:
                integer1.next.value=integer1.next.value+(r//10)
            elif integer2.next:
                integer2.next.value=integer2.next.value+(r//10)
            else:
                result.addValue(r//10)
                
        integer2=integer2.next
        integer1=integer1.next
        
    while integer1:
        if integer1.value >9:
            result.addValue(integer1.value%10)
            if integer1.next:
                integer1.next.value+=integer1.value//10
            else:
                integer1.addValue(integer1.value//10)   
        else:
            result.addValue(integer1.value)
        integer1=integer1.next
        
    while integer2:
        if integer2.value >9:
            result.addValue(integer2.value%10)
            if integer2.next:
                integer2.next.value+=integer2.value//10
            else:
                integer2.addValue(integer2.value//10)   
        else:
            result.addValue(integer1.value)
        integer2=integer2.next
        
    return result


#####################################TEST 1####################################
input1=[9,9,9,9,9,9,9]
input2=[9,9,9,9]

integer1 = LinkedList()
for i in input1:
    integer1.addValue(int(i))

integer2 = LinkedList()
for i in input2:
    integer2.addValue(int(i))

    
result = sumAsLinkedList(integer1, integer2)

output=[]
while result:
    output.append(result.value)
    result=result.next
print("Test 1\nFirst Integer : ",input1)
print("Second Integer : ",input2)
print("Output : ",output)
#####################################TEST 2####################################

input1=[2,4,3]
input2=[5,6,4]

integer1 = LinkedList()
for i in input1:
    integer1.addValue(int(i))

integer2 = LinkedList()
for i in input2:
    integer2.addValue(int(i))

    
result = sumAsLinkedList(integer1, integer2)

output=[]
while result:
    output.append(result.value)
    result=result.next

print("\nTest 2\nFirst Integer : ",input1)
print("Second Integer : ",input2)
print("Output : ",output)
print("\nTest 3")
#####################################TEST 3####################################

input1 = input("Enter positive integer in reverse order like 3 2 1 for 123 : ").split()
input2 = input("Enter another positive integer in reverse order like 3 2 1 for 123 : ").split()

integer1 = LinkedList()
for i in input1:
    integer1.addValue(int(i))

integer2 = LinkedList()
for i in input2:
    integer2.addValue(int(i))

    
result = sumAsLinkedList(integer1, integer2)

output=[]
while result:
    output.append(result.value)
    result=result.next

print("\nTest 3\nFirst Integer : ",input1)
print("Second Integer : ",input2)
print("Output : ",output)


