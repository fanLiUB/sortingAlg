# max-heap

# returns index of the parent of element at index i
def parent(i):
    if i==0:
        return 0
    return (i-1)//2

# returns the index of the left child of element at index i
def left(i):
    return 2*i+1

# returns the index of the right child of element at index i
def right(i):
    return 2*i+2

# returns the size of heap A
def size(A):
    return len(A)

# heapify elements rooted from element at index i
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

# build a max heap from a list of elements
def build_max_heap(A):
    si = size(A)
    for i in range(si//2+1)[::-1]:
        max_heapify(A,i)

# sort list A using heapsort
def max_heap_sort(A):
    build_max_heap(A)
    si = size(A)
    B = []
    for i in range(si)[::-1]:
        B.insert(0,A[0])
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        A.remove(A[i])
        max_heapify(A,0)
    return B
