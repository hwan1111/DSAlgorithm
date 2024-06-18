def merge_sort(arr):
    # 배열의 길이가 1 이하이면 이미 정렬된 상태로 반환
    if len(arr) <= 1:
        return arr

    # 배열을 반으로 나눔
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 정렬된 배열을 병합
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # 두 배열을 비교해 작은 요소를 배열에 추가
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 남은 요소 추가
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
