#ex2 Find All Subsets of a Set

def find_subsets(lst):
     if not lst:
        return [[]]
    #exclude first element
     smaller_sub = find_subsets(lst[1:])
    #for each of the smaller subsets!
     new_sub = [subset + [lst[0]] for subset in smaller_sub]

     return smaller_sub + new_sub


print(find_subsets([1,2]))
print(find_subsets([]))
print(find_subsets([1,2,3]))