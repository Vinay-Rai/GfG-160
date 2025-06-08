#direct method 
def reverse(arr):
    return arr.reverse()


#coding way

def reversearray(arr):
    i = 0
    j = len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

print(reversearray([1, 4, 3, 2, 6, 5]))

