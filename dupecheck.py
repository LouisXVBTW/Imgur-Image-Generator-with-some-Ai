f = open('testdouble.txt', 'r')
newlinks=[]
dupelinks=[]
for line in f:
    link = line.replace('\n','')
    if link not in newlinks:
        print ('link added')
        newlinks.append(link)
    else:
        dupelinks.append(link)
        print ('this link alread exists')


print (dupelinks)
        
    
