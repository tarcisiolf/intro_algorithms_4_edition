array = [12, 3, 7, 9, 14, 6, 11, 2]


def merge(A, p, q, r):
    nl = q - p + 1
    nr = r - q

    L = [0] * nl
    R = [0] * nr

    for i in range(nl):
        L[i] = A[p+i]
    
    for j in range(nr):
        R[j] = A[q+j+1]
    
    i = j = 0
    k = p

    while i < nl and j < nr:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    while i < nl:
        A[k] = L[i]
        i += 1
        k += 1

    while j < nr:
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort(A, p, r):
    if p >= r: return

    q = (p+r)//2
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)


array_sorted = merge_sort(array, 0, len(array)-1)
print(array)