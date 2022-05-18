# merge Sort

merge sort is a simple sorting algorithm that assort an array element in ascending  manner

## Pseudocode

    ALGORITHM Mergesort(arr)
        DECLARE n <-- arr.length

        if n > 1
        DECLARE mid <-- n/2
        DECLARE left <-- arr[0...mid]
        DECLARE right <-- arr[mid...n]
        // sort the left side
        Mergesort(left)
        // sort the right side
        Mergesort(right)
        // merge the sorted left and right sides together
        Merge(left, right, arr)

    ALGORITHM Merge(left, right, arr)
        DECLARE i <-- 0
        DECLARE j <-- 0
        DECLARE k <-- 0

        while i < left.length && j < right.length
            if left[i] <= right[j]
                arr[k] <-- left[i]
                i <-- i + 1
            else
                arr[k] <-- right[j]
                j <-- j + 1

            k <-- k + 1

        if i = left.length
        set remaining entries in arr to remaining values in right
        else
        set remaining entries in arr to remaining values in left


## Tracing

sample array =[8,4,23,42,16,15]

![trace](picture/trace.png "trace")

as we see in the picture above the first thing the function do is to split the array to left and right array until it reach array with length 1

then in the merging sort function it will compare each element inside the array with other elment and sort it in ascending maner and combine them in one array 