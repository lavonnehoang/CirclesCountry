'''
Created on Jan 31, 2018

@author: lavonnehoang
'''

def shorten(name):
    data = name.split()
    dataLength = len(data)
    if dataLength==1:
        return data[0]
    else:
        return data [0] + " " + data[-1]


if __name__ == '__main__':
    print (shorten ("Mary Elizabeth Taylor"))