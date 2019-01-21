#Import necessary modules
import time
import random

#Initialize vocabulary list
#Vocabulary list has pre-built values

vocab_list = [
  ('Intelligent', 'Having or showing intelligence, especially of a high level.'), 
  ('Hardworking', '(of a person) tending to work with energy and commitment; diligent.'), 
  ('Conscientious', '(of a person) wishing to do what is right, especially to do one\'s work or duty well and thoroughly'),
  ('Dilligent','having or showing care and conscientiousness in one\'s work or duties.')]

# Create the character class
class Character:
    def __init__(self, char_name = '', char_lvl = 1, total_points = 0):
      self.char_name = char_name
      self.char_lvl = char_lvl
      self.total_points = total_points
    def printProfile(self):
      print("Character Name: ", self.char_name)
      print("Level:",self.char_lvl)
    # Takes in the points earned and adds to the character's level.  Returns level.
    def experienceCalculator(self, char_lvl, points_earned):
      total_points = 0
      exp_ceiling = char_lvl * 30
      total_points += points_earned
      while self.total_points > exp_ceiling:
        char_lvl += 1
        print("You've gained a level, congratulations!")
        total_points = points_earned - exp_ceiling
      return char_lvl
      
# Randomizes the position of the options for the vocabulary test.  
def randomize(a, b ,c):
  if a > b > c: 
    a = 0
    b = 1
    c = 2
  elif a > c > b:
    a = 0 
    c = 1
    b = 2
  elif c > a > b:
    c = 0
    a = 1
    b = 2
  elif c > b > a:
    c = 0
    b = 1
    a = 2
  elif b > c > a:
    b = 0
    c = 1
    a = 2
  elif b > a > c:
    b = 0
    a = 1
    c = 2
  # In the case that one of the randomized values is the same as another,
  # adds one for the case and recursively calls the randomize function.
  else:
    if a == b:
      a += 1
      randomize(a,b,c)
    elif b == c:
      b += 1
      randomize(a,b,c)
    else:
      c += 1
      randomize(a,b,c)
  # Adds the values in at their indexed positions.
  return [a, b, c]

# Checks if the option that the user selects is the same as the definition of the 
# word
def checkIfCorrect(test_word, word_to_check):
  if test_word[1] == word_to_check[1]:
    increase_points = True
  else:
    increase_points = False
  return increase_points

# Returns the minutes that the user was reading for.
def timeCalculation(start_hour, start_min, end_hour, end_min):
    if end_min >= start_min:
      minutes = end_min - start_min
      hours = end_hour - start_hour
    # If the end minutes are less than the start minutes, the
    # following will happen
    else:
      minutes = 60 - start_min + end_min
      hours = end_hour - start_hour + 1
    hours *= 60
    minutes += hours
    # 1 minute = 1 point
    return minutes
        
