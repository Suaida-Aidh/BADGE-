# COLLECTT

from collections import deque
list1=[10, 23, 235, 46, 54, 23, 3]
arr=deque()

for i in list1:
    arr.append(i)
# arr.sort()
print(arr)


# CRUD

arr=[10,23,45,65,2,3,54,6,87,8,96]

list1=[]

for i in range(len(arr)):
    list1.append(arr[i])
    print(list1)

for j in range(len(list1)):
    list1.pop()
    print(list1)
   


# LINKED list

class Node:
    def __init__(self,data):
        self.data=data
        self.ref= None

class LinkedList:
    def __init__(self):
        self.Top=None

    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.Top
        self.Top=new_node

    def pop(self):
        if self.Top is None:
            return None
        popdata=self.Top.data
        self.Top=self.Top.ref
        return popdata
    
    def peek(self):
        if self.Top:
            print(self.Top.data)
            return
        else:
            print('empty!!!!')
            return
    
    def is_empty(self):
        return self.Top.data is None
    
    def print(self):
        if self.Top is None:
            print('EMPTY LIST!!')
            return
        else:
            n=self.Top
            while n:
                print(n.data,'-->',end='')
                n=n.ref

    


LL=LinkedList()
LL.push(15)
LL.push(16)
LL.push(17)
LL.push(18)
LL.push(19)
LL.push(20)
LL.pop()
LL.is_empty()
LL.peek()
LL.print()

        






# UPDATE

arr=[10,10,235,46,54,23,234545,576567,56232,2323,32,323,545,454556,56534,3]
def update(num,rep):
    for i in range(len(arr)):
        if arr[i]==num:
            arr[i]=rep
        
             
            


update(10,0)
print(arr)


