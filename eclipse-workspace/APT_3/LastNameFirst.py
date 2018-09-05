'''
Created on Feb 14, 2018

@author: lavonnehoang
'''

def modify (name):
    name = name.split()
    if len(name) == 1:
        return name
    if len(name) == 2:
        ret = name[1] + ", " + name[0]
        strRet = str(ret)
        return strRet
    else:
        x = ""
        for i in range(len(name)):
            x += name[i][0] + ". "
        ret = name [-1] + ", " + name [0] + x[2:-3]
        strRet = str(ret)
        return strRet
if __name__ == '__main__':
    print (modify ("Elizabeth Rosamund Hartsell Taylor"))