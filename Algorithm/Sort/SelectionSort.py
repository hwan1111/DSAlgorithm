def SelectionSort(arr):
    for i in range(len(arr)-1):
        k = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[k]:
                k = j

        arr[k], arr[i] = arr[i], arr[k]

    return arr
