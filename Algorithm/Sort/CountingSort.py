def counting_sort(arr):
    # 최대값 찾기
    max_element = max(arr)

    # 카운트 배열 생성
    counts = [0] * (max_element + 1)

    # 각 요소의 카운트
    for i in range(len(arr)):
        counts[arr[i]] += 1

    # 누적 카운트
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    # 출력 배열 생성
    output = [0] * len(arr)

    # 정렬
    i = len(arr) - 1
    while i >= 0:
        output[counts[arr[i]] - 1] = arr[i]
        counts[arr[i]] -= 1
        i -= 1

    # 입력 배열에 결과 복사
    for i in range(len(arr)):
        arr[i] = output[i]

    return arr
