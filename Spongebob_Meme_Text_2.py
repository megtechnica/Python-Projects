def SpongeBob_Meme_Text(meme_text):
    returned_string = []
    for letter, word in enumerate(meme_text): 
        if letter %2 == 0:
            returned_string.append(word.upper())

        else:
            returned_string.append(word.lower())
    returned_string = ''.join(returned_string)

    return returned_string
meme_text = input("Please enter a phrase that you would like to modify: ")

returned_string = SpongeBob_Meme_Text(meme_text)
print(returned_string)