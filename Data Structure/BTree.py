'''
    이진 트리(BT): 알고리즘 구현(Python) -- 이중연결리스트
        파일명: LinkedBTree.py
                - main: 데이터 삽입.삭제, 전체 원소 출력
            - 클래스: DNode
            - 클래스: LinkedBTree
                - 이진 트리 생성: makeLinkedBTree
                - 깊이 우선 순회: Preorder, Inorder, Postorder
                - 너비 우선 순회: Levelorder
'''

# 연산자 여부 판단
def isOperator(op):
    return op == '+' or op == '-' or op == '*' or op == '/'

class DNode:
    def __init__(self, data):
        self.data = data
        self.Llink = None
        self.Rlink = None

class LinkedBTree:
    def __init__(self):
        self.root = None

    def __del__(self):
        if self.root is None:
            return
        Queue = [self.root]
        while Queue:
            current_node = Queue.pop(0)
            if current_node.Llink is not None:
                Queue.append(current_node.Llink)
            if current_node.Rlink is not None:
                Queue.append(current_node.Rlink)
            del current_node
        self.root = None

    def makeLinkedBTree(self, postfix):
        Stack = []
        for token in postfix:
            current_node = DNode(token)
            if isOperator(token):
                current_node.Rlink = Stack.pop()
                current_node.Llink = Stack.pop()
            Stack.append(current_node)
        self.root = Stack.pop()
        return self.root

    # DFS: 전위 순회
    def Preorder(self):
        def _Preorder(node):
            if node is None:
                return
            print(node.data, end=' ')
            _Preorder(node.Llink)
            _Preorder(node.Rlink)
        _Preorder(self.root)
        print()

    # DFS: 중위 순회
    def Inorder(self):
        def _Inorder(node):
            if node is None:
                return
            _Inorder(node.Llink)
            print(node.data, end=' ')
            _Inorder(node.Rlink)
        _Inorder(self.root)
        print()

    # DFS: 후위 순회
    def Postorder(self):
        def _Postorder(node):
            if node is None:
                return
            _Postorder(node.Llink)
            _Postorder(node.Rlink)
            print(node.data, end=' ')
        _Postorder(self.root)
        print()

    # BFS: 레벨 순회
    def Levelorder(self):
        if self.root is None:
            return
        Queue = [self.root]
        while Queue:
            current_node = Queue.pop(0)
            print(current_node.data, end=' ')
            if current_node.Llink is not None:
                Queue.append(current_node.Llink)
            if current_node.Rlink is not None:
                Queue.append(current_node.Rlink)
        print()
