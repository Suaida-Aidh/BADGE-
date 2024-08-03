# DD LINKED LIST 
class Node:
    def __init__(self,data):
        self.data= data
        self.nref= None
        self.pref=None


class DoubleLL:
    def __init__(self):
        self.head=None

    def printDLL(self):
        if self.head is None:
            print('ll is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,end=' ')
                n=n.nref


    def printDLL_reverse(self):
        print()
        if self.head is None:
            print('ll is empty')
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,end=' ')
                n=n.pref

    def insert(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('linked list is not empty')

    def insert_begin(self,data):
        n=self.head
        new_node=Node(data)
        if self.head is None:
            self.head= new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node

    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref

            n.nref=new_node
            new_node.pref=n

    def add_after(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print('ll is empty')
            return
        else:
            n=self.head
            while n is not None:
                if n.data == x:
                    break
                n=n.nref

            if n is  None:
                print('node not found after ')
            else:
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node

    def add_before(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print('it empty!!')
            return
        
        if self.head.data == x:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head = new_node
            return
        
        n=self.head
        while n.nref is not None:
            if n.nref.data == x:
                break
            n=n.nref


        if n.nref is None:
            print('not found before element')
        else:
            new_node.nref=n.nref
            new_node.pref=n
            n.nref.pref=new_node
            n.nref=new_node
        
                

DLL=DoubleLL()
# DLL.insert(10)
# DLL.insert_begin(100)
# DLL.insert_end(20)
# DLL.insert_end(150)
# DLL.add_after(55,10)


DLL.insert_end(100)
DLL.insert_end(200)
DLL.insert_end(300)
DLL.insert_end(400)
DLL.insert_end(500)
DLL.add_before(00, 500)
DLL.add_before(11111, 100)

DLL.add_after('after', 500)
# DLL.add_after('after', 0)





DLL.printDLL()
DLL.printDLL_reverse()

# _________________________________________________________________________________________________________________________________

# SINGLE LINKED LIST 

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


class LinkedList:
    def __init__(self):
        self.head=None

    def printLL(self):
        if self.head is None:
            print('LL is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,end=' ')
                n=n.ref

    def reverse(self):
        if self.head is None:
            print('ll is empty')
            return
        
        if self.head.ref is None:
            print('already reverse format')
            return
        
        prev= None
        
        curr= self.head

        while curr is  not None:
            next = curr.ref
            curr.ref = prev
            prev=curr
            curr=next

        self.head= prev

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n.ref is not None:
            if x == n.data:
                break
            n=n.ref

        if n.ref is None:
            print('Data link not found in the list')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print('list is empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref=self.head
            self.head = new_node
            return
        
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n=n.ref

        if n is None:
            print('not found!')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node


    def delete_begin(self):
        if self.head is None:
            print('ll is empty in delete begin')
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print('ll empty in delete end')
            return
        elif self.head.ref is None:
            self.head = None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None


    def delete_middle(self,x):
        if self.head is None:
            print('empty')
            return
        if self.head.data == x:
            self.head=self.head.ref
            return
        
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n=n.ref

        if n.ref is None:
            print('node not found')
        else:
            n.ref = n.ref.ref

    def middle(self):       #FIND MIDDLE ELEMENT
        if self.head is None:
            print('empty list!')
            return
        s=self.head
        f=self.head.ref
        while f is not None and f.ref is not None:
            f=f.ref.ref
            s=s.ref
        print('middle value of the Linked List is :',s.data)


    def length(self):
        length=0
        if self.head is None:
            print('Empty list!!')
        else:
            n=self.head
            while n is not None:
                length+=1
                n=n.ref
            print('Length of the linked list is',length)

    def sort(self):
        if self.head is None:
            print('ll is empty in sort')
            return
        else:
            i=self.head
            while i.ref is not None:
                j=i.ref
                while j is not None:
                    if i.data > j.data:
                        i.data , j.data = j.data, i.data
                    j=j.ref
                i=i.ref
    
    def duplicates(self):
        if self.head is None:
            print('empty!')
            return
        else:
            n=self.head
            while n.ref is not None:
                if n.data == n.ref.data:
                    n.ref=n.ref.ref
                    continue
                n=n.ref



ll1 = LinkedList()
ll1.add_begin(13)
ll1.add_begin(14)
ll1.add_end(1000)
ll1.add_end(10)
ll1.add_begin(15)
ll1.add_begin(16)
ll1.add_after(110,10)
ll1.printLL()

# _________________________________________________________________________________________________________________________________



class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head2=None
        self.head1=None

    def add_begin(self,data1,data2):
        new_node1=Node(data1)
        new_node2=Node(data2)
        new_node1.ref=self.head1
        self.head1=new_node1
        new_node2.ref=self.head2
        self.head2=new_node2
    def merge(self):
        n1=self.head1
        n2=self.head2
        while n1.ref is not None:
            n1=n1.ref
        n1.ref=n2    

    def printLL(self):
        n1=self.head1
        n2=self.head2
        
        while n1 is not None:
            print(n1.data,'-->',end="")
            n1=n1.ref
        print()
        # while n2 is not None:
        #     print(n2.data,end=' -> ')
        #     n2=n2.ref

        print()    
       



LL=LinkedList()
LL.add_begin(10,12)
LL.add_begin(14,16)
LL.add_begin(15,18)
LL.add_begin(17,11)
LL.add_begin(19,10)
LL.add_begin(23,13)
LL.merge()
LL.printLL()




        