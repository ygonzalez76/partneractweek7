text = input("input a text:")
#tell them to enter a text
print("You entered: " + text)
#tell them to put 3 random letters
randomletters= input("Input three random letters: ")
print("You entered " + randomletters)

#we tell them how many times the random letters appeared in the text
for letter in randomletters:
    count = text.count(randomletters)
    print(f"The letters '{randomletters}' appears {count} time(s) in the text.")

#we tell them how many words there are in total
num_words = len(text)
print(f'The text has {num_words} words.')

#we tell them their text in inverted order
print(text[::-1])
#we tell them the first and last letter
print(text[0::-1])
print(text[-1])
#we search the text for "python" and tell them if it's true or false
print("python" in text)