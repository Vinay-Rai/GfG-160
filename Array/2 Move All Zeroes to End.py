def pushZerosToEnd(arr):
    # code here
    n = len(arr)
    i=j=float("-inf")
    for k in range(n):
        if arr[k]==0:
            i = k
            j = i+1
            break
    if i == float("-inf"):
        return arr
    while j<n:
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i = i+1
            j=j+1
        else:
            j+=1
    return arr




#other way
