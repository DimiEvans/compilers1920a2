#Παππά Δήμητρα Π2015015

#χρήση βιβλιοθήκης re
import re

#διάβασμα του αρχείου
with open('testpage.txt','r',encoding='utf-8') as fp:
 text=fp.read()

#εξαγωγή και εκτύπωση των τίτλων
  reTitle=re.compile('<title>(.+?)</title>')
  title=re.findall(reTitle,text)
  print(title)
  
 #Διαγραφή σχολίων
  reComment=re.compile('<!--(.*?)-->',re.DOTALL)
  text=reComment.sub(' ',text)
  
 #Διαγραφή script και style
  ScriptStyle=re.compile(r'<script(.*?)</script>|style='(.*?),re.DOTALL)
  text=ScriptStyle.sub(' ',text)
 
 #Ιδιότητα href
  href=re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)
  text=href.sub(' ',text)
  
 #Διαγραφή των ετικετών tags\
  tags=re.compile(r'<.+?>(.*?)</.+?>',re.DOTALL)
  text=tags.sub(' ',text)
  
 #Μετατροπή html entities
 def entities(m):    #Δημιουργία της function
    if m.group(0)=='&amp;': return '&'
    if m.group(0)=='&gt;': return '>'
    if m.group(0)=='&lt;': return '<'
    if m.group(0)=='&nbsp;': return ' '
  html=re.compile(r'&(amp|gt|lt|nbsp);')
  text=html.sub(entities,text)
