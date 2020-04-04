data=open("dataset27018.csv","r")
train=open("train.csv","w")
test=open("test.csv","w")
dataline=data.readlines()
train.write(dataline[0])
test.write(dataline[0])
for i in dataline[1:int((0.8*len(dataline))//1)]:
    train.write(i)
for i in dataline[int((0.8*len(dataline))//1):]:
    test.write(i)