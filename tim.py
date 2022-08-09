def tim(keyboard,st):
    l=list(keyboard)
    d={}
    x=[]
    s=0
    prev=0
    for i in range(0,len(l)):
        d[l[i]]=i
    for i in st:
        x.append(d[i])
    for i in range(0,len(x)):
        if i ==0:
            s+=x[i]
            prev=x[i]
        else:
            s+=abs(prev-x[i])
            prev=x[i]
    print(s)

tim("abcdefghijklmnopqrstuvwxy","cba")
