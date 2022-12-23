## Take all file path and hash
## add to list objects
## loop get all duplicate save in list object
## show to the user the result for take action


from tkinter import filedialog
from tkinter import *
import os
import hashlib
import multiprocessing 
from timeit import default_timer as timer






counter = 0
fileList =[]
duplicateList =[]
duplicateOne =[]
processes =[]

######################################## Hash function
def hash_file(filename):
 
   
   # make a hash object
   h = hashlib.blake2b()

   # open file for reading in binary mode
   with open(filename,'rb') as file:
       print('Reading binary for getting hash blake2b.....')
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           # update for speed I change to 64000
           chunk = file.read(64000)
           h.update(chunk)

   # return the hex representation of digest
   fileHash = h.hexdigest()
   print(filename, '| Hash = ',fileHash)
   fileList.append((filename,fileHash))
   return h.hexdigest()

####################################################################





############# list file with hash #################

def loopFiles(folder_selected):
    for root, dir, files in os.walk(folder_selected):
        for file in files:
            filePath = root +'/'+str(file)
            
            hash_file(filePath)
            p = multiprocessing.Process(target=hash_file, args=(filePath,))
            p.start()
            processes.append(p)

    for p in processes:
        p.join()

            
   

 

   
       
    
######################################################

### compare the hash #################################

def compareFiles():
    for x in range(len(fileList)):
        for y in range(len(fileList)):
            if y+x+1 < len(fileList):
                z = y+x+1
            else:
                break
            print(fileList[x], ' VS ', fileList[z])
            if fileList[x][1] == fileList[z][1]:
                duplicateList.append(fileList[x])
                duplicateList.append(fileList[z])
                duplicateOne.append(fileList[z])



    print('Total Files : ',len(fileList))
    print('the result for all duplicate files : ', duplicateList)
    print('Total Files : ',len(duplicateOne))

    if len(duplicateOne) !=0:
        Confirmation = input('please write yes to delete the duplicated files ! :\n')

        if Confirmation =='yes':
            print('Deleteting.....')
            for x in range(len(duplicateOne)):
                file = duplicateOne[x][0]
                print('delete file '+file)
                try:
                    os.remove(file)
                except Exception as e:
                    print(e)

        else:
            print('No Action...See You')
    else:
        print('Done!  No Duplicate')

###############################################################

if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

    loopFiles(folder_selected)
    compareFiles()