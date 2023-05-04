from StackClass import Stack

def is_matched_html(raw):
    """Returns true if all HTML tags are properly matched, False otherwise"""

    S= Stack() # create a stack object which is empty per constructor
    j = raw.find('<') # find in line the character "<" if there is any

    while j != -1: 
        k= raw.find('>', j+1) #find the next character '>'

        # if k does not find ">" then k stays at -1 and returns false as there is no closing tag
        if k == -1:
            return False
        
        tag= raw[j+1 : k] #strip away < >

        #checks for opening tag
        if not tag.startswith('/'):
            S.push(tag) # pushes opening tag 
        else: #if it starts is / then it is a closing tag 
            if S.isEmpty(): #if stack is empty meaning there is not a  match tag for the opening tag
                return False
            
            if tag[1:] != S.pop():
                return False #mismatched delimeter
            
        j= raw.find('<', k+1) #find next opening tag to check if there is a closing tag 
    
    return S.isEmpty()