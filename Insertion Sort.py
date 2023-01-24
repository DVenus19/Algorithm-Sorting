print("~~~~~~~~~~ALGORITHM - INSERTION SORT~~~~~~~~~~")
print("~~~~~~~~~~Donasco , Venus M.~~~~~~~~~~")
print("~~~~~~~~~~BSCOE 2-2~~~~~~~~~~")

#Python - Insertion Sort

def InsertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:




