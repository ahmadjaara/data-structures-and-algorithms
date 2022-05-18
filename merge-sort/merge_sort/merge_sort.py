
def Mergesort(arr):
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
        # sort the left side
        Mergesort(left)
        # sort the right side
        Mergesort(right)
        # merge the sorted left and right sides together
        Merge(left, right, arr)
    return arr

def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1

    # if i == len(left):
    #     set remaining entries in arr to remaining values in right
    # else:
    #     set remaining entries in arr to remaining values in left
    while i < len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j< len(right):
        arr[k]=right[j]
        j+=1
        k+=1


a=[8,4,23,42,16,15]
print(Mergesort(a))