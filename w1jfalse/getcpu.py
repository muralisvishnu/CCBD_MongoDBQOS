f=open("dop.txt","r")
f1=open("dop.csv","w+")
lines=f.readlines()
data={}
titletext=""
for i in range(13):
    title=lines[2].split("[0;0m")[i].strip()
    if("|" in title):
        title=title[1:]
        title=title.strip()
    titletext=titletext+title+","
    data[title]=[]
f1.write(titletext+"\n")
for i in range(4,len(lines)-1):

    line=lines[i].split("|")
    line=" ".join(line)
    datalist=list(filter(lambda a: a != "[0;0m", line.split()))
    print(datalist)
    k=0
    for j in data:
        if("[0;0m" in datalist[k]):
            datalist[k]=datalist[k][6:]
        data[j].append(datalist[k].strip())
        
        k=k+1
    text=",".join(datalist)
    f1.write(text+"\n")
x=[]
# for i in range(data["usr"]):
    # x.append(i)
#plt.plot(x,data["usr"])
print(data)
f1.close()
