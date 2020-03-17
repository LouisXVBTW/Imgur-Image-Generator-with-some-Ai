from sightengine.client import SightengineClient
from tkinter import messagebox


client= SightengineClient('token', 'token')

count = 0

inc = 0
f=open('links.txt', 'r')
for line in f:
    client= SightengineClient(cid[inc], ckey[inc])
    if count < 143:
        link = str(line.replace('\n',''))
        print (link)
        try:
            
            output = client.check('nudity','offensive').set_url(link)

            if output['nudity']['safe'] <= output['nudity']['partial'] or output['offensive']['prob'] > .55:
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
        count += 1
    else:
        print ("Trial ran out")
        break


