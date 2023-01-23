print("~~~~~~~~~~ALGORITHM - BUBBLE SORT~~~~~~~~~~")
print("~~~~~~~~~~Donasco , Venus M.~~~~~~~~~~")
print("~~~~~~~~~~BSCOE 2-2~~~~~~~~~~")

#Python - Bubble Sort

def BubbleSort(array):
    for i in range(len(array)): #To access the given array element
        for j in range(0, len(array) - i - 1): #To compare given the array element
            if array[j] > array[j + 1]: #to sort in descending order ,change > to <
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp #if elements are not in the intended order swap the elements

data = [50,71,7,81,20,6,30,90,86,10]
BubbleSort(data)

print('Result of the sorted array by Bubble Sort:')
print(data)