dop=open("dop.csv","r")
check=open("checkload.csv")
m7=open("m7new.csv","r")
mx=open("m9new.csv","r")
mt7=open("mtnew7.csv","r")
mtx=open("mtnew9.csv","r")
dataset=open("dataset127019.csv","w")
doplines=dop.readlines()
checklines=check.readlines()
m7lines=m7.readlines()
mxlines=mx.readlines()
mt7lines=mt7.readlines()
mtxlines=mtx.readlines()
dataset.write(doplines[0].strip()+checklines[0].strip()+","+m7lines[0].strip()+","+mt7lines[0].strip()+","+mxlines[0].strip()+","+mtxlines[0].strip()+"\n")
c=0
for i,j,k,l,m,n in zip(doplines[1:],checklines[1:],m7lines[1:],mt7lines[1:],mxlines[1:],mtxlines[1:]):
    dataset.write(i.strip()+","+j.strip()+","+k.strip()+","+l.strip()+","+m.strip()+","+n.strip()+"\n")
    # c=c+1
    # if(c>=4000):
    #     break
dataset.close()
print("Done!!")

dataset=open("dataset127019.csv","r")
dataset1=open("dataset27019.csv","w")
datasetlines=dataset.readlines()
dataset1.write(datasetlines[0])
for i in datasetlines[1:]:
    i=i.replace("M","e+6")
    i=i.replace("m","e+6")
    i=i.replace("G","e+9")
    i=i.replace("k","e+3")
    i=i.replace("B","")
    i=i.split(",")
    if("b" in i[37]):
        i[37]=str(int(i[37][:len(i[37])-1])/8)
    if("b" in i[38]):
        i[38]=str(int(i[38][:len(i[38])-1])/8)
    if("b" in i[77]):
        i[77]=str(int(i[77][:len(i[77])-1])/8)
    if("b" in i[37]):
        i[78]=str(int(i[78][:len(i[78])-1])/8)
    i=",".join(i)
    dataset1.write(i)
print("Done!!!")


