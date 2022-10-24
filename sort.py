def write(n,f):
    li=[]
    for i in f:
        li.append(i.split()[n])
    return li


def sort1(n,f):
    li=[]
    for i in f:
        if n in i:
            li.append(i)
    return li    


