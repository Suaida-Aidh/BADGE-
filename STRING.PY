name='hai'
n=54

if n>26:
    n=n%26
    
new_name=''    
for i in range(len(name)):
        
        if ord(name[i])>=122:
            order=96+ ord(name[i])%26
        else:
             order=ord(name[i])
        
        
        new_name+=chr(order+n)
                

print(new_name)