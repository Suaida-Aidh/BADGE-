# BST DELETE ROOT
class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if not self.key:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    def preorder(self):
        print(self.key,end=' ')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=' ')
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=' ')

    def min(self):
        curr=self
        while curr.lchild:
            curr=curr.lchild
        print('Min value of the tree is:',curr.key)
    def max(self):
        curr=self
        while curr.rchild:
            curr=curr.rchild
        print('Max value of the tree is :',curr.key)


    def delete(self,data,curr):
        if not self.key:
            print('Tree is empty!')
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data,curr)
            else:
                print('Not found in Tree!')
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data,curr)
            else:
                print('Not found in Tree!')
        else:
            if not self.lchild:
                temp=self.rchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            if not self.rchild:
                temp=self.lchild
                if data==curr:
                    self.key=temp.key
                    self.rchild=temp.rchild
                    self.lchild=temp.lchild
                    temp=None
                    return
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key,curr)

        return self
def count(root):
    if not root:
        return 0
    else:
        return 1+count(root.lchild)+count(root.rchild)
    

    
    
root=BST(None)

arr=[2,4,5,6,77,8,3,45,7]
for i in arr:
    root.insert(i)
   
root.preorder()    
print('Preorder')

if count(root)>1:
    root.delete(2,root.key)
else:
    print('cannot do this operation!')
root.preorder()    
print('Preorder')

# ____________________________________________________________________________________________________________________



#  BST SEARCH 

class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if not self.key:
            self.key=data
            return 
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    def search(self,data):
        if self.key==data:
            print('found at root!')
            return
        if self.key>data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('not found!')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('not found!')






root=BST(10)
arr=[2,3,5,6,7,8,43]

for i in arr:
    root.insert(i)

root.search(23)




# ____________________________________________________________________________________________________________________


# HEAP

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._heapify_up()

    def pop(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            min_val = self.heap.pop()
            self._heapify_down()
        elif len(self.heap) == 1:
            min_val = self.heap.pop()
        else:
            raise IndexError("pop from an empty heap")
        return min_val

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            raise IndexError("peek from an empty heap")

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Example usage:
min_heap = MinHeap()
min_heap.push(3)
min_heap.push(1)
min_heap.push(4)
min_heap.push(2)

print("Min heap:", min_heap.heap)

print("Peek:", min_heap.peek())

print("Pop:", min_heap.pop())
print("Min heap after pop:", min_heap.heap)



# ____________________________________________________________________________________________________________________

# HEAP 2

import heapq
list1=[]

heapq.heappush(list1,50)
heapq.heappush(list1,30)
heapq.heappush(list1,20)
heapq.heappush(list1,5)
heapq.heappush(list1,10)
print(list1)
heapq.heappop(list1)
heapq.heappushpop(list1,12)
print(list1)

list2=[123,24,56,76,34,2,2535,67]

heapq.heapify(list2)
print(list2)
print(heapq.nsmallest(3,list1))
print(heapq.nlargest(3,list2))

list3=[(1,'hrishi'),(7,'prasad'),(3,'hrishikesh')]
heapq.heapify(list3)
print(list3)
for i in range(len(list3)):
    print(heapq.heappop(list3))


# ____________________________________________________________________________________________________________________

# HEAP SORT 

def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)


# ____________________________________________________________________________________________________________________


# TRIE 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
trie = Trie()
words = ["apple", "app", "apricot", "banana", "bat"]

for word in words:
    trie.insert(word)

print("Search 'apple':", trie.search("apple"))  # True
print("Search 'apricot':", trie.search("apricot"))  # True
print("Search 'orange':", trie.search("orange"))  # False

print("Starts with prefix 'ap':", trie.starts_with_prefix("ap"))  # True
print("Starts with prefix 'ban':", trie.starts_with_prefix("ban"))  # True
print("Starts with prefix 'cat':", trie.starts_with_prefix("cat"))  # False


# ____________________________________________________________________________________________________________________


# TRIE INSERT

class Node:
    def __init__(self):
        self.children={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=Node()
            node=node.children[char]
        node.end=True

    def search(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.end
    
    def prefix(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return True

root=Trie()

root.insert('HRISHI')
res=root.search('HRISHI')
print(root.prefix('HR'))
print(res)


# ____________________________________________________________________________________________________________________


# VALIDATE TREE


class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def add_node(self,data):
        if not self.key :
            self.key=data

        if self.key==data:
            return
        
        if self.key>data:
            if self.lchild:
                self.lchild.add_node(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.add_node(data)
            else:
                self.rchild=BST(data)

    def validate(self):
        if not self.key:
            print('Empty Tree!')
            return False
        if self.lchild and self.lchild.key>=self.key:
            return False
        if self.rchild and self.rchild.key<=self.key:
            return False
        if self.lchild and not self.lchild.validate():
            return False
        if self.rchild and not self.rchild.validate():
            return False

        return True 

            

        
    
    

root=BST(None)
arr=[2,4,5,23,65,123,23]
for i in arr:
    root.add_node(i)

print(root.key)
res=root.validate()

if res:
    print('Tree is a BST!')
else:
    print('Tree is not a BST!')    







