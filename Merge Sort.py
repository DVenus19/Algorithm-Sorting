print("~~~~~~~~~~ALGORITHM - MERGE SORT~~~~~~~~~~")
print("~~~~~~~~~~Donasco , Venus M.~~~~~~~~~~")
print("~~~~~~~~~~BSCOE 2-2~~~~~~~~~~")

#Python = Merge Sort
def MergeSort(array):
    if len(array) > 1:

#This where r represents the array being divide into 2 subarrays
        r = len(array)//2
        X = array[:r]
        Y = array[r:]

        #
        MergeSort(X)
        MergeSort(Y)


