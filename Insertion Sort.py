print("~~~~~~~~~~ALGORITHM - INSERTION SORT~~~~~~~~~~")
print("~~~~~~~~~~Donasco , Venus M.~~~~~~~~~~")
print("~~~~~~~~~~BSCOE 2-2~~~~~~~~~~")

#Python - Insertion Sort

def InsertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

       #Compare the key in left element if its greater or less than until smallest element is found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

            array[j + 1] = key #place the key after finding the element smaller from it

data = [50,71,7,81,20,6,30,90,86,10]

InsertionSort(data)
print('Result of the sorted array by Bubble Sort:')
print(data)




