import os
from subprocess import Popen,call
#Popen("powershell putty.exe root@10.230.25.106 -pw vizarchsai123!@# -m C:\Users\Administrator\Desktop\cmd.txt")
#call('start /wait ssh root@10.230.25.106 python bb.py -pw vizarchsai123!@# -m C:\Users\Administrator\Desktop\cmd.txt', shell=True)
#call('start /wait ssh root@10.230.25.106 python3 bb.py', shell=True)
#call('start /wait plink.exe -ssh root@10.230.25.106 -P 22 -pw vizarchsai123!@# -m C:\Users\Administrator\Desktop\cmd.txt', shell=True)
#call('start /wait plink.exe -ssh root@10.230.25.106 -P 22 -pw vizarchsai123!@# -m C:\Users\Administrator\Desktop\cmd.txt', shell=True)
import threading   
def print_cube(ipaddress,file):
    call('start /wait plink.exe -ssh root@'+ipaddress+' -P 22 -pw vizarchsai123!@# source ./shfiles/'+file, shell=True)
    #call('start /wait plink.exe -ssh root@'+ipaddress+' -P 22 -pw vizarchsai123!@# sudo apt-get install dstat -y', shell=True)
    #print(ipaddress,file)   
if __name__ == "__main__": 
    ipaddress=["10.230.25.99","10.230.25.100","10.230.25.101","10.230.25.102","10.230.25.103","10.230.25.104","10.230.25.105","10.230.25.106","10.230.25.107"] 
    c=0
    l=[]
    for i in ipaddress:
        if(c==0):
            print(c)
            l.append(threading.Thread(target=print_cube, args=(i,"d.sh")))
            l.append(threading.Thread(target=print_cube, args=(i,"thiswontwork.sh")))
            l.append(threading.Thread(target=print_cube, args=(i,"m7.sh")))
            l.append(threading.Thread(target=print_cube, args=(i,"mt7.sh")))
            c=c+1
            continue
        if(c==1):
            l.append(threading.Thread(target=print_cube, args=(i,"d.sh")))
            l.append(threading.Thread(target=print_cube, args=(i,"thiswontwork.sh")))
            l.append(threading.Thread(target=print_cube, args=(i,"m8.sh")))
            l.append(threading.Thread(target=print_cube, args=(i,"mt8.sh")))
            c=c+1
            continue
        if(c==2):
            l.append(threading.Thread(target=print_cube, args=(i,"d.sh")))
            l.append(threading.Thread(target=print_cube, args=(i,"thiswontwork.sh")))
            l.append(threading.Thread(target=print_cube, args=(i,"m9.sh")))
            l.append(threading.Thread(target=print_cube, args=(i,"mt9.sh")))
            c=0
            continue  
    for i in l:
        i.start()
    for i in l:
        i.join() 
    print("Done!") 