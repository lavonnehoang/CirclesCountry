'''
Created on Jan 31, 2018

@author: lavonnehoang
'''

def ratio(dna):
    c_count = dna.count('c')
    g_count = dna.count('g')
    total = c_count + g_count
    return total/(len(dna))
        
if __name__ == '__main__':
    print (ratio("agatc"))
    
    w = "reading is fundamental"
    print (w[:7]) 