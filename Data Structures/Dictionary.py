mydict = {}

mydict = {'a':'apple','b':'ball','c':'cat'}

# Methods

'''
mydict.clear()
print(mydict)
'''

'''
x  = mydict.copy()
print(x)
'''

'''
x = ('key1','key2','key3')
y = ('2')

mydict = dict.fromkeys(y,x)
print(mydict)
'''

'''
x = mydict.get('b')
print(x)
'''

''' 
x = mydict.items() # Returns a tuple with all the key-value pair
print(x)
print(mydict)
'''

'''
x = mydict.keys() # Returns all the keys
print(x)
'''

'''
mydict.pop('a') # Removes perticular item
mydict.popitem() # Removes last item from dict
print(mydict)
'''

'''
# Returns all the values
x = mydict.values()
print(x)
'''


#Insert an item into dict
mydict.update({'d':'dog'})

print(mydict)
