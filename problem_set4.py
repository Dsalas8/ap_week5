def problem4():
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