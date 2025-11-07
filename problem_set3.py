def problem3():
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