import os
from subprocess import Popen,call
#Popen("powershell putty.exe root@10.230.25.106 -pw vizarchsai123!@# -m C:\Users\Administrator\Desktop\cmd.txt")
#call('start /wait ssh root@10.230.25.106 python bb.py -pw vizarchsai123!@# -m C:\Users\Administrator\Desktop\cmd.txt', shell=True)
#call('start /wait ssh root@10.230.25.106 python3 bb.py', shell=True)
#call('start /wait plink.exe -ssh root@10.230.25.106 -P 22 -pw vizarchsai123!@# -m C:\Users\Administrator\Desktop\cmd.txt', shell=True)
#call('start /wait plink.exe -ssh root@10.230.25.106 -P 22 -pw vizarchsai123!@# -m C:\Users\Administrator\Desktop\cmd.txt', shell=True)
import threading 
# mongod --shardsvr --replSet srs3  --dbpath /var/lib/mongodb/srs --bind_ip_all --port 27017
# mongod --configsvr --replSet cf  --dbpath /var/lib/mongodb/crs-1 --bind_ip_all --port 27017
# mongos --configdb cf/10.230.25.98:27017,10.230.25.98:27018,10.230.25.98:27019 --bind_ip_all --port 27020 
def print_cube(ipaddress,name):
    call('start /wait plink.exe -ssh root@'+ipaddress+' -P 22 -pw vizarchsai123!@# sudo kill -9 $(sudo lsof -t -i:27017)', shell=True)
    # call('start /wait plink.exe -ssh root@'+ipaddress+' -P 22 -pw vizarchsai123!@# sudo apt-get install dstat -y', shell=True)
    # print(ipaddress,name)
def crun(ipaddress,file,port):
    call('start /wait plink.exe -ssh root@'+ipaddress+' -P 22 -pw vizarchsai123!@# sudo kill -9 $(sudo lsof -t -i:'+port+')',shell=True)
    # print(ipaddress,file,port)
def mongosrun():
    call('start /wait plink.exe -ssh root@10.230.25.98 -P 22 -pw vizarchsai123!@# sudo kill -9 $(sudo lsof -t -i:27020)',shell=True)
if __name__ == "__main__": 
    ipaddress=["10.230.25.99","10.230.25.100","10.230.25.101","10.230.25.102","10.230.25.103","10.230.25.104","10.230.25.105","10.230.25.106","10.230.25.107"] 
    c=0
    l=[]
    for i in ipaddress:
        if(c//3==0):
            print(c)
            l.append(threading.Thread(target=print_cube, args=(i,"srs1")))
            c=c+1
            continue
        if(c//3==1):
            l.append(threading.Thread(target=print_cube, args=(i,"srs2")))
            c=c+1
            continue
        if(c//3==2):
            l.append(threading.Thread(target=print_cube, args=(i,"srs3")))
            c=c+1
            continue  
    t1=threading.Thread(target=crun, args=("10.230.25.98","crs-1","27017"))
    t2=threading.Thread(target=crun, args=("10.230.25.98","crs-2","27018"))
    t3=threading.Thread(target=crun, args=("10.230.25.98","crs-3","27019"))
    t4=threading.Thread(target=mongosrun)
    for i in l:
        i.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    for i in l:
        i.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("Done!") 