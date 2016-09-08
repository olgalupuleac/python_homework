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
    i=0
    j=0
    lst=[]
    while (i<len(lst1))and (j<len(lst2)):
        if (lst1[i]<lst2[j]):
            lst.append(lst1[i])
            i=i+1
        else:
            lst.append(lst2[j])
            j=j+1
    else:
        if i<len(lst1):
            lst.extend(lst1[i:])
        else:
            lst.extend(lst2[j:])
            
    return(lst)
lst1=[1,1,2,4,4,7]
lst2=[1,1,2,4,5]
print(remove_adjacent(lst1))
print(linear_merge(lst1,lst2))
