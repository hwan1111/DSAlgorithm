def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
# 수정(향상)된 버블 정렬 알고리즘
def betterbubbleSort(arr):
    for i in range(len(arr) - 1):
        state = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                state = False
        if state is True:  # 교환이 발생하지 않으면 정렬 완료
            break
    return arr
