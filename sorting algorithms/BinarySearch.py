def BinarySearch(arr, low, high, x):
    
    if (high >= low):

        mid = (low + high) // 2
        if(arr[mid] == x):
            return mid
        elif(arr[mid] > x):
            return BinarySearch(arr, low, mid-1, x)
        else: 
            return BinarySearch(arr, mid+1, high, x)
        
    else: 
        return -1



