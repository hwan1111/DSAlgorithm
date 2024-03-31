# 노드(SNode): 데이터(data), 후(next)
class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None
# 단순 연결 리스트
class SingleLinkedList:
    #생성자
    def __init__(self):
        self.head = None
    # 빈 리스트 판단 여부
    def isEmpty(self):
        return self.head == None
    # 탐색: 노드의 총 개수
    def countNode(self) -> int:
        if self.isEmpty(): return 0
        count = 0
        rNode = self.head
        while rNode:
            count += 1
            rNode = rNode.next
        return count
    # 탐색: 첫 번째 노드
    def frontNode(self) -> SNode:
        if self.isEmpty(): return None
        return self.head
    # 탐색: 마지막 노드
    def rearNode(self) -> SNode:
        if self.isEmpty(): return None
        rNode = self.head
        while rNode.next:
            rNode = rNode.next
        return rNode
    # 삽입 (마지막에 삽입)
    def append(self, data):
        new_node = SNode(data)
        # 빈 리스트이면 생성
        if self.head is None:
            self.head = new_node
        else:
            rNode = self.head
            while rNode.next:
                rNode = rNode.next
            rNode.next = new_node
    # 삽입 (첫 번째에 삽입)
    def prepend(self, data):
        new_node = SNode(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    # 삽입 (prev_node뒤에 삽입)
    def insert_after(self, data, prev_node):
        if prev_node is None:
            print('Previous node must be in the linked list')
            return

        new_node = SNode(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    # 삭제 (node 삭제)
    def remove_node(self, node):
        if node is None:
            return

        if node == self.head:
            self.head = node.next
        else:
            rNode = self.head
            while rNode.next != node:
                rNode = rNode.next
            rNode.next = node.next
    # 출력
    def print_list(self):
        if self.isEmpty(): return
        current_node = self.head

        while current_node:
            print(f"{current_node.data} ->>", end=' ')
            current_node = current_node.next

        print()
    # 역방향 출력
    def revprint_list(self):
        if self.isEmpty(): return

        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

        current_node = self.head
        while current_node:
            print(f"{current_node.data} <<-", end=' ')
            current_node = current_node.next

        print()
