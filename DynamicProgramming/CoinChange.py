lookup = {}

def coin_change(n):
    if lookup.has_key(n):
        return lookup[n]
    
    result = [[n]]
    
    for i in range(1,n):
        j = n-i
        if i <= j:
            a = coin_change(i)
            b = coin_change(j)
            c = get_combinations(a,b)
            for d in c:
                d = sorted(d)
                if d not in result:
                    result.append(d)
        
    lookup[n] = result
    return result


def get_combinations(a, b):
    result =[]
    for x in a:
        for y in b:
            c = x+y
            result.append(c)           
    return result


print coin_change(4)

