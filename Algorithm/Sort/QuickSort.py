def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left, right = [], []

    for i in range(len(arr)):
        if i == len(arr) // 2:
            continue
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quickSort(left) + [pivot] + quickSort(right)
