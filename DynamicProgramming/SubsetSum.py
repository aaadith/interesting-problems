lookup={}

def subsetsum(a,sum,i):

    if lookup.has_key(i):
        return lookup[i]
    r = (a[i]==sum)
    if i==0:
        return r
    r = subsetsum(a,sum,i-1) or subsetsum(a, sum-a[i],i-1)
    return r


a=[2,3,4,5]
sum=9

print subsetsum(a,sum, len(a)-1)