def bubble_sort(arr):
    """
    Arguments : it takes an array of length n

    purpose : it sorts an array

    return  : a sorted array
    """
    n = len(arr)

    for i in range(n):
        for j in range(n-1):
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

a = [5,4,3,2,1]
res = bubble_sort(a)
print(res)
