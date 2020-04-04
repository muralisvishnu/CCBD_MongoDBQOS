data=open("dataset27019.csv","r")
train=open("train9.csv","w")
test=open("test9.csv","w")
dataline=data.readlines()
train.write(dataline[0])
test.write(dataline[0])
for i in dataline[1:int((0.8*len(dataline))//1)]:
    train.write(i)
for i in dataline[int((0.8*len(dataline))//1):]:
    test.write(i)