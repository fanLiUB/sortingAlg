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
