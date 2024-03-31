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

    # 인덱스로 노드 접근
    def __getitem__(self, index):
        if index < 0:
            index = self.countDNode() + index
            if index < 0:
                raise IndexError("Index out of range")

        current_node = self.head
        count = 0

        while current_node:
            if count == index:
                return current_node
            current_node = current_node.next
            count += 1
        raise IndexError("Index out of range")

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

    # 삽입 (인덱스 기반 접근, 데이터 기반 접근, 직접 위치 지정 기반 접근)
    def append(self, data, index=None, target_data=None, prev_node=None):
        new_node = DNode(data)

        # 모든 인자가 None인 경우 맨 마지막 삽입
        if index is None and target_data is None and prev_node is None:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                return
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
        # index가 None이 아닌 경우 index위치에 삽입
        elif index is not None:
            if index < 0:
                index = self.countDNode() + index
                if index < 0:
                    raise IndexError("Index out of range")
            elif index > self.countDNode():
                raise IndexError("Index out of range")
            elif index == 0:
                self.prepend(data)
            elif index == self.countDNode() - 1:
                self.append(data)
            else:
                prev_node = self[index - 1]
                self.append(data, prev_node=prev_node)
        # target_data가 None이 아닌 경우 해당 데이터 뒤에 삽입
        elif target_data is not None:
            current_node = self.head
            while current_node:
                if current_node.data == target_data:
                    new_node.prev = current_node
                    new_node.next = current_node.next

                    if current_node.next is not None:
                        current_node.next.prev = new_node
                    else:
                        self.tail = new_node

                    current_node.next = new_node
                    return
                current_node = current_node.next
            raise ValueError("Target data not found in the list")
        #prev_node가 None이 아닌 경우에는 prev_node 다음에 삽입
        elif prev_node is not None:
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

    # 삭제 (인덱스 기반 접근, 데이터 기반 접근, 직접 위치 지정 기반 접근)
    def pop(self, index=None, target_data=None, node=None):
        if self.isEmpty(): return
        # 인자가 모두 None이면 맨 마지막 노드 삭제
        if index is None and target_data is None and node is None:
            if self.tail is None:
                return
            else:
                node_to_remove = self.tail
                if self.head == self.tail:  # 리스트에 노드가 하나만 있는 경우
                    self.head = None
                    self.tail = None
                else:   # 리스트에 노드가 여러 개 있는 경우
                    self.tail = self.tail.prev
                    self.tail.next = None
                node_to_remove.prev = None
                return
        # index가 None이 아닌 경우 해당 인덱스의 노드 삭제
        elif index is not None:
            if index < 0:
                index = self.countDNode() + index
                if index < 0:
                    raise IndexError("Index out of range")
            elif index >= self.countDNode():
                raise IndexError("Index out of range")

            node_to_remove = self[index]

        # target_data가 None이 아닌 경우 해당 데이터를 가진 노드 삭제
        elif target_data is not None:
            current_node = self.head
            while current_node:
                if current_node.data == target_data:
                    node_to_remove = current_node
                    break
                current_node = current_node.next
            else:
                raise ValueError("Target data not found in the list")

        # node가 None이 아닌 경우 해당 노드 삭제
        elif node is not None:
            node_to_remove = node

        # 삭제할 노드가 리스트의 맨 앞에 있는 경우
        if node_to_remove == self.head:
            self.head = node_to_remove.next
            if self.head is not None:
                self.head.prev = None
            else:   # 리스트에 노드가 하나밖에 없는 경우
                self.tail = None
        # 삭제할 노드가 리스트의 맨 끝에 있는 경우
        elif node_to_remove == self.tail:
            self.tail = node_to_remove.prev
            self.tail.next = None
        # 삭제할 노드가 리스트의 중간에 있는 경우
        else:
            node_to_remove.prev.next = node_to_remove.next
            node_to_remove.next.prev = node_to_remove.prev

        # 삭제된 노드의 연결을 끊는 작업
        node_to_remove.prev = None
        node_to_remove.next = None

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
