def f1(a):
    s=0
    for i in a:
        if i%2==0 and i>8:
            s+=1
    return s
k=[13,7,4,16,3,12,11]
print(f1(k))