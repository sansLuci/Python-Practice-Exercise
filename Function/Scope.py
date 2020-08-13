x = 300 # global

def myfunc():
    global x
    x = 200 # local
    print(x)

myfunc()

print(x)

# 'global' keyword to declear a local variable globally