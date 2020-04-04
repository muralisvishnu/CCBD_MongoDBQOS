'''
This file takes '_s behind primary ' from fullrop and puts into 2 csv files: for port 8 and 9
'''

f1= open("fullout1.txt")
f4= open("time1.txt")
f2=open("outs27018.csv",'w+')
f3=open("outs27019.csv",'w+')
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
                i=i+1
# for (i,j) in zip(d1,d2):
#     d1[i]=Average(d1[i])
#     d2[j]=Average(d2[j])
#     f2.write(i+","+str(d1[i])+"\n")
    # f3.write(j+","+str(d2[j])+"\n")
f1.close()
f2.close()
f3.close()
f4.close()