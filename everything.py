
# coding: utf-8

# In[8]:


f1= open("C:\\Users\\Abishek\\Desktop\\CCBDmongoQoS\\fullout (2).txt")
#f4= open("C:\Users\Abishek\Desktop\CCBDmongoQoS\time1 (2).txt")
f2=open("C:\\Users\\Abishek\\Desktop\\CCBDmongoQoS\\outs27018_a.csv",'w+')
f3=open("C:\\Users\\Abishek\\Desktop\\CCBDmongoQoS\\outs27019_a.csv",'w+')
lines = f1.readlines()
str1="behind the primary"
str2="syncedTo:"
i=0
# d1={}
# d2={}
# def Average(lst):
#     if(len(lst)!=0): 
#         return sum(lst) / len(lst)
#     else:
#         return 0 
for line in range(len(lines)):
        if (i%2==0):
            f=f2
        else:
            f=f3
        if str1 in lines[line]:
                # if(lines[line].split()[5] in d ):
                    # d[lines[line].split()[5]].append(int(lines[line+1].split()[0]))
                # else:
                #     d[lines[line].split()[5]]=[]
                # d[lines[line].split()[5]].append(int(lines[line+1].split()[0]))
                f.write(lines[line].split()[0])  
                f.write("\n")
                i=i+1
# for (i,j) in zip(d1,d2):
#     d1[i]=Average(d1[i])
#     d2[j]=Average(d2[j])
#     f2.write(i+","+str(d1[i])+"\n")
    # f3.write(j+","+str(d2[j])+"\n")
f1.close()
f2.close()
f3.close()
#f4.close()


# In[9]:


##################################################################################
import csv
csvfile=open('C:\\Users\\Abishek\\Desktop\\CCBDmongoQoS\\outs27018_a.csv','r') 
f1=open("C:\\Users\Abishek\Desktop\CCBDmongoQoS\\time1 (2).txt")

f2=open("C:\\Users\\Abishek\\Desktop\\CCBDmongoQoS\\average27018_a.csv",'w+')

plots = csv.reader(csvfile, delimiter=',')
plots1 = f1.readlines()
x1=[]
y1=[]
d={}

def Average(lst):
    if(len(lst)!=0): 
        return sum(lst) / len(lst)
    else:
        return 0 

for row,row1 in zip(plots,plots1):
    if(row1[:8] in d ):
        d[row1[:8]].append(int(row[0]))
    else:
        d[row1[:8]]=[]
        d[row1[:8]].append(int(row[0]))
for i in d:
    d[i]=Average(d[i])
    f2.write(i+","+str(d[i])+"\n")


# In[10]:


###################
import matplotlib.pyplot as plt
f2=open("C:\\Users\\Abishek\\Desktop\\CCBDmongoQoS\\average27018_a.csv",'r')
plots = csv.reader(f2, delimiter=',')
x=[]
y=[]
for row in plots:
    x.append(row[0])
    y.append(float(row[1]))
#print(x,y)
plt.xlabel('timestamp')
plt.ylabel('Replication lag')

ax = plt.gca()
plt.xticks(rotation=60)

plt.rc('xtick',labelsize=0.5)
plt.rc('ytick',labelsize=8)

plt.plot(x,y, "o-",label='27018',markersize="0.05")
plt.show()
f2.close()

