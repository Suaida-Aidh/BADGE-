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

        
# VALID PARENTHESIS
def is_balanced(s):
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses.keys():
            if stack == [] or matching_parentheses[char] != stack.pop():
                return False
    
    return stack == []

# Example usage
print(is_balanced("({[]})"))  # True
print(is_balanced("({[})"))   # False









# UPDATE

arr=[10,10,235,46,54,23,234545,576567,56232,2323,32,323,545,454556,56534,3]
def update(num,rep):
    for i in range(len(arr)):
        if arr[i]==num:
            arr[i]=rep
        
             
            


update(10,0)
print(arr)





def reverse_words_with_stack(s):
    # Step 1: Initialize an empty stack
    stack = []
    word = ''

    # Step 2: Traverse the string and push words onto the stack
    for char in s:
        if char == ' ':
            if word:  # When a space is encountered, push the current word onto the stack
                stack.append(word)
                word = ''
        else:
            word += char
    
    # Push the last word onto the stack (if any)
    if word:
        stack.append(word)
    
    # Step 3: Pop words from the stack to form the reversed string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
        if stack:  # Add a space if there are more words to pop
            reversed_string += ' '
    
    return reversed_string

# Example usage
input_string = 'MY NAME IS SUAIDA'
print(reverse_words_with_stack(input_string))  # Output: 'SUAIDA IS NAME MY'


