def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]   # 정렬되지 않은 배열의 첫 번째 요소를 저장
        j = i-1
        # 정렬된 배열의 요소와 비교하여 삽입할 위치를 찾음
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]   # 현재 요소를 오른쪽으로 이동
            j -= 1              # 삽입할 위치를 찾기 위해 인덱스를 감소시킴
        arr[j+1] = temp     # 저장된 요소를 올바른 위치에 삽입

    return arr
