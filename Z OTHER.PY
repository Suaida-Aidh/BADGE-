def character_count(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

string = "hello world"
print(character_count(string))
