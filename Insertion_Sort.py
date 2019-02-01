def insertion_sort(array):
    for number in range(1, len(array)):
        current_value = array[number]
        position = number
        
        while position > 0 and array[position-1] > current_value:
            array[position] = array[position-1]
            position = position-1

        array[position] = current_value

choice = ''
array = []
while choice != 'q':
    choice = input("Please either enter a number or enter 'q' to quit: ")
    if choice == 'q':
        break
    else:
        array.append(int(choice))

        
insertion_sort(array)
print(array)
    