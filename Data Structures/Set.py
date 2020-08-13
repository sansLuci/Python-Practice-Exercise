new_set = {'apple','ball','cat'}

'''
new_set.add("orange")
print(new_set)
'''

'''
new_set.clear()
print(new_set)
'''

'''
x = new_set.copy()
print(x)
'''


x = {1,2,3,4,5}
y = {2,4,6,8}

# items that are in x, not in y
# z = x.difference(y)
# print(z)
print(x)



# Removes unmatched items
x.difference_update(y)
print(x)

