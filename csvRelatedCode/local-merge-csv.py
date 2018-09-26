__author__ = 'Tao Yang'

import csv
import os,os.path

def readFile(file1, file2):
    '''
    read from old files
    '''
    arr2 = []
    arr1 = []

    winnersFile = open(file1)
    selecotosFile = open(file2)
    winners = csv.reader(winnersFile)
    selecotos = csv.reader(selecotosFile)
    
    # with open(file1, 'r', encoding='utf-8') as f:
    #     flag = 1
    #     for line in f:
    #         if flag == 1 :
    #             line = line[1:]
    #             flag = 0
    #         arr1.append(line)
    
    # with open(file1, 'r', encoding='utf-8') as f:
    #     flag = 1
    #     for line in f:
    #         if flag == 1 :
    #             line = line[1:]
    #             flag = 0
    #         arr2.append(line)


    for line in selecotos:
        arr2.append(line)

    for line in winners:
        arr1.append(line)

    winnersFile.close()
    selecotosFile.close()

    newArr = []
    newOthersArr = []
    newDupliArr = []

    #Find the item according to winner's sheet

    for line in arr1:
        hasFound = False
        for target in arr2:
            if line[0] != '' and line[0] != 'n/a':
                if line[0] == target[0]:
                    newArr.append(list((target[0], target[1], target[2], line[2], '-')))
                    hasFound = True
                    break
            else:
                if line[1] == target[1] and line[1] != '':
                    newArr.append(list((target[0], target[1], target[2], line[2],'-')))
                    hasFound = True
                    break
        if hasFound == False:
            if line[1] == '':
                newArr.append(list((line[0], line[1], '','','-')))
            else:
                newArr.append(list((line[0], line[1], '-', line[2], '-')))

    #Find others in selecotos but not in winners        
    for line in arr2:
        hasFound = False
        for target in arr1:
            if line[0] == line[1] and line[0] == '':
                hasFound = True
                break
            elif line[1] != '' and line[1] == target[1]:
                hasFound = True
                break
            elif line[0] !='' and line[0] == target[0]:
                hasFound = True
                break
            
        if hasFound == False:
            newOthersArr.append(list((line[0], line[1], line[2], '-', '-')))


    #Same Identifer but different English term
    for line in arr2:
        for target in arr1:
            if line[0] == target[0] and line[1] != '' and line[0] != '' and line[1] != target[1]:
                newDupliArr.append(list((target[0], target[1], '------Needs adjustment------', '-', '-')))


    return newArr, newOthersArr, newDupliArr


def writeFile(arr1, arr2, arr3, newFile):
    '''
    write in to new file
    '''
    mergeFile = open(newFile, 'w')
    writer = csv.writer(mergeFile)

    #Write in to new csv file Part 1
    for line in arr1:
        writer.writerow(line)

    writer.writerow(list(('')))
    writer.writerow(list(('')))
    writer.writerow(list(('')))
    writer.writerow(list(('**', 'In Selecotos but not in Winner:', '**','-' ,'-')))
    writer.writerow(list(('')))
        

    #Write in to new csv file Part 2
    for line in arr2:
        writer.writerow(line)

    writer.writerow(list(('')))
    writer.writerow(list(('')))
    writer.writerow(list(('')))
    writer.writerow(list(('**', 'Same Identifer but different English term, keep the terms below, need addjust Spanish term','**','-' ,'-')))
    writer.writerow(list(('')))
        
    #Write in to new csv file Part 3
    for line in arr3:
        writer.writerow(line)

def file_rm( fileName ):  #delete file
	if(os.path.exists(fileName)):  #check if exist
		os.remove(fileName)        #delete if exist
		print("delete " +  fileName +   " success\n")
	else:
		print("file not exist\n")

def main():
    fileList = [
                'Android-Admin'
                ,'Android-Frontend'
                ,'API'
                ,'iOS-Admin'
                ,'iOS-Frontend'
                ,'JS-Frontend'
            ]
    for item in fileList:
        oldFile = 'Merged-Winners-' + item + '.csv'
        newFile = 'Selectos-' + item + '.csv'
        mergedFile = 'merged/' + item + '.csv'
        #delete old file when run again
        file_rm(mergedFile)
        arr1, arr2, arr3= readFile(oldFile, newFile)
        writeFile(arr1, arr2, arr3, mergedFile)

main()