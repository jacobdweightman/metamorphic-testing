def kth_occurrence(x, k, A):
    '''
    Searches an unsorted iterable A for the kth occurrence of x. Returns the
    index of this occurrence if there is one, or -1 otherwise.
    '''
    count = 0

    for i in range(len(A)):
        if A[i] == x:
            count += 1
            if count == k:
                return i
    return -1
