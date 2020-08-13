
# Open a file, defult mode = r (read)

# f = open("abc.txt")
# print(f.name)
# print(f.mode)
# f.close()


# Context Manager: it allows to work with file
# in a block and then close it automatically
# also closes when there is some exception

with open("abc.txt") as f:
    # Reads all the data
    
    # print(f.read()) 
    
    # returns all the content in a list
    
    # f_lies = f.readlines() 
    # print(f_lies)
    
    # returns only single line
    
    # f_line = f.readline()
    # print(f_line)
    # f_line = f.readline()
    # print(f_line)
    # f_line = f.readline()
    # print(f_line)
    
    # to print all the lines one by one
    
    # for line in f:
    #     print(line, end='')
    
    # want to return specific sizes content
    # pass the size in read(x)
    
    # size = 20
    # print(f.read(size),end='')
    # print(f.tell())
    # for printing small part of a file
    
    # size = 10
    # f_read = f.read(size)

    # while len(f_read) > 0:
    #     print(f_read,end='*')
    #     f_read = f.read(size)
    
    # want to know at waht position we are on
    '''
    size = 12
    f_read = f.read(size)
    
    a = f.tell()
    print(a)
    '''
    # start print from a perticular position
    
    # size = 13
    # f_read = f.read(size)
    # print(f_read,)
    # f.seek(0)
    # f_read = f.read(size)
    # print(f_read)
    
    
