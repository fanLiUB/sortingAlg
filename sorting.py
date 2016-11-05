import math
import random

# sorting by comparisons
# can't achieve better than O*log(O)

# insertion sort:
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

# merge-sort:
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

# heapsort:
# a: max-heap
def parent(i):
    return i//2-1

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def size(A):
    return len(A)

def max_heapify(A,i):
    l = left(i)
    r = right(i)
    largest = i
    si = size(A)
    if l>=0 and l<si and A[l] > A[i]:
        largest = l
    if r>=0 and r<si and A[r] > A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A,largest)

def build_max_heap(A):
    si = size(A)
    for i in range(si//2+1)[::-1]:
        max_heapify(A,i)

# b: heap-sort
def max_heapsort(A):
    build_max_heap(A)
    si = size(A)
    B = []
    for i in range(si)[::-1]:
        B.insert(0,A[0])
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        A = A[:-1]
        max_heapify(A,0)
    A = B
    return A

# not by comparisons

# counting sort
def counting_sort(A):
    m = max(A)+1
    C = [0]*m
    B = [0]*len(A)
    for i in range(len(A)):
        B[i] = A[i]
    for j in range(len(B)):
        C[B[j]] += 1
    for k in range(1,m):
        C[k] += C[k-1]
    for l in range(len(B))[::-1]:
        A[C[B[l]]-1] = B[l]
        C[B[l]] -= 1

# bucket sort
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
