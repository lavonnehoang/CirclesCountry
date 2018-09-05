'''
Created on Apr 17, 2018

@author: lavonnehoang
'''

def winners(data):
    d = {}
    for one in data:
        x = one.split()
        name = x[0]
        time = x[1].split(":")
        seconds = (int(time[0])*60) + int(time[1])
        if name not in d: 
            d[name] = [0,0] 
        d[name][0] += seconds
        d[name][1] += 1
    
    sortedTime = sorted(d.items(), key = lambda x: x[1][0])
    
    sortedTask = sorted(sortedTime, key = lambda x: x[1][1], reverse = True)
    
    names = []
    for item in sortedTask: 
        names.append(item[0])
    return names
       
        


if __name__ == '__main__':
    
    data = ["owen 2:00", "jeff 1:29", "owen 1:00", "jeff 1:30", "robert 0:21"]
    print(winners(data))