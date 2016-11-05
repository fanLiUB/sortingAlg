# counting sort

# counting sort does not require comparisons among input elements
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
