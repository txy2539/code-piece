__author__ = 'Tao Yang'

import csv
import os,os.path

def readFile(file1):
    '''
    read from old files
    '''
    arr1 = []

    targetFile = open(file1)
    target = csv.reader(targetFile)


    for line in target:
        arr1.append(line)

    targetFile.close()

    newArr = []

    #locate item column
    
    termInFrench = 0
    for item in arr1[0]:
        if item != 'Term in French':
            termInFrench = termInFrench + 1
        else:
            break

    # get the first line

    newArr.append(arr1.pop(0))

    # get the length of each line

    colNum = len(arr1[0])

    for line in arr1:
        for i in range( colNum - 1 - termInFrench ):
            if line[termInFrench] == '':
                line[termInFrench] = line[termInFrench + i + 1]
            elif line[termInFrench + i + 1 ] != '' and len(line[termInFrench + i + 1 ]) - 10 <= len(line[termInFrench]):
                line[termInFrench] = line[termInFrench + i + 1]

        newArr.append(line)     

    return newArr


def writeFile(arr1, newFile):
    '''
    write in to new file
    '''
    mergeFile = open(newFile, 'w')
    writer = csv.writer(mergeFile)

    #Write in to new csv file Part 1
    for line in arr1:
        writer.writerow(line)


def file_rm( fileName ):  #delete file
	if(os.path.exists(fileName)):  #check if exist
		os.remove(fileName)        #delete if exist
		print("delete " +  fileName +   " success\n")
	else:
		print("file not exist\n")

def main():
    oldFile = 'Winners-Android-Admin.csv'
    newFile = 'Merged-' + oldFile
    
    #delete old file when run again
    file_rm(newFile)

    arr1 = readFile(oldFile)
    # for i in arr1:
    #     print(i)
    writeFile(arr1, newFile)

main()
