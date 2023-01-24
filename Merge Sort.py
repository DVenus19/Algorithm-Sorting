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

        #sort it into two
        MergeSort(X)
        MergeSort(Y)


        i = j = k = 0


        while i < len(X) and j < len(Y):
           if X[i] < Y[j]:
                   array[k] = X[i]
                   i += 1
           else:
                   array[k] = Y[j]
                   j += 1
           k += 1

        while i < len(X):
            array[k] = X[i]
            i += 1
            k += 1

        while j < len(Y):
            array[k] = Y[j]
            j += 1
            k += 1

def List(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
