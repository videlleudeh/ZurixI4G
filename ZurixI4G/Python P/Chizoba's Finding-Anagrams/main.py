# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


import re
def find_anagram(word, anagram):
    # [assignment] Add your code here

    # filter all non-alphabetic characters and convert to lowercase.
    word = "".join(re.findall("[a-zA-Z]+", word)).lower()
    anagram = "".join(re.findall("[a-zA-Z]+", anagram)).lower()

    if sorted(word.lower()) == sorted(anagram.lower()):
        return True
    else:
        return False

print(find_anagram("hello", "check"))
print(find_anagram("meBelow ", "elbow me"))
print(find_anagram("redivider", "ddreiViEr"))

