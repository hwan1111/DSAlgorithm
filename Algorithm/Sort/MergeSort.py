def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # 배열의 중간지점
        left = arr[:mid]    # 배열의 왼쪽
        right = arr[mid:]   # 배열의 오른쪽

        mergeSort(left)     # 반쪽 정렬
        mergeSort(right)    # 반쪽 정렬

        i = j = k = 0

        # 현재 배열을 L[]와 R[]로 복사
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr
