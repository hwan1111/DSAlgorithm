# 노드(DNode): 데이터(data), 전(prev), 후(next)
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 이중 연결 리스트
class DoubleLinkedList:
    # 생성자
    def __init__(self):
        self.head = None    # 첫 번째 노드
        self.tail = None    # 마지막 노드
    
    # 빈 리스트 판단 여부 메서드
    def isEmpty(self):
        return self.head == None
    
    # 탐색: 노드의 총 개수(count)
    def countDNode(self) -> int:
        if self.isEmpty(): return 0
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next

        return count
    
    # 탐색: 첫 번째 노드
    def frontDNode(self):
        if self.isEmpty(): return None
        return self.head
    
    # 탐색: 마지막 노드
    def rearDNode(self):
        if self.isEmpty(): return None
        return self.tail
    
    # 삽입
    def insert(self, data, prev_node=None):
        new_node = DNode(data)
        if prev_node is None:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
        else:
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node

            if new_node.next is not None:
                new_node.next.prev = new_node
            else:
                self.tail = new_node
    
    # 삽입: 첫 번째 노드
    def prepend(self, data):
        new_node = DNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # 삭제
    def remove_node(self, node):
        if self.isEmpty() : return

        # 삭제할 노드가 리스트에 속하는지 확인
        if node not in self:
            raise ValueError("Node not found in the list")

        # 노드가 리스트에 하나만 남아 있는 경우
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # 삭제할 노드가 head인 경우
            if node == self.head:
                self.head = node.next
            # 삭제할 노드가 tail인 경우
            elif node == self.tail:
                self.tail = node.prev
            # 삭제할 노드가 중간에 위치한 경우
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

        # 삭제된 노드의 연결을 끊음
        node.prev = None
        node.next = None

    # 리스트의 전체 노드 출력
    def printDLinkedList(self):
        if self.isEmpty():
            return
        current_node = self.head

        while current_node:
            if current_node != self.head:
                print(' <<->>', end=' ')
            print(f"{current_node.data}", end='')
            current_node = current_node.next
        print()
