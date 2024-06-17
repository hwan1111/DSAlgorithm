def SelectionSort(arr):
    for i in range(len(arr)):
        k = i
        for j in range(i, len(arr)):
            if arr[k] > arr[j]:
                k = j

        arr[k], arr[i] = arr[i], arr[k]

    return arr
