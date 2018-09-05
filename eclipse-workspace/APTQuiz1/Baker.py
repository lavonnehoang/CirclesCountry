'''
Created on Feb 6, 2018

@author: lavonnehoang
'''


def amount(desired):
    if desired <= 12:
        return desired
    else:
        return  (desired-(desired//13)*13) + ((desired//13)*12)
if __name__ == '__main__':
    print (amount(512))