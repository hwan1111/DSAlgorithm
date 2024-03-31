def shellSort(arr):
    interval = len(arr)
    while interval >= 1:
        interval //= 2
        for i in range(interval):
            intervalSort(arr, i, interval)

    return arr

# 쉘 정렬에 쓰이는 삽입 정럴: interval 간격만큼 삽입 정렬
def intervalSort(arr, start:int, interval:int):
    for i in range(start, len(arr), interval):
        temp, j = arr[i], i - interval
        while j >= 0 and temp < arr[j]:
            arr[j+interval] = arr[j]
            j -= interval

        arr[j+interval] = temp
