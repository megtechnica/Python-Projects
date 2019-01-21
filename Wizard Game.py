import random
import string
def main():
    print("The Wizard Inventory program")
    print("COMMAND MENU")
    print("1 - Walk down the path")
    print("2 - Show all items")
    print("3 - Drop an item")
    print("4 - Exit program")
    myfile = open('wizard_bag.txt',"w")
    myfile.close()
    command = 0
    try:
        while(command != "exit"):
            command = input("Command:")
            if(command == 1):
                walk()
            elif(command == 2):
                show()
            elif(command == 3):
                drop()
            elif(command == 4):
                break
            elif type(command) == str:
                raise ValueError("Invalid Type")
            else: 
                print("That is not a valid command!")
        print("Bye!")
        return
    except ValueError as excpt:
        print("Could not accept the input command")
    except IOError as excpt:
        print("Could not find the file")
    except:
        print("Unknown Error Encountered :(")
        
    
def walk():
    choice = 0
    random_line = random.choice(list(open('wizard_all_items.txt')))
    print("While walking down a path you see", random_line)
    choice = int(input("Do you want to grab it? (1 for yes/2 for no):"))
    if choice == 1:
        myfile = open('wizard_bag.txt',"a")
        myfile.write(random_line.rstrip()+"\n")
        myfile.close()
    elif choice == 2:
        return
    else:
        print("That is not a valid choice!")
def drop():
    item = int(input("number:")) 
    i = open("wizard_bag.txt","r")
    lines = i.readlines()
    i.close()
    l = open("wizard_bag.txt","w")
    counter = 1
    for line in lines:
        if (counter != item):
            l.write(line)
        counter += 1
    i.close()
def show():
    i = open("wizard_bag.txt","r")
    lines = i.readlines()
    for line in lines:
        print(line)
    i.close()


main()