def insertion_sort(array):
    for number in range(1, len(array)):
        current_value = array[number]
        position = number
        
        while position > 0 and array[position-1] > current_value:
            array[position] = array[position-1]
            position = position-1

        array[position] = current_value

array = [34,65,23,77,3,34,423,9,0]
insertion_sort(array)
print(array)
    