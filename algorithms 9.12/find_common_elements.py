def find_common_elements(array1, array2):
    common_elements = []
    for element1 in array1:
        for element2 in array2:
            if(element1 == element2):
                common_elements.append(element1)
    
    #remove duplicates
    return list(set(common_elements))
    #return common_elements

def find_common_elements_improved(array1, array2):
    set1 = set(array1)
    common_elements = [element for element in array2 if element in set1]
    return common_elements



array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]   
print(find_common_elements(array1, array2))
print(find_common_elements_improved(array1,array2))

array3 = [1,1,1,2,3]
array4 = [1,2,3,4,5,6]
print(find_common_elements(array3, array4))
print(find_common_elements_improved(array3,array4))


def find_common_elements_3(array1, array2, array3):
    common_elements = list(set(array1) & set(array2) & set(array3))
    return common_elements

print(find_common_elements_3(array1, array2, array3))
print(find_common_elements_3(array1, array2, array4))