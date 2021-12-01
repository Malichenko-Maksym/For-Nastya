def  f2(a1,a2):
    s1=0
    for i in a1:
        if i>9 and i<100:
            s1+=1
    s2=0
    for i in a2:
        if i>9 and i<100:
            s2+=1
    if s1==s2: return True
    else: return False
print(f2([236,7,6,34],[1,18,744,2,6,111]) )