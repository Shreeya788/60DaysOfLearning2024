set_a= {1,2,3,4,5}
set_b = {4,5,6,7,8,9}

#Union
print(set_a.union(set_b)) #Joins two sets
#this can also be written as : 
print(set_a | set_b)

#intersection
print(set_a.intersection(set_b)) #prints intersection/ common element of both sets
#this can also be written as : 
print(set_a & set_b)

# difference
print(set_a.difference(set_b)) #prints elements of set_a without intersecting element
#this can also be written as : 
print(set_a - set_b)

#symmetric difference
print(set_a.symmetric_difference(set_b)) #prints all elements of set_a and set_b neglecting intersected elements
#this can also be written as : 
print(set_a ^ set_b)