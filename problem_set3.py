def problem3():
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