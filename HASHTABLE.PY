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










def reverse_words_with_hashtable(s):
    # Split the string into words
    words = s.split()
    
    # Create a dictionary (hash table) to store words and their positions
    word_dict = {}
    
    # Populate the dictionary with words and their indices
    for index, word in enumerate(words):
        word_dict[index] = word
    
    # Create a list of words in reverse order
    reversed_words = [word_dict[i] for i in range(len(word_dict)-1, -1, -1)]
    
    # Join the reversed list of words into a single string
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

# Example usage
input_string = 'MY NAME IS SUAIDA'
print(reverse_words_with_hashtable(input_string))  # Output: 'SUAIDA IS NAME MY'




def reverse_words_without_builtin(s):
    # Step 1: Manually split the string into words
    word_list = []
    word = ''
    
    for char in s:
        if char == ' ':
            if word:
                word_list.append(word)
                word = ''
        else:
            word += char
    
    # Append the last word if there's any
    if word:
        word_list.append(word)
    
    # Step 2: Use a dictionary to reverse the order of words
    word_dict = {}
    for index, word in enumerate(word_list):
        word_dict[index] = word
    
    # Step 3: Create a reversed list of words
    reversed_words = []
    for i in range(len(word_dict) - 1, -1, -1):
        reversed_words.append(word_dict[i])
    
    # Step 4: Manually join the reversed words into a single string
    reversed_string = ''
    for i, word in enumerate(reversed_words):
        if i > 0:
            reversed_string += ' '
        reversed_string += word
    
    return reversed_string

# Example usage
input_string = 'MY NAME IS SUAIDA'
print(reverse_words_without_builtin(input_string))  # Output: 'SUAIDA IS NAME MY'
