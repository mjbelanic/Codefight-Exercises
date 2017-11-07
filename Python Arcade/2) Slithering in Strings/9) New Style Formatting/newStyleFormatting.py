import re

def newStyleFormatting(s):
    s1 = re.sub('%%', '?', s)
    s2 = re.sub(r'%[bcedfgnosx]', '{}', s1) 
    s3 = s2.replace("?", "%")
    return(s3)