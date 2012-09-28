import os
#returns currtdir as string
print(os.getcwd())
currentdir = os.getcwd()


#creates a directory
dirname = "testfolder"
if not os.path.isdir("./" + dirname + "/"):
    os.mkdir("./" + dirname + "/")

#another way to get currentdir    
from os.path import abspath, dirname
currentdir = abspath(dirname('imageoftheday.py'))
print(currentdir)
