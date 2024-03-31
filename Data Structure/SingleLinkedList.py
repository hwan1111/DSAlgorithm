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
        self.tail = None

    # 인덱스로 노드 접근
    def __getitem__(self, index):
        if index < 0:
            index = self.countSNode() + index
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
    
    # 빈 리스트 판단 여부
    def isEmpty(self):
        return self.head == None

    # 탐색: 노드의 총 개수
    def countSNode(self) -> int:
        if self.isEmpty(): return 0
        count = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            count += 1  
        return count

    # 탐색: 첫 번째 노드
    def frontSNode(self) -> SNode:
        if self.isEmpty(): return None
        return self.head

    # 탐색: 마지막 노드
    def rearSNode(self) -> SNode:
        if self.isEmpty(): return None
        return self.tail

    # 삽입 (인덱스 기반 접근, 데이터 기반 접근, 위치 직접 지정 기반 접근(전 노드))
    def append(self, data, index=None, target_data=None, prev_node=None):
        new_node = SNode(data)
        # 모든 인자가 None인 경우 맨 마지막에 삽입
        if index is None and target_data is None and prev_node is None:
            if self.isEmpty():  #빈 리스트인 경우
                self.head = new_node
                self.tail = new_node
                return
            else:
                self.tail.next = new_node
                self.tail = new_node
        
        # index가 None이 아닌 경우 index위치에 삽입
        elif index is not None:
            if index < 0:
                index = self.countSNode() + index
                if index < 0:
                    raise IndexError("Index out of range")
                elif index == 0:
                    self.prepend(data)
                elif index == self.countSNode() - 1:
                    self.append(data)
                else:
                    prev_node = self[index]
                    self.append(data, prev_node=prev_node)
            elif index >= self.countSNode():
                raise IndexError("Index out of range")
            elif index == 0:
                self.prepend(data)
            elif index == self.countSNode() - 1:
                self.append(data)
            else:
                prev_node = self[index - 1]
                self.append(data, prev_node=prev_node)
        
        # target_data가 None이 아닌 경우
        elif target_data is not None:
            current_node = self.head
            while current_node:
                if current_node.data == target_data:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    if current_node == self.tail:
                        self.tail = new_node
                    return
                current_node = current_node.next
            raise ValueError("Target data not found in the list")

        # prev_node가 None이 아닌 경우에는 prev_node 다음에 삽입
        elif prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node

            if new_node.next is None:
                self.tail = new_node
        
    # 삽입 (첫 번째에 삽입)
    def prepend(self, data):
        new_node = SNode(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # 삭제  (인덱스 기반 접근, 데이터 기반 접근, 직접 위치 지정 기반 접근)
    def pop(self, index=None, target_data=None, node=None):
        if self.isEmpty(): return

        # 인자가 모두 None이면 맨 마지막 노드 삭제
        if index is None and target_data is None and node is None:
            if self.tail is None:
                return
            else:
                node_to_remove = self.tail
                return

        # index가 None이 아닌 경우 해당 인덱스의 노드 삭제
        elif index is not None:
            if index < 0:
                index = self.countSNode() + index
                if index < 0:
                    raise IndexError("Index out of range")
            elif index >= self.countSNode():
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
            self.head = self.head.next
            if self.head is None:   # 리스트에 노드가 하나인 경우
                self.tail = None

        # 삭제할 노드가 리스트의 맨 끝에 있는 경우
        elif node_to_remove == self.tail:
            if self.tail == self.head:  #  리스트에 노드가 하나인 경우
                self.head = None
                self.tail = None
            else:   # 리스트에 노드가 여러 개인 경우 tail을 갱신하기 위해 탐색을 진행해야한다.
                current_node = self.head
                while current_node:
                    if current_node.next == self.tail:
                        self.tail = current_node
                        self.tail.next = None
                        break
                    currnet_node = current_node.next

        # 삭제할 노드가 리스트의 중간에 있는 경우
        else:
            current_node = self.head
            while current_node:
                if current_node.next == node_to_remove:
                    current_node.next = current_node.next.next
                    if current_node.next is None:   # 삭제한 노드가 tail인 경우
                        self.tail = current_node
                    break
                current_node = current_node.next
        
        node_to_remove.next = None

    # 출력
    def printSLinkedList(self):
        if self.isEmpty():
            return
        current_node = self.head

        while current_node:
            if current_node != self.head:
                print(' ->>', end=' ')
            print(f"{current_node.data}", end='')
            current_node = current_node.next
        print()
