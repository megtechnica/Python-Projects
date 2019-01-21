import time
import random

vocab_list = []

class Character:
    def __init__(self, char_name = '', char_lvl = 1):
        self.char_name = char_name
        self.char_lvl = char_lvl
    def timeCalculation(self, start_hour, start_min, end_hour, end_min):
        if self.end_min >= self.start_min:
            minutes = self.end_min - self.start_min
            hours = self.end_hour - self.start_hour
        else:
            minutes = 60 - self.start_min + self.end_min
            hours = self.end_hour - self.start_hour - 1
        hours *= 60
        minutes += hours
        points = minutes // 5
        return points
        
        
        

def print_menu(char_profile):
    play_character = char_profile
    choice = 0          
    print("Enter 1 to begin the reading timer\nEnter 2 to play the vocabulary game\nEnter 3 view character profile\nEnter 4 to quit")
    choice = input("What would you like to do? Enter your choice: ")
    while command != 4:
        if command == 1:
            print("Welcome! You have started the timer!\nWhen you come across a word that\nyou don't know, add it into your list!")
            print("When you want to stop, go ahead and enter 'n' at the prompt to keep going!")
            start_time = time.localtime()
            start_min = start_time.tm_min
            start_hour = start_time.tm_hour
            keep_going = 'y'
            while keep_going != 'n':
                new_word = str(input("Enter a word that you want to add to your vocabulary list"))
                word_definition = str(input("Enter the word\'s definition: "))
                new_entry = (new_word, word_definition)
                vocab_list.append(new_entry)
                keep_going = str(input("Would you like to enter another value? (y/n): "))
            end_time = time.localtime()
            end_hour = end_time.tm_hour
            end_min = end_time.tm_min   
            points = play_character.timeCalculation(start_hour, start_min, end_hour, end_min)
            
enter_char_name = ''
print("Welcome to the Vocabulary Tracker!")
enter_char_name = input("Please enter your character\'s name: ")
print("Your Character\'s Name is:", enter_char_name)
char_profile = Character(enter_char_name)

        
    
