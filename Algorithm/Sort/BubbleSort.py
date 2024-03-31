def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr
# 수정(향상)된 버블 정렬 알고리즘
def betterbubbleSort(arr):
    for i in range(lne(arr)):
        state = True
        for j in range(len(arr)-1, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                state = False

        if state:
            break

    return arr