def print_menu(char_profile):
    play_character = char_profile
    char_lvl = play_character.char_lvl
    command = 0          
    menu = "Enter 1 to begin the reading timer\nEnter 2 to play the vocabulary game\nEnter 3 view character profile\nEnter 4 to quit"
    while command != 4:
      print(menu)
      
      command = int(input("What would you like to do? Enter your choice: "))
      if command == 1:
        print("Welcome! You have started the timer!\nWhen you come across a word that you don't know, add it into your list!")
        print("When you want to stop, go ahead and enter 'n' at the prompt.")
        # Takes the initial time stamp from the system clock
        start_time = time.localtime()
        start_min = start_time.tm_min
        start_hour = start_time.tm_hour
        keep_going = 'y'
        while keep_going != 'n':
          # Takes a word from the user and stores it in a tuple
          new_word = str(input("Enter a word that you want to add to your vocabulary list: "))
          word_definition = str(input("Enter the word\'s definition: "))
          new_entry = (new_word, word_definition)
          vocab_list.append(new_entry)
          keep_going = str(input("Would you like to enter another value? (y/n): "))
        # Takes the ending time stamp
        end_time = time.localtime()
        end_hour = end_time.tm_hour
        end_min = end_time.tm_min
        # Stores minutes in the points value
        play_character.points_earned = timeCalculation(start_hour, start_min, end_hour, end_min)
        command = 0
      elif command == 2:
        another_test = 'y'
        points_earned = 0
        range_ceiling = len(vocab_list)-1
        mid = range_ceiling//2
        # Sets the ceiling of the range to the minimum number of items for the user to be 
        # tested on.
        # Sets the number of points that the user earns per session at 0
        while another_test != 'n':
          # Generates a number to store in 'a', 'b' and'c' for the indexed position of the word
          # in vocab_list
          A = random.randint(0, range_ceiling)
          # If 'a' is at index position 0, we need to generate two other words from 
          # further up the list
          if A == 0:
            B = random.randint(1, mid)
            C = random.randint(mid, range_ceiling)
            # If 'a' is at index position at the end of the list, we need to generate two other 
           # words from further down the list
          elif A == range_ceiling:
            range_ceiling -= 1
            B = random.randint(mid, range_ceiling)
            C = random.randint(0, mid)
          # If 'a' is at index position in the middle of the list, we can generate another 
        # option from either side of test_word.
          else:
            upper_limit = A - 1
            lower_limit = A + 1
            B = random.randint(0, upper_limit)
            C = random.randint(lower_limit, range_ceiling)
            # Takes the tuples at the randomized index positions and stores them in the 
            # word variables.
          test_word = vocab_list[A]
          first_word = vocab_list[B]
          second_word = vocab_list[C]
          test_word_def = test_word[1]
          first_word_def = first_word[1]
          second_word_def = second_word[1]
          # Overwrites the 'a','b' and 'c' items to set the options for the test.  
          # I chose the range 0 - 30 because the likelihood that two randomized numbers
          # would be the same would be less, which would decrease the likelihood that the
          # program would run the randomize function over and over again.
          a = random.randint(0,30)
          b = random.randint(0,30)
          c = random.randint(0,30)
          # Returns a randomized index of values for the tested words
          tested_words = randomize(a, b, c)
          a = tested_words[0]
          b = tested_words[1]
          c = tested_words[2]
          for word,i in enumerate(tested_words):
            if i == 0:
              tested_words[word] = test_word_def
            elif i == 1:
              tested_words[word] = first_word_def
            else:
              tested_words[word] = second_word_def
          # Stores the tails of the tuples in the position of the returned randomized index positions
          # for example, [b, c, a] would be [second_word, first_word, test_word]
          print("What is the definition of {0}?". format(test_word[0]))
          print("Option 1: {0}".format(tested_words[0]))
          print("Option 2: {0}".format(tested_words[1]))
          print("Option 3: {0}".format(tested_words[2]))
          answer = int(input("Enter your choice(1, 2 or 3): "))
          # Checks the user's selection to see if the user's selection is correct.
          if answer == 1:
            word_to_check = tested_words[0]
            increase_points = checkIfCorrect(test_word_def, word_to_check)
          elif answer == 2:
            word_to_check = tested_words[1]
            increase_points = checkIfCorrect(test_word_def, word_to_check)
          elif answer == 3:
            word_to_check = tested_words[2]
            increase_points = checkIfCorrect(test_word_def, word_to_check)
          else: 
            print("Not sure if I have that option.")
            increase_points = False
          if increase_points == True:
            # Increases the current exp of the character
            points_earned += 5
            play_character.experienceCalculator(char_lvl, points_earned)
            print("Congratulations! You are right!")
          else:
            print("That doesn't seem to be the answer..")
          another_test = input("Would you like to try again? (y/n)")
        command = 0
      elif command == 3:
        play_character.printProfile()
        command = 0
      else: 
        print("That doesn't seem to be an option...")
        command = 0
      if command == 4:
        print("Goodbye!")
        break

enter_char_name = ''
print("Welcome to the Vocabulary Tracker!")
enter_char_name = input("Please enter your character\'s name: ")
print("Your Character\'s Name is:", enter_char_name)
char_profile = Character(enter_char_name)
print_menu(char_profile)