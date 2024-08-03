# CD 
arr=[12,32,43,54,23,2,121,21,1,32,4]
list1=[]
for i in range(len(arr)):
    list1.append(arr[i])
    print(list1)

print()
print()
for i in range(len(list1)):
    list1.pop(0) 
    print(list1)


arr=[12,23,45,65,43,34,56,3,2,2,43]
def update(num,replace):
    for i in range(len(arr)):
        if arr[i]==num:
            arr[i]=replace
            num=None
update(43,0)
print(arr)            



# _______________________________________________________________________________


# IN LINKED LIST 

class Node:
    def __init__(self,data) :
        self.data=data
        self.ref=None

class QueueList:
    def __init__(self) :
        self.front= None
        self.rear=None

    def enqueue(self,data):
        new_node= Node(data)
        if self.is_empty():
            self.front=self.rear=new_node
        else:
            self.rear.ref=new_node
            self.rear=new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            dq_data=self.front.data
            self.front=self.front.ref
            if self.front is None:
                self.rear= None
            return dq_data
    def front(self):
        return self.front.data if self.front else None
    
    def is_empty(self):
        return self.front is None
    
    def printLL(self):
        n=self.front
       
        while n:
            print(n.data,'-->',end='')
            n=n.ref


LL=QueueList()
LL.enqueue(12)
LL.enqueue(13)
LL.enqueue(14)
LL.enqueue(15)
LL.enqueue(16)
LL.dequeue()
LL.dequeue()
LL.dequeue()
LL.dequeue()
LL.dequeue()
      
     
LL.printLL()


# _______________________________________________________________________________


