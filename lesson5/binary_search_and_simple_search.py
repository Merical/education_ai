import time

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        time.sleep(0.01)
    return -1

def simple_search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
        time.sleep(0.01)
    return -1

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list = [i for i in range(1, 1000)]

tic = time.time()
print(simple_search(list, 650))
print('the simple_search cost time is ', time.time() - tic, ' seconds.')

tic = time.time()
print(binary_search(list, 650))
print('the binary_search cost time is ', time.time() - tic, ' seconds.')
