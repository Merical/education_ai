import numpy as np
import time

def blobsort(array):
    '''your code here'''
    pass

def selectsort(array):
    '''your code here'''
    pass

def quicksort(array):
    if len(array) < 2 :
        return array
    else :
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greate = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greate)

'''
    本次作业实现两种排序算法：1）冒泡排序bubblesort 2）选择排序selectsort 
    请使用python借鉴ppt上的讲解完成
    
    array是长度为3000的随机整数列表，请实现两种排序算法并与快速排序quicksort比较，看看哪一个更快？为什么？
    
'''

array = [np.random.randint(1, 1000) for _ in range(3000)]

tic = time.time()
print(blobsort(array))
print('the blobsort cost time is ', time.time() - tic, ' seconds.')

tic = time.time()
print(selectsort(array))
print('the simplesort cost time is ', time.time() - tic, ' seconds.')


tic = time.time()
print(quicksort(array))
print('the quicksort cost time is ', time.time() - tic, ' seconds.')
