# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


import re


def find_anagram(word, anagram):
    # [assignment] Add your code here
   
    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")

    word = word.lower()
    anagram = anagram.lower()


    if sorted(word.lower()) == sorted(anagram.lower()):
        return True
    else:
        return False

print(find_anagram("hello", "lleho"))
print(find_anagram("Chizoba ", "bazochi"))
print(find_anagram("iloveyou", "ihateyou"))
print(find_anagram("Mathematics", "mahetamtic"))



   

