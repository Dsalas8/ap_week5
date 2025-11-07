
#restructure code without 
#changing its external behavior 
#this helps improve 

#importing the functions 
from problem_set1 import problem1


# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
every_second_letter = alphabet[0:13:2]
# c. Reverse the entire string using slicing.
reversed_alphabet = alphabet[::1]
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote.find('John F. Kennedy'))# out put 83
personality_name = quote[83:] 
print(personality_name)
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
quote = "Python is fun. Fun is good. Good is subjective."
print(quote.find('subjective'))
adjective = quote[36:]
print(adjective)
# b. Extract every third word.
every_third_word = quote.split()[::3]
print(every_third_word)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reversed_word_positions = quote.split()[::1]
print(reversed_word_positions)
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text = "MAY THE FORCE BE WITH YOU"
lowercase_text = print(text.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
motto =["Make", "Haste", "slowly"]
motto_string = ' '.join(motto)
print(motto_string)
# b. Now, split the string at every occurrence of the letter 'a'.
every_letter_a = motto_string.split('a')
print(every_letter_a)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
Life = "Life is what happens when you are busy making other plans"
new_life = Life.replace("plans","mistakes") 
print(new_life)
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word = "moonlight"
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
appears_in_quote = word in quote
print(appears_in_quote)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
phrase ="Supercalifragilisticexpialidocious"
length_of_phrase = len(phrase)
# b. Count the number of times the letter 'i' appears in the same word/phrase.
count_of_i = phrase.count('i')
print(count_of_i)
