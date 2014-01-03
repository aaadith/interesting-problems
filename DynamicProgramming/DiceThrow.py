"given n dice each having m faces, how many ways are there to get a sum of x when all of them all thrown at once"

lookup={}
def DiceThrow(d,n,m,sum):
    key = (d,n,sum)
    if lookup.has_key(key):
        return lookup[key]

    if d==n:
        if sum>0 and sum<=m:
            return 1
        else:
            return 0

    if sum<0:
        return 0
    c=0
    for i in range(1,m+1):
        c+=DiceThrow(d+1,n,m,sum-i)
    lookup[key]=c
    return c

print DiceThrow(1,3,4,5)