'''
Version 1.0, Created on Nov 15, 2015
Version 2.0, April 1, 2018

@author: ola
'''
import urllib.request,random,os,json

repd = {}

def getReplacement(tag):
    """
    return replacement for tag
    which is a string. If in the form
    <label>, then strip < and >
    if no replacements for label, 
    then return "NO-REPLACEMENT"
    else return a random replacement
    """
    global repd
    
    # read files to load global
    # dictionary if hasn't been read before
    
    if len(repd.keys()) == 0:
        readDirectory()
        
    # tag shouldn't have <>, but be safe
    
    if tag.startswith("<"):
        end = tag.find(">")
        tag = tag[1:end]
    
    
    if not tag in repd:
        tag = tag+'s'
        if not tag in repd:
            return "NO-REPLACEMENT"
      
    return random.choice(repd[tag])

def readAndStore(label,source):
    """
    label is a string, source is file of choices
    add label to global repd
    and read source to populate the
    entry for repd[label]
    """
    global repd
    f = open(source, encoding="utf-8")
    st = f.read()
    
    lines = st.split("\n")    
    if label not in repd:
        repd[label] = []
    for line in lines:
        if len(line) > 0:
            repd[label].append(line.strip())
    
    f.close()
    #print(label,repd[label])

def processFile(fname):
    """
    fname is a path: directory/filename
    where file is LABEL.txt, readAndStore this file
    with the tag: LABEL in global repd
    """
    head,tail = os.path.split(fname)
    dot = tail.find(".")
    label = tail[:dot]
    #print("readAndStore",head,label,tail)
    readAndStore(label,fname)

def readDirectory():
    """
    Read the folder "tagreplacements"
    and readAndStore each .txt file in that folder
    by calling processFile. This stores values
    in global dictionary repd
    """
    tagdir = "tagreplacements"
    data = os.listdir(tagdir)
    for d in data:
        processFile(os.path.join(tagdir,d))
        
    #print(repd)

def readjson():
    url = "http://www.cs.duke.edu/csed/tag-a-story/tags.json";
    f = urllib.request.urlopen(url)
    st = f.read().decode("utf-8")
    d = json.loads(st)
    f.close()
    return d

if __name__ == '__main__':

    d = readjson()
    readDirectory()

    print("sets of tags",set(d) == set(repd))
    for key in repd:
        if key not in d:
            print("key",key,"in files not json")
        else:
            js = set(d[key])
            ds = set(repd[key])
            print(key,"values are ==",js == ds)
            if js != ds:
                print("json",key,js)
                print("file",key,ds)
