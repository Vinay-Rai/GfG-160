def getSecondLargest(arr):
    # Code Here
    if len(arr)<2:
        return -1
        
    maxi = float("-inf")
    second_maxi = float("-inf")
    n = len(arr)
    for i in range(n):
        if arr[i]> maxi:
            second_maxi = maxi
            maxi = arr[i]
        
        elif arr[i] > second_maxi and arr[i]<maxi:
            second_maxi = arr[i]
        
    if second_maxi == float("-inf"):
        return -1
    else:
        return second_maxi