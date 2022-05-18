array1232488 =[8,4,23,42,16,15]

def insertionSort(arr):
    for i in range(1,len(arr)):
        print(i)
        temp=arr[i]
        j=i-1
        # print(j)
        
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            # print(arr[j+1])
            j=j-1
            # print(temp)
            arr[j+1]=temp
            # print(arr[j+1])
        
    return arr


def SelectionSort(arr):
    n = len(arr)
    for i in range(n): 
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j

        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr 


if __name__ == '__main__':
    print(insertionSort(array1232488))
    