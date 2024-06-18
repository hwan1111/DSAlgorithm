# 연결 리스트에 대한 병합 정렬

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# 연결 리스트를 반으로 나누는 함수    
def split_list(head):
    if not head or not head.next:
        return head, None
    
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None
    return head, mid

# 두 정렬된 리스트를 병합하는 함수
def merge_list(l1, l2):
    dummy = Node()
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    
    tail.next = l1 if l1 else l2

    return dummy.next

# 병합 정렬을 수행하는 재귀함수
def merge_sort_recursive(head):
    if not head or not head.next:
        return head
    left, right = split_list(head)
    left = merge_sort_recursive(left)
    right = merge_sort_recursive(right)
    return merge_list(left, right)

# 연결 리스트 생성 및 사용 예시
def print_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print('None')


# 예시로 사용할 연결 리스트
nodes = [Node(12), Node(34), Node(54), Node(2), Node(3), Node(1), Node(23), Node(45), Node(67), Node(89), Node(78)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

head = nodes[0]
print("정렬 전 연결 리스트:")
print_list(head)

sorted_head = merge_sort_recursive(head)
print("정렬 후 연결 리스트:")
print_list(sorted_head)
