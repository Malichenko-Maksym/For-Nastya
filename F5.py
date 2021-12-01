def f5(c):
    f=open('poem.txt')
    k=f.readlines()
    f.close
    
    s=0
    for line in k:
        if c  in line: s+=1
        if c.upper() in line: s+=1
    return s
print(f5("m"))
   