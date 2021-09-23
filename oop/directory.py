# URL : https://www.askpython.com/python/python-directory-operations

# 1. CREATING A NEW DIRECTORY

import os
os.mkdir('C:/python1') #create a direcotry abc in C:
os.mkdir('/Users/Armando/Desktop') # create a directory in the desktop folder


# 2. GET THE CURRENT DIRECTORY

import os
os.getcwd() 


# 3. RENAME DIRECTORY

os.rename(old,new)


# 4. LIST DIRECTORIES

os.listdir('path_to_the_directory_to_be_listed')


# 5. REMOVE DIRECTORIES

os.rmdir('path_to_directory_to_be_removed')

# 6. CHECK IF A DIRECTORY EXIST

os.path.exists('path')