print("~~~~~~~~~~ALGORITHM - SELECTION SORT~~~~~~~~~~")
print("~~~~~~~~~~Donasco , Venus M.~~~~~~~~~~")
print("~~~~~~~~~~BSCOE 2-2~~~~~~~~~~")

#Python - Selection Sort

def SelectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
    #Change > to < to sort in descending order
            if array[i] < array[min_idx]:
                min_idx = i

        #next, place the min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

data = [50,71,7,81,20,6,30,90,86,10]
size = len(data)
SelectionSort(data, size)
print('Result of the sorted array by Selection Sort: ')