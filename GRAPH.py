def add_node(v):
    if v in graph:
        print(v,'is already inside the graph!')
    else:
        graph[v]=[]

def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,'node not found in graph!')
    elif v2 not in graph:
        print(v2,'node not found in graph!')
    else:
        # list1=[v1,cost]  #When INSERT IN AL ALSO THE COST
        # list2=[v2,cost]
        # graph[v1].append(list2)
        # graph[v2].append(list1)
        # ---------------------------
        graph[v1].append(v2)
        graph[v2].append(v1)



def DFS(node,visited,graph):
    if node not in graph:
        print('node not found in graph!')
        return
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)

visited=set()
graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_edge('A','B')
add_edge('A','C')
add_edge('D','C')
add_edge('B','C')
print(graph)
DFS('A',visited,graph)
# __________________________________________________________________________________________

# INSERT AM

def add_node(v):
    global nodes_count
    if v in nodes:
        print('Already in the graph')
    else:
        nodes_count+=1
        nodes.append(v)
        for n in graph:
            n.append(0) 
        temp=[]
        for i in range(len(nodes)):
            temp.append(0)
        graph.append(temp)

def print_AM():
    for i in range(nodes_count):
        for j in range(nodes_count):
            print(graph[i][j],end=' ')
        print()

def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,'is not found in nodes')
    elif v2 not in nodes:
        print(v2,'is not found in nodes')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost



nodes=[]
graph=[]
nodes_count=0



add_node('A')
add_node('B')
add_node('C')


print(nodes_count)
print(nodes)
add_edge('A','C',3)
add_edge('B','C',3)
add_edge('A','B',3)
print_AM()

# __________________________________________________________________________________________
# BFS DFS RECURSION

from collections import deque


def add_node(v):
    if v in graph:
        print(v ,'is already in graph')
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'not found in graph!')        
    elif v2 not in graph:
        print(v2,'not found in graph!')
    else:
        # list1=[v1,cost]
        # list2=[v2,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)

def DFS(node,visited,graph):
    if node not in graph:
        print('Node not found in graph!')
        return
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
        for i in graph:
            if i not in visited:
                print(i,end=' ')
                visited.add(i)

def BFS(node,graph):
    if node not in graph:
        print('node not found!')
        return
    visit=set()
    arr=deque([node])
    while arr:
        vertex=arr.popleft()
        visit.add(vertex)
        print(vertex,end=' ')
        for i in graph[vertex]:
            if i not in visit:
                arr.append(i)
    
    for i in graph:
        if i not in visit:
            print(i,end=' ')
            visit.add(i)


    

visited=set()
graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge('A','B')
add_edge('A','C')
add_edge('C','B')
# add_edge('E','B')
# add_edge('D','B')
print('DFS:',end=' ')
DFS('A',visited,graph)
print()
print('BFS:',end=' ')
BFS('A',graph)
print()
# print(graph)
# __________________________________________________________________________________________



# DELETE AL

def add_node(v):
    if v in graph:
        print(v ,'is already in graph')
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'not found in graph!')        
    elif v2 not in graph:
        print(v2,'not found in graph!')
    else:
        # list1=[v1,cost]
        # list2=[v2,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)

def delete_node(v):
    if v not in graph:
        print('not found')
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)

def delete_edge(v1,v2):
    if v1 not in graph:
        print('not found!')
    elif v2 not in graph:
        print('not found!')
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)




graph={}
add_node('A')
add_node('B')
add_node('C')

add_edge('A','B')
add_edge('C','B')
add_edge('A','C')
print(graph)
delete_edge('A','B')
print(graph)
# __________________________________________________________________________________________

# DELETE AM

def add_node(v):
    global nodes_count
    if v in nodes:
        print('Already in the graph')
    else:
        nodes_count+=1
        nodes.append(v)
        for n in graph:
            n.append(0) 
        temp=[]
        for i in range(len(nodes)):
            temp.append(0)
        graph.append(temp)

def print_AM():
    for i in range(nodes_count):
        for j in range(nodes_count):
            print(graph[i][j],end=' ')
        print()

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,'is not found in nodes')
    elif v2 not in nodes:
        print(v2,'is not found in nodes')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1

def delete_node(v):
    global nodes_count
    if v not in nodes:
        print(v,'is not found in graph')
    else:
        index1=nodes.index(v)
        nodes_count-=1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print('not found!')
    elif v2 not in nodes:
        print('not found!')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        # graph[index2][index1]=0




nodes=[]
graph=[]
nodes_count=0



add_node('A')
add_node('B')
add_node('C')


print(nodes_count)
print(nodes)
add_edge('A','C')
add_edge('B','C')
add_edge('A','B')

print_AM()
delete_edge('A','C')
delete_edge('A','B')
delete_edge('C','B')
print()
print_AM()

# __________________________________________________________________________________________

# DFS ITERATIVE

def add_node(v):
    if v in graph:
        print(v ,'is already in graph')
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'not found in graph!')        
    elif v2 not in graph:
        print(v2,'not found in graph!')
    else:
        # list1=[v1,cost]
        # list2=[v2,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)

def DFSiterative(node,graph):
    visited=set()
    if node not in graph:
        print('node not in graph!')
        return
    stack=[]
    stack.append(node)
    while stack:
        curr= stack.pop()
        if curr not in visited:
            print(curr,end=' ')
            visited.add(curr)
            for i in graph[curr]:
                stack.append(i)
    for i in graph:
        if i not in visited:
            print(i,end=' ')
            visited.add(i)








graph={}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge('A','B')
add_edge('C','B')
add_edge('A','C')
print(graph)
DFSiterative('B',graph)


# print(graph)

# __________________________________________________________________________________________
# __________________________________________________________________________________________
# __________________________________________________________________________________________
# __________________________________________________________________________________________
