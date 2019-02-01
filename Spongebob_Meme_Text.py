def SpongeBob_Meme_Text(meme_text):
    x = 0
    returned_string = []
    for letter in meme_text:
        if x %2 == 0:
            returned_string.append(letter.upper())
        else:
            returned_string.append(letter.lower())
        x+=1
    returned_string = ''.join(returned_string)

    return returned_string

meme_text = input("Please enter a phrase that you would like to modify: ")

returned_string = SpongeBob_Meme_Text(meme_text)
print(returned_string)