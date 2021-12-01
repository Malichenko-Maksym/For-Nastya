def f4(d):
    s=0
    for i in d:
        try:
            if d[i]>=5 and d[i]<=10:
                s+=d[i]
        except:
            for j in d[i]:
                if j>=5 and j<=10:
                    s=s+j
        
    return s
print(f4({"arr1":[2,6,-10],"arr2": -1 ,"arr3":[2,9,8,1]}))
    