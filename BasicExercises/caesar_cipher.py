print("Please input a piece of text you'd like to be encrypted")
text = str(input()) #Takes the string being encrypted
shift = 3 #How much the characters are getting shifted by
encrypted = '' #The encrypted text
for i in range(len(text)):
    if i != ' ' or '.' or '?' or '!':
        encrypted.append(chr(ord(text[int(i)]) + shift)) 

print(encrypted)
#working on it
