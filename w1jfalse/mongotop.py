import csv
f=open("mt7.txt")
csvFile=open("mt7.csv","a",newline='')
writer = csv.writer(csvFile)
data=f.readlines()
head=data[0].split()
times=head[4]
head.pop()
head.append("time")

writer.writerow(head)


for i in range(1,len(data)):
	m=[]
	data[i]=data[i].strip()
	l=data[i].split(" ")
	
	for j in l:
		if j !='':
			m.append(j)

	#print(l)
	#print(m)
	
	if m and m[0]=="ns":
		times=m[4]
		

	elif m:
		m.append(times)		
		#print("m=====\n",m)
		#print(len(m))
	
		writer.writerow(m)
	

csvFile.close()
f.close()	



