def binary_search(arr, target, low=None, high=None):
    if low is None and high is None:
        low, high = 0, len(arr) - 1

    mid = low + (high - low) // 2

    if target == arr[mid]:
        return mid+1
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

arr = [1, 2, 3, 4, 5, 6, 7]
result = binary_search(arr, 7)
print(result)

# ____________________________________________________________________________________________________________________

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

n=factorial(5)
print(n)

# ____________________________________________________________________________________________________________________


def fibanocci(n):
    if n<=1:
        return n
    else:
        return fibanocci(n-1) + fibanocci(n-2)
print(fibanocci(6))



# ____________________________________________________________________________________________________________________


def sum(n):
    if n<=0:
        return n
    else:
        return n+sum(n-1)
    
print(sum(996))    


# ____________________________________________________________________________________________________________________


def power(num,p):
    if p<1:
        return 1
    else:
        return num*power(num,p-1)
    
print(power(5,3))    



# ____________________________________________________________________________________________________________________


def reverse(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+reverse(s[:-1])
    
print(reverse('hrishikeshprasadc@gmail.com'))



# ____________________________________________________________________________________________________________________


def palendrome(s):
    s=s.lower()
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and palendrome(s[1:-1])

print(palendrome('Malayalam'))
print(palendrome('English'))




# ____________________________________________________________________________________________________________________

def fact(num):
    if num<=1:
        return 1
    return num * fact(num-1)

result=fact(990)
print(result)    




# ____________________________________________________________________________________________________________________


def oper(num):
    if num<1:
        return 1
    oper(num-1)
    print(num,end=' ')
    oper(num-1)
    return

oper(3)

# ____________________________________________________________________________________________________________________

