'''
Version 1.0: Created on Nov 16, 2015
Extensively Modified, 2.0: April 1, 2018

@author: ola
'''

import Replacements, TemplateChooser

def doWord(word):
    """
    word is a string
    if word is <tag>, find replacement
    and return it. Else return word
    """
    start = word.find("<")
    if start != -1:
        end = word.find(">")
        tag = word[start+1:end]
        
        rep = Replacements.getReplacement(tag)
        return rep
    return word

def linesToStory(lines):
    """
    lines is a list of strings,
    each a line from a template file
    Return a string based on substituting
    for each <tag> in each line
    """
    story = ""
    for line in lines:
        st = ""
        for word in line.split():
            st += doWord(word) + " "
        story += st.strip() + "\n"

    return story

def makeStory():
    """
    let user make a choice of
    available templates and print
    the story from the chosen template
    """
    lines = TemplateChooser.getTemplateLines("templates")
    st = linesToStory(lines)
    print(st)
    
if __name__ == '__main__':
    makeStory()
