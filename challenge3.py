text = input("input a text: ")
#tell them to enter a text
print("You entered: " + text)
#tell them to put 3 random letters
#we tell them how many times the random letters appeared in the text
letter1 = input("input a random letter: ")
letter2 = input("input a random letter: ")
letter3 = input("input a random letter: ")

count = text.count(letter1)
print(f"The letters '{letter1}' appears {count} time(s) in the text.")
count = text.count(letter2)
print(f"The letters '{letter2}' appears {count} time(s) in the text.")
count = text.count(letter3)
print(f"The letters '{letter3}' appears {count} time(s) in the text.")

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