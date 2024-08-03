# # BUBBLE
def sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[10,24,65,33,65,22,12,3232,3545346,56756867867,343,1]      
sort(arr)
print(arr)          
                

def sort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[90,20,30,45,66,78,12]
ar=sort(arr)
print(arr)



# BUBBLE IN LINKES list
class Node:
    def __init__ (self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def bubble(self):
        if not self.head or not self.head.ref:
            return self.head
        bsort=False
        while not bsort:
            bsort =True
            curr=self.head
            while curr.ref:
                if curr.data>curr.ref.data:
                    curr.data,curr.ref.data=curr.ref.data,curr.data
                    bsort=False
                curr=curr.ref
        return self.head

    def printLL(self):
        n=self.head
        while n:
            print(n.data,'-->',end='')
            n=n.ref





# ____________________________________________________________________________________________________________________


# INSERTION 
def sort(arr):
    n=len(arr)

    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

arr=[10,24,65,33,65,22,12,3232,3545346,56756867867,343,1]      
sort(arr)
print(arr)   

# INSERTION IN LINKED LIST 

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head= None

    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.ref=self.head
            self.head=new_node
    def printLL(self):
        n=self.head
        while n is not None:
            print(n.data,'-->',end='')
            n=n.ref
    def sort(self):
        prev=None
        n=self.head 
# ____________________________________________________________________________________________________________________

# MERGE
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2

        left=arr[:mid]
        right=arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(arr,left,right)

def merge(arr,left,right):
    i=j=k=0

    while len(left)>i and len(right)>j:
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

arr=[5,6,7,3,2,8,23,4]

merge_sort(arr)
print(arr)

# MERGE IN LINKED list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mid(head):
    slow=head
    fast=head.next

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    return slow

def merge(head):
    if not head or not head.next:
        return head
    
    left=head
    right=mid(head)
    temp=right.next
    right.next=None
    right=temp

    left=merge(left)
    right=merge(right)

    return sort(left,right)

def sort(left,right):
    tail=dummy=Node(0)

    while left and right:
        if left.data<right.data:
            tail.next=left
            left=left.next
        else:
            tail.next=right
            right=right.next
        tail=tail.next
    
    while left:
        tail.next=left
    while right:
        tail.next=right

def printLL(head):
    while head:
        print(head.data,end=' ')        
        head=head.next

head = Node(3)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(2)
head.next.next.next.next = Node(2)

printLL(head)
merge(head)
printLL(head)



# ____________________________________________________________________________________________________________________


# QUICK

def sort(arr):
    n=len(arr)

    if n<=1:
        return arr
    else:
        pivot=arr[0]
        less=[x for x in arr[1:] if x<=pivot]
        larg=[x for x in arr[1:] if x>pivot]
        return sort(less)+[pivot]+sort(larg)
    
arr=[9,8,4,5,10,17,21,6]
ass=sort(arr)
print(ass)



# QUICK IN LINKED LIST 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(start, end):
    pivot_value = start.data
    pivot = start
    current = start.next

    while current :
        if current.data < pivot_value:
            pivot = pivot.next
            current.data, pivot.data = pivot.data, current.data
        current = current.next

    start.data, pivot.data = pivot.data, start.data
    return pivot

def quicksort(start, end=None):
    if start and start != end:
        pivot = partition(start, end)
        quicksort(start, pivot)
        quicksort(pivot.next, end)

def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Example usage:
# Create a linked list
head = Node(3)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(2)
head.next.next.next.next = Node(2)

# Find the end of the linked list
end = head
while end.next:
    end = end.next

print("Original Linked List:")
print_list(head)

# Call quicksort with the correct end parameter
quicksort(head, end)

print("Sorted Linked List:")
print_list(head)


# ____________________________________________________________________________________________________________________


# SELECTION

def sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

arr=[10,90,23,54,12,34,66]
sort(arr)
print(arr)

# SELCTION IN LINEDK list
class Node:
    def __init__ (self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def printLL(self):
        n = self.head
        while n:
            print(n.data, '-->', end='')
            n = n.ref
    
    def selectionsort(self):
        if not self.head or not self.head.ref:
            return self.head

        curr = self.head
        while curr:
            min_node = self.find_min()  # Removed curr argument here
            self.swap(curr, min_node)
            curr = curr.ref
    
    def find_min(self):
        min_node = self.head
        curr = self.head.ref

        while curr:
            if curr.data < min_node.data:
                min_node = curr
            curr = curr.ref
        return min_node
    
    def swap(self, node1, node2):
        temp = node1.data
        node1.data = node2.data
        node2.data = temp

# Example usage:
if __name__ == "__main__":
    LL = LinkedList()
    LL.push(11)                    
    LL.push(12)                    
    LL.push(13)                    
    LL.push(14)                    
    LL.push(15)                    
    LL.push(16)
    LL.selectionsort()
    LL.printLL()


# ____________________________________________________________________________________________________________________
