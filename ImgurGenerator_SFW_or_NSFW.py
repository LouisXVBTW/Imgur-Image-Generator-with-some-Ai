import requests
import string
import random
from lxml.html import fromstring
from sightengine.client import SightengineClient
client= SightengineClient('token', 'token')



count = 0
while count != 300:

    link1 = "https://imgur.com/"
    rand1 = random.randint(5,7)
    linkid = ''.join(random.choices(string.ascii_letters + string.digits, k=rand1))
    flink1 = link1+linkid
    r1 = requests.get(flink1)
    tree1= fromstring(r1.content)
    title1=tree1.findtext('.//title')

    
    if title1 == "    Zoinks! You've taken a wrong turn.":
        pass
    else:
        flink1 +='.jpg'
        print (flink1)
        f=open('links.txt', 'a')
        flink1 +='\n'
        f.write(flink1)
        f.close()
        

f=open('links.txt', 'r')
for line in f:
    link = str(line.replace('\n',''))
    print (link)
    try:
        
        output = client.check('nudity','offensive').set_url(link)

        if output['nudity']['safe'] <= output['nudity']['partial'] or output['offensive']['prob'] > .85:
            print ('is NSFW added to NSFW.txt')
            f=open('NSFW.txt', 'a')
            link+='\n'
            f.write(link)
            f.close()
        else:
            print('SFW')
            f=open('SFW.txt', 'a')
            link+='\n'
            f.write(link)
            f.close()
    except:
        pass
    

        
    #print (title)
    #print (flink)
#<link rel="image_src" href="https://i.imgur.com/Dhhfl.jpg"/>
