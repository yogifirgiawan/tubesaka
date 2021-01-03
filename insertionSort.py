# Function to perform insertion sort on list
def insertionSortIterative(A):
 
    # Start from the second element
    # (element at index 0 is already sorted)
    for i in range(1, len(A)):
 
        value = A[i]
        j = i
 
        # Find the index j within the sorted subset A[0..i-1]
        # where element A[i] belongs
        while j > 0 and A[j - 1] > value:
            A[j] = A[j - 1]
            j = j - 1
 
        # Note that sublist[j..i-1] is shifted to
        # the right by one position i.e. A[j+1..i]
 
        A[j] = value
def insertionSortRecursive(A, i):
 
    value = A[i]
    j = i
    # Find index j within the sorted subset A[0..i-1]
    # where element A[i] belongs
    while j > 0 and A[j - 1] > value:
        A[j] = A[j - 1]
        j = j - 1
 
    A[j] = value
 
    # Note that sublist[j..i-1] is shifted to
    # the right by one position i.e. A[j+1..i]
 
    if i + 1 < len(A):
        insertionSort(A, i + 1)
    print(A)