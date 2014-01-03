lookup={}

def max_prod_cut(n):
    if lookup.has_key(n):
        return lookup[n]
    if n==1:
        return 1
    r=0
    for i in range(1,n):
        j = n-i
        a = max_prod_cut(i)
        if i>a:
            a = i
        b = max_prod_cut(j)
        if j>b:
            b = j
        c = a*b
        if c>r:
            r=c
    lookup[n]=r
    return r

print max_prod_cut(10)