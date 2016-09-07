# Remove equal adjacent elements
#
# Example input: [1, 2, 2, 3]
# Example output: [1, 2, 3]
def remove_adjacent(lst):
    return([x for x in set(lst)])
 
# Merge two sorted lists in one sorted list in linear time
#
# Example input: [2, 4, 6], [1, 3, 5]
# Example output: [1, 2, 3, 4, 5, 6]
def linear_merge(lst1, lst2):
    return(lst1+lst2)
lst1=[1,1,2,4,4]
lst2=[1,1,2,4,3]
print(remove_adjacent(lst1))
print(linear_merge(lst1,lst2))
