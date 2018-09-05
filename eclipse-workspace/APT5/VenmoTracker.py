'''
Created on Mar 20, 2018

@author: lavonnehoang
'''

def networth(transactions):
    ret = []
    d = {}
     
    for x in transactions: 
        data = x.split(":")
        payer = data[0]
        payee = data[1]
        amount = int(float(data[2])*100) 
        
        if payer not in d:
            d[payer] = 0 
        if payee not in d:
            d[payee] = 0
         
        d[payer] -= amount
        d[payee] += amount
        
    for nm in sorted(d.keys()):
        dollar = d[nm]
        ret.append(nm + ":" + str(float(dollar)/100))
    
    return ret

if __name__ == '__main__':
    tr = ["owen:susan:10", "owen:robert:10", "owen:drew:10"]
    print(networth(tr))
