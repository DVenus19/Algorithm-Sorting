print("~~~~~~~~~~ALGORITHM - INSERTION SORT~~~~~~~~~~")
print("~~~~~~~~~~Donasco , Venus M.~~~~~~~~~~")
print("~~~~~~~~~~BSCOE 2-2~~~~~~~~~~")

#Python - Insertion Sort

def Insertion_Sort(array):
    for i in range(1,len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and value < array[j]:



