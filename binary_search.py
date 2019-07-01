def binary_search_helper(x, A, i, j):
    '''
    Searches A for an element x using binary search. Returns the index of x if
    x is in A, or -1 if x is not in A.

    i is a lower bound on the index of x in A, and j is an upper bound on the
    index of x in A.
    '''
    if i > j:
        return -1

    mid = int((i + j) / 2)

    if A[mid] == x:
        return mid
    elif A[mid] > x:
        return binary_search_helper(x, A, i, mid-1)
    else:
        return binary_search_helper(x, A, mid+1, j)

def binary_search(x, A):
    '''
    A curried version of `binary_search_helper` that searches all of A.
    '''
    return binary_search_helper(x, A, 0, len(A))
