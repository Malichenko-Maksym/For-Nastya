#  f=open('people.csv')
#  k=f.readline()
import csv
def f6(g,n1,n2):
    f=open('people.csv')
    k=csv.reader(f)
    f.close
    s=0
    for i in k:
        try:
            a=int( i[2])
            if n1<=a<=n2 and i[3]==g:
                s+=1
        except: continue
    return s
print(f6("Female",160,180))