print("~~~~~~~~~~ALGORITHM - QUICK SORT~~~~~~~~~~")
print("~~~~~~~~~~Donasco , Venus M.~~~~~~~~~~")
print("~~~~~~~~~~BSCOE 2-2~~~~~~~~~~")

#Pyton - Quick Sort
def Partition(array, low, high):
    pivot = array[high] #Rightmost element as pivot
    i = low - 1 #pointer for greater element in the array

    for j in range(low, high): # traverse through all elements and compare each element with pivot
        if array[j] <= pivot:
            i = i + 1  # if element smaller than pivot, then swap it with greater element pointed by i
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

# function to perform quicksort
def QuickSort(array, low, high):
    if low < high:
        pi = Partition(array, low, high)

    # recursive call on the left of pivot
        QuickSort(array, low, pi - 1)

    # recursive call on the right of pivot
        QuickSort(array, pi + 1, high)


data = [50,71,7,81,20,6,30,90,86,10]
print("Given Unsorted Array Value: ")
print(data)

size = len(data)

QuickSort(data, 0, size - 1)

print('Result of the sorted array by Merge Sort:')
print(data)