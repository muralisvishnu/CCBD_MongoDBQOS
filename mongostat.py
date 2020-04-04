import csv
f=open("m7.txt")
csvFile=open("m7.csv","a",newline='')
writer = csv.writer(csvFile)
data=f.readlines()
head=data[1].split()
writer.writerow(head)

#print(data[1][1])
for i in range(2,len(data)):
	m=[]

	data[i]=data[i].strip()
	l=data[i].split(" ")
	
	#print("ll========\n",l)
	if ("insert" not in l):
		for i in l:
			if i!="":
				m.append(i)
			
		#print("m=====\n",m)
		#print(len(m))
		writer.writerow(m)

csvFile.close()
f.close()



'''
from pandas import read_csv
df=read_csv("C:\\Users\\Abishek\\Documents\\SEM_5\\4_BD\\Project\\fianl\\try2.csv")

#manually deleted the time column



#removing *
df= df.replace(to_replace ='\*', value = '', regex = True) 
#emoving the % 
df_updated = df.replace(to_replace ='%', value = '', regex = True) 
  
# Print the updated dataframe 
print(df_updated) 
'''
	
	
#row = ['4', ' Danny', ' New York']'''