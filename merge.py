def mergeArr(a1,a2,n,m):
    a3 = [None]*(n+m)
    i = 0
    j = 0
    k = 0
    #traverse both arrays
    #if element of first array is less than store it in third array
    #if element of second array is less than store it in third array
    while i < n and j < m:
        if a1[i] < a2[i]:
            a3[k] = a1[i]
            k = k + 1
            i = i + 1
        else:
            a3[k] = a2[j]
            k = k + 1
            j = j + 1
    #if elements of first array are remaining
    #then transfer them to third array
    while i < n:
        a3[k] = a1[i]
        k = k + 1
        i = i + 1

    #if elementd