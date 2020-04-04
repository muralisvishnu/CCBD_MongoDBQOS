f=open("dopload20.txt","r")
lines=f.readlines()
data={}
for i in range(5):
    data[lines[1].split("[0;0m")[i]]=[]
for i in range(2,len(lines)-1):

    line=lines[i].split("|")
    datalist=list(filter(lambda a: a != "[0;0m", line[0].split()))
    k=0
    for j in data:
        data[j].append(datalist[k])
        k=k+1
print(data)