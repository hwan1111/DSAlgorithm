class Chaining:
    class SNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, n=10):
        self._table = [None for _ in range(n)]

    def _hash(self, key):
        return sum(ord(char) for char in key) % len(self._table)

    def insert(self, key):
        new_node = self.SNode(key)
        slot = self._hash(key)
        if self._table[slot] is None:
            # 슬롯이 비어있다면, 새로운 노드를 삽입
            self._table[slot] = new_node
        else:
            # 슬롯에 충돌이 있으면, 연결 리스트의 끝에 추가
            current_node = self._table[slot]
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def delete(self, key):
        slot = self._hash(key)
        current_node = self._table[slot]
        prev_node = None

        while current_node:
            if current_node.data == key:
                if prev_node is None:
                    # 삭제하려는 노드가 첫 번째 노드인 경우
                    self._table[slot] = current_node.next
                else:
                    # 중간 또는 끝 노드 삭제
                    prev_node.next = current_node.next
                return key  # 삭제된 키 반환
            prev_node = current_node
            current_node = current_node.next

        return None  # 키가 없으면 None 반환

    def search(self, key):
        slot = self._hash(key)
        current_node = self._table[slot]

        while current_node:
            if current_node.data == key:
                return key  # 찾은 키 반환
            current_node = current_node.next

        return None  # 키가 없으면 None 반환

    def output(self):
        for i in range(len(self._table)):
            print(f'{i:3}', end = '')
            current_node = self._table[i]
            while current_node :
                print(f' --> {current_node.data}', end='')
                current_node = current_node.next
            print('')

if __name__ == '__main__':
    hash_table = Chaining()
    hash_table.insert('kim')
    hash_table.insert('lee')
    hash_table.insert('park')
    print(f"Search 'lee': {hash_table.search('lee')}")  # "lee" 출력
    print(f"Search 'choi': {hash_table.search('choi')}")  # None 출력
    hash_table.delete('kim')
    print(f"Search 'kim': {hash_table.search('kim')}")  # None 출력
    hash_table.output()
