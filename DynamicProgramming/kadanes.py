def maxsumsubarray(a):
    max_sum=0
    sum_so_far=0
    result_start, result_end=-1,-1

    for i in range(len(a)):

        t = a[i]+sum_so_far 

        if t>=0:
            sum_so_far = t
            if sum_so_far>max_sum:
                max_sum=sum_so_far
                result_end=i
        else:
            sum_so_far=0
            result_start=i

    if result_start==-1:
        result_start=0

    return a[result_start:result_end+1]
            
"r= maxsumsubarray([-2, -3, 4, -1, -2, 1, 5, -3])"

r = maxsumsubarray([1,2,-3,4])

print r
print sum(r)