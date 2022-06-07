# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}




from cgitb import text
import re


def read_file_content(file):
    # [assignment] Add your code here 

     with open('./story.txt', 'r') as file:
        contents = file.read()
        return(contents)

result = read_file_content("./story.txt")
print (result)           
    
           



def count_words():
    text = read_file_content("Reading-Text-Files\story.txt")
    # [assignment] Add your code here
    words = text.split()
    word_count = {}
    for word in words:
          
           word = re.sub(r'[^\w\s]', '', word).lower()
           
           if word in word_count:
                word_count[word] += 1
           else:
                word_count[word] = 1
               
    return word_count


print(count_words())
    #return {"as": 10, "would": 20}
   