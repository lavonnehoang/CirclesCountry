'''
Created on Feb 21, 2018

@author: lavonnehoang
'''

def decrypt(library,message):
    ret = ""
    for w in message.split():
        char = transform(library,w)
        ret = ret + char
    
    return ret

def transform(library,message):
    for x in library:
        y = x.split()
        if y[1] == message:
            return y[0]
    return "?"

if __name__ == '__main__':
    library = ["O ---"]
    message = "... --- ..."
    print(decrypt(library, message))
    