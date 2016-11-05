# bucket sort
# input in range [0,1)

import math

# bucket_sort uses insertion_sort as a helper function
def insertion_sort(l):
    l1 = l
    for i in range(1, len(l1)):
        j = i-1
        while l1[i] < l1[j] and j >= 0:
            current = l1[i]
            l1[i] = l1[j]
            l1[j] = current
            i -= 1
            j -= 1
    return l1

def bucket_sort(A):
    B = [[-1]]*len(A)
    for i in range(len(A)):
        index = math.floor(10*(A[i]))
        if B[index] == [-1]:
            B[index] = [A[i]]
        else:
            B[index].append(A[i])
    A = []
    for i in range(len(B)):
        if (B[i] != [-1]):
            insertion_sort(B[i])
            A+=B[i]
    return A

