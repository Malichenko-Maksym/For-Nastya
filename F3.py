import re
def f3(t):
    k=re.findall('\d+',t)
    s=0
    for i in k:
        a=int(i)
        if 9<a<1000: s=s+a
    return s
z=input()
print(f3(z))