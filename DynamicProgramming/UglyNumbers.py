lookup={}

def get_nth_ugly(n):
    i=1
    c=1
    while i<n:
        c+=1
        if isUgly(c):
            i+=1
    return c




x=[2,3,5]
def isUgly(n):
    given_n=n
    if lookup.has_key(n):
        return lookup[n]
    for a in x:
        while n%a==0:
            n/=a
            if lookup.has_key(n):
                return lookup[n]
    lookup[given_n]=(n==1)
    return (n==1)


print get_nth_ugly(150)
print list(lookup.keys)