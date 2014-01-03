lookup = {}

def WordBreak(str, dict):
    if lookup.has_key(str):
        return lookup[str]

    r = []

    if str in dict:
        r.append([str])

    n = len(str)
    for i in range(1,n):
        j=n-i

        a = WordBreak(str[:i], dict)
        b = WordBreak(str[i:], dict)

        if len(a)>0 and len(b)>0:
            c = get_combinations(a,b)
            for d in c:
                if d not in r:
                    r.append(d)
    lookup[str]=r
    return r



def get_combinations(a, b):
    result =[]
    for x in a:
        for y in b:
            c = x+y
            result.append(c)           
    return result




str="ilikesamsung"
dict = ["i","like", "samsung", "sam", "sung"]

print WordBreak(str,dict)
