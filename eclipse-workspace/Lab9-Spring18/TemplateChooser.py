'''
Created on Apr 2, 2018

@author: ola
'''
import os

def dirToDictionary(dirname):
    """
    dirname is name of a folder containing
    text files. Create and return a dictionary
    in which keys are integers 0,1,2,...
    and values are file names in folder
    """
    data = os.listdir(dirname)
    d = {}
    index = 0
    for one in data:
        f = os.path.join(dirname,one)
        d[index] = f
        index += 1
    
    return d

def reader(path):
    """
    path is a file that can be opened
    return a list of lines from the file,
    line is a string withOUT a newline
    """
    f = open(path, encoding="utf-8")
    ret = f.readlines()
    f.close()
    return [x.strip() for x in ret]

def chooseOne(d):
    """
    d is a dictionary in which values are
    file-names. Allow user to choose a file-name
    and return that full-path filename
    """
    while True:
        for key in d:
            print("%d\t%s" % (key,d[key])) 
        print("------")
        st = input("choose one> ")
        try:
            val = int(st)
            if 0 <= val and val < len(d):
                return reader(d[val])
        except ValueError:
            print("please enter a number")

def getTemplateLines(dirname):
    """
    dirname is a string that's the name of a folder
    Prompt user for files in folder, allow user
    to choose, and return the lines read from file
    """
    d = dirToDictionary(dirname)
    lines = chooseOne(d)
    return lines

if __name__ == '__main__':
    lines = getTemplateLines("templates")
    print(lines)