import random
# quicksort

# partition array A into two parts based on a pivot
# takes on A, and the part of A to be sorted(A[low] to A[high])
# returns the index of the pivot
def partition(A,low,high):
    pivot = A[high-1]
    i = low-1
    for j in range(low,high-1):
        if A[j] <= pivot:
            i+=1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp2 = A[i+1]
    A[i+1] = pivot
    A[high-1] = temp2
    return i+1

# quicksort
def quicksort(A,low,high):
    if low < high:
        pivot_index = partition(A,low,high)
        quicksort(A,low,pivot_index)
        quicksort(A,pivot_index+1,high-1)
    

# a randomized quicksort

# randomly chooses a pivot before partitioning
def random_partition(A,low,high):
    pivot_index = random.randint(low,high-1)
    temp = A[pivot_index]
    A[pivot_index] = A[high-1]
    A[high-1] = temp
    return partition(A,low,high)

# randomized quicksort using randomized partition
def random_quicksort(A,low,high):
    if low < high:
        pivot_index = random_partition(A,low,high)
        random_quicksort(A,low,pivot_index)
        random_quicksort(A,pivot_index+1,high-1)
