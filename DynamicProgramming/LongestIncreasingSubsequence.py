def longest_increasing_subsequence(a):
    prev=[None]
    seq_len=[1]
    for i in range(1,len(a)):
        prev_elem=None
        max_seq_len=1
        for j in range(i):
            if a[i]>a[j]:
                if seq_len[j]+1 > max_seq_len:
                    max_seq_len = seq_len[j]+1
                    prev_elem = j
        prev.append(prev_elem)
        seq_len.append(max_seq_len)
    return get_result(a, prev, seq_len)

def get_result(a, prev, seq_len):
    i=seq_len.index(max(seq_len))
    result = [a[i]]

    while prev[i]!=None:
        result.insert(0, a[prev[i]])
        i = prev[i]
    return result

print longest_increasing_subsequence( [ 10, 22, 9, 33, 21, 50, 41, 60 ])


