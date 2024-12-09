import random

def partition(array, low, high):
    pivot_index = random.randint(low, high)  # Randomly select a pivot
    array[pivot_index], array[high] = array[high], array[pivot_index]  # Swap pivot to the end
    pivot = array[high]
    i = low - 1 
    for j in range(low, high): 
        if array[j] <= pivot: 
            i += 1
            array[i], array[j] = array[j], array[i] 

    array[i + 1], array[high] = array[high], array[i + 1]  
    return i + 1  


def quickSort(array, low=0, high=None):
    if high is None: 
        high = len(array) - 1

    if low < high:
        pi = partition(array, low, high)  
        quickSort(array, low, pi - 1)  
        quickSort(array, pi + 1, high) 

    return array  

######################################################################

def custom_sort_key(num, n):
    if num % 15 == 0:  
        priority = 0
    elif num % 5 == 0:  
        priority = 1
    elif num % 3 == 0:  
        priority = 2
    else:  
        priority = 3
    return (priority, len(str(abs(num))), num % n, num)


def partition(array, low, high, n):
    pivot = array[high]
    pivot_key = custom_sort_key(pivot, n)
    i = low - 1  

    for j in range(low, high):
        if custom_sort_key(array[j], n) <= pivot_key:
            i += 1
            array[i], array[j] = array[j], array[i] 

    array[i + 1], array[high] = array[high], array[i + 1]  
    return i + 1

def quick_sort(array, low=0, high=None, n=1):
    if high is None:  
        high = len(array) - 1

    if low < high:
        pi = partition(array, low, high, n)  
        quick_sort(array, low, pi - 1, n)  
        quick_sort(array, pi + 1, high, n)  

    return array





