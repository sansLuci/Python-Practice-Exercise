'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
'''

f = open("demo.txt", "a")
f.write("Appending some content at the end")
f.close()

f = open("myfile.txt", "x")


####################################
##### Deleting a file or folder#####
####################################

import os
os.remove("demo.txt") # file
os.rmdir("myfolder") # folder

