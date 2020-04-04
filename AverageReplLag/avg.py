m8=open("dataset27018m.csv","r")
m9=open("dataset27019m.csv","r")
q8=open("dataset27018q.csv","r")
q9=open("dataset27019q.csv","r")
w8=open("dataset27018w.csv","r")
w9=open("dataset27019w.csv","r")
x8=open("dataset27018x.csv","r")
x9=open("dataset27019x.csv","r")
m8l=m8.readlines()
m9l=m9.readlines()
q8l=q8.readlines()
q9l=q9.readlines()
w8l=w8.readlines()
w9l=w9.readlines()
x8l=x8.readlines()
x9l=x9.readlines()
def avg(l):
    res=0
    for i in l:
        res=res+i
    return res*10/len(l)
def getlist(l,k):
    m=[]
    for i in l[1:]:
        i=i.split(",")
        m.append(int(i[k]))
    return m
print(avg(getlist(m8l,14)))
print(avg(getlist(m9l,15)))
print(avg(getlist(q8l,14)))
print(avg(getlist(q9l,15)))
print(avg(getlist(w8l,14)))
print(avg(getlist(w9l,15)))
print(avg(getlist(x8l,14)))
print(avg(getlist(x9l,15)))