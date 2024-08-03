# BINARY SEARCH 1

arr=[21,34,23,76,87,11,32,43]
arr.sort()
print(arr)
n=76
pos =-1
def binarySearch(arr,n):
    low=0
    up=len(arr)-1

    while low<=up:
        mid=low+(up-low)//2
        if arr[mid]==n:
            globals() ['pos']=mid
            return True
        else:
            if arr[mid]<n:
                low=mid
            else:
                up=mid
    return False

if binarySearch(arr,n):
    print('found at ', pos+1)
else:
    print('Not Found!')

# _________________________________________________________________________________________________________________________________

# BINARY SEARCH 2

arr=[1,2,3,4,5,6,7,8,9]
n=23
k=7
def search(arr,n,k):
    low=0
    up=len(arr)-1
    while low<=up:
        mid=low+(up-low)//2

        if arr[mid]==n:
            arr[mid]=k
            print(arr)
            return
        else:
            if mid<n:
                low=mid
            else:
                up=mid
    return 

search(arr,n,k)            


# _________________________________________________________________________________________________________________________________


# BS RECURSION 

def search(arr,target,low=None,high=None):
    if low is None and high is None:
        low,high=0,len(arr)-1

    mid=low+ (high - low) //2
    if target==arr[mid]:
        return mid+1
    elif target<arr[mid]:
        return search(arr,target,low,mid-1)
    else:
        return search(arr,target,mid+1,high)

arr = [1, 2, 3, 4, 5, 6, 7]
result = search(arr, 1)
print(result)


# _________________________________________________________________________________________________________________________________


# LINEAR SEARCH
arr=[10,5,4,3,7,8,32]
pos=-1
def search(list1,n):
    i=0

    while i<len(list1):
        if n == list1[i]:
            globals()['pos']=i
            return True
        i+=1
    return False

if search(arr,7):
    print('Found at',pos+1)
else:
    print('not found')
