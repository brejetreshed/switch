def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

#####################################################################################

def merge_sort_by_abs(arr):
#same as above, just call the other func
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_by_abs(arr[:mid])
    right = merge_sort_by_abs(arr[mid:])

    return merge_by_abs(left, right)


def merge_by_abs(left, right):
    merged = []
    i = j = 0

    while (i < len(left) and j < len(right)):
        if abs(left[i]) <= abs(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

#####################################################################################

def merge_sort_by_capital(arr):
    #same as above, just call the other func
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_by_capital(arr[:mid])
    right = merge_sort_by_capital(arr[mid:])

    return merge_capital_first(left, right)

def is_capital_first(s):
    return s[0].isupper()

def merge_capital_first(left, right):
    merged = []
    i = j = 0

    while (i < len(left) and j < len(right)):
        if (is_capital_first(left[i]) and not is_capital_first(right[j])) or \
           (is_capital_first(left[i]) == is_capital_first(right[j]) and left[i] <= right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

#####################################################################################

def merge_sort_by_odd_first(arr):
    #same as above, just call the other func
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_by_odd_first(arr[:mid])
    right = merge_sort_by_odd_first(arr[mid:])

    return merge_odd_first(left, right)

def is_odd(n):
    return (n % 2 == 1)

def merge_odd_first(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (is_odd(left[i]) and not is_odd(right[j])) or \
           (is_odd(left[i]) == is_odd(right[j]) and left[i] <= right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

#####################################################################################

def merge_sort_by_prime_first(arr):
    #same as above, just call the other func
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_by_prime_first(arr[:mid])
    right = merge_sort_by_prime_first(arr[mid:])

    return merge_primes_first(left, right)

def is_prime(n):
    if n <= 1:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def merge_primes_first(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (is_prime(left[i]) and not is_prime(right[j])) or \
           (is_prime(left[i]) == is_prime(right[j]) and left[i] <= right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged