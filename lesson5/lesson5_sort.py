import numpy as np
import time

def quicksort(array):
    if len(array) < 2 :
        return array
    else :
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greate = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greate)

def selectsort(array):
    output = []
    while len(array) > 0:
        minimum = array[0]
        index = 0
        for i in range(len(array)):
            if array[i] < minimum:
                minimum = array[i]
                index = i
        output.append(minimum)
        array = array[:index] + array[index+1:]
        # del array[index]
    return output

def blobsort(array):
    for j in range(len(array)-1):
        for i in range(len(array)-1 - j):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array


# array = [1,5,2,3,7]
array = [np.random.randint(1, 1000) for _ in range(3000)]

tic = time.time()
print(blobsort(array))
print('the blobsort cost time is ', time.time() - tic, ' seconds.')

tic = time.time()
print(selectsort(array))
print('the simplesort cost time is ', time.time() - tic, ' seconds.')

# array = [np.random.randint(1, 100) for _ in range(100)]

tic = time.time()
print(quicksort(array))
print('the quicksort cost time is ', time.time() - tic, ' seconds.')
