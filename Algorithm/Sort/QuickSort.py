def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]    # 피벗 요소 선택
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + middle + quick_sort(right)

# in-place 정렬을 수행하는 퀵 정렬
def quick_sort_in_place(arr, low=0, high=None):
    # high가 None인 경우 배열의 마지막 인덱스로 설정
    if high is None:
        high = len(arr) - 1
    # 배열의 부분이 정렬될 필요가 있는 경우
    if low < high:
        pivot_index = partition(arr, low, high)     # partition함수를 사용해 피벗을 기준으로 배열을 분할
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]   # 마지막 요소를 피벗으로 선택
    i = low - 1     # 작은 요소의 인덱스를 설정
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
