'''
Created on Feb 20, 2018

@author: lavonnehoang
'''

def whichOrder(available, orders):
    setAvailable = set(available)
    for i in orders:
        a = i.split()
        setOrders = set(a)
        match = setAvailable & setOrders
        a = set(a)
        if a <= match:
            return orders.index(i)
    return -1
            
    

        
        

if __name__ == '__main__':
    available = [ "ham", "cheese", "mustard" ]
    orders = [ "ham cheese", "bacon tomato" ]
    whichOrder(available,orders)
    
