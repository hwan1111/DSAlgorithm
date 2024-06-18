def shell_sort(arr):
    gap = 1

    # 초기 간격 설정: 1, 4, 13, 40, 121, ...
    while gap < len(arr) // 3:
        gap = 3 * gap + 1

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            # gap 간격으로 떨어진 요소들을 삽입 정렬 방식으로 정렬
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # 간격을 줄임
        gap //= 3

    return arr
