def merge_sort(A):
    l = len(A)
    mid = (int)(l/2)
    if l <= 1:
        return A
    left = A[:mid]
    right = A[mid:l]
    return merge(merge_sort(left), merge_sort(right))

def merge(L, R):
    B = []
    while len(L) > 0 and len(R) > 0:
        if L[0] < R[0]:
            B.append(L.pop(0))
        else:
            B.append(R.pop(0))
    if(len(L) > 0):
        B.extend(L)
    else:
        B.extend(R)
    return B
