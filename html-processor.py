#χρήση βιβλιοθήκης re
import re

#διάβασμα του αρχείου
with open('testpage.txt','r',encoding='utf-8') as fp:
 text=fp.read()

#εξαγωγή και εκτύπωση των τίτλων
 ptitle = '<title>(.+?)</title>'
 result = re.compile(ptitle)
 title = re.findall(result,text)
 print (title)
