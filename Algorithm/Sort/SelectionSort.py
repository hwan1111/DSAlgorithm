def selectionSort(arr):
    for i in range(len(arr)):
        smIndex = i
        for j in range(i, len(arr)):
            if arr[smIndex] > arr[j]:
                smIndex = j

        arr[smIndex], arr[i] = arr[i], arr[smIndex]

    return arr
