# DICTIONARY.PY
new={'1':'hrishi','2':'prasd','3':'hrishikesh'}
# print(new)
# print(type(new))

# print(new['2'])
# print(new['1'])
print(new.values())
# print(new.keys())
# print(new.get('1'))
# for x in new:
#     print(x)
# for x in new.values():
#     print(x)
# for x,y in new.items():
#     print(y,x)

# new['2']='Prasad'
# new['4']='c'

# print(new)



# _________________________________________________________________________________________________________________________________

# DUPLICATES
def remove_duplicates(dict1):
    res={key:value for key,value in dict1.items() if list(dict1.values()).count(value)==2}
    return res

dict1={'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
res=remove_duplicates(dict1)
print(res)

# _________________________________________________________________________________________________________________________________

# INVERT

input_dict = {'a': 1, 'b': 2, 'c': 3}
invert={ value :key for key,value in input_dict.items()}
print(invert)


# _________________________________________________________________________________________________________________________________

# MERGE

def merge_dictionaries(dict1, dict2):
    for x in dict1:
        if x in dict2:
            dict1[x]=dict2[x]
    dict1.update(dict2)    
    return dict1 
# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)


# _________________________________________________________________________________________________________________________________

# WORD FREQUENCY

def word_frequency(sentence):
    words=sentence.split()
    freq={}

    for word in words:
        word=word.lower()
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq        

sentence="This is a simple example. This example demonstrates word frequency"
res=word_frequency(sentence)
print(res)