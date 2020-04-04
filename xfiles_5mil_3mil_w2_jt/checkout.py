r=open("checkload.txt","r")
w=open("checkload.csv","w")
lines=r.readlines()
w.write("Start,repl8,repl9,rticket,wticket,ocursors,aconn,pf,memo,dd,bytescurrentused,readq,writeq\n")
for i in lines:
    i=i.split()
    i[5]=i[5][:(len(i[5])-1)]
    i[7]=i[7][:(len(i[7])-1)]
    w.write(",".join(i)+"\n")
r.close()
w.close()