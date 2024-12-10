text = input()
text = text.lower()
for letter in text:
    if letter in 'a': 
        text = text.replace(letter, "")
    elif letter in 'e':
        text = text.replace(letter, "")
    elif letter in 'i':
        text = text.replace(letter, "")
    elif letter in 'o':
        text = text.replace(letter, "") 
    elif letter in 'u':
        text = text.replace(letter, "")
print(text)

