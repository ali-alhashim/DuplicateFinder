## Take all file path and hash
## add to list objects
## loop get all duplicate save in list object
## show to the user the result for take action


from tkinter import filedialog
from tkinter import *
import os
import hashlib


def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""
   
   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:
       print('Reading binary for getting hash SHA-1.....')
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

counter = 0
fileList =[]
for root, dir, files in os.walk(folder_selected):
    for file in files:
        filePath = root +'/'+str(file)
        fileHash = hash_file(filePath)
        print(filePath, '| Hash = ',fileHash)
        fileList.append((filePath,fileHash))








