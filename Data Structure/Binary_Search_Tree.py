import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

class DNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LinkedBTree:
    def __init__(self):
        self.root = None

    def search(self, data):
        def _search(root, data):
            if root is None or data == root.data:
                return root.data if root else None
            elif data < root.data: return _search(root.left, data)
            else: return _search(root.right, data)

        _search(self.root, data)

    def search_unrecursive(self, data):
        if self.root is None:
            return

        temp_node = self.root
        while temp_node is not None:
            if temp_node.data == data:
                break
            elif data < temp_node.data:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        return temp_node.data

    def append(self, data):
        def _append(root, data):
            new_node = DNode(data)
            if root is None:
                root = new_node
            elif new_node.data < root.data:
                root.left = _append(root.left, new_node.data)
            else:
                root.right = _append(root.right, new_node.data)

            return root

        self.root = _append(self.root, data)

    def append_unrecursive(self, data):
        new_node = DNode(data)
        parent = None
        temp_node = self.root

        while temp_node is not None:
            if new_node.data == temp_node.data:
                raise IndexError('Value is already in Binary Tree')

            parent = temp_node
            if new_node.data < temp_node.data:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        if parent is None:
            self.root= new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, data):
        def _delete(node, data):
            if node is None:
                return None, False
            
            if data < node.data:
                node.left, deleted = _delete(node.left, data)
            elif data > node.data:
                node.right, deleted = _delete(node.right, data)
            else:   # 삭제할 노드를 찾았을때
                deleted = True
                # Case1: 자식노드 없을 때
                if node.left is None and node.right is None:
                    return None, deleted
                # Case2: 오른쪽 자식만 있을 때
                elif node.left is None: 
                    return node.right, deleted 
                # Case2: 왼쪽 자식만 있을 때
                elif node.right:
                    return node.left, deleted 
                # Case3: 두 자식이 있을 때
                else:
                    # 오른쪽 서브트리에서 최소값을 찾음
                    min_larger_node = self._find_min(node.right)
                    node.data = min_larger_node.data
                    node.right = _delete(node.right, min_larger_node.data)
            
            return node, deleted 
        
        self.root, deleted = _delete(self.root, data)

        if deleted:
            print(f"{data} 삭제 성공")
        else:
            print(f"{data} 트리에서 찾을 수 없음")

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete_unrecursive(self, data):
        stack = []
        current_node = self.root
        parent = None

        # 1. 삭제할 노드 탐색
        while current_node and current_node.data != data:
            stack.append((current_node, parent))
            parent = current_node
            if data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        # 노드가 존재하지 않는 경우
        if current_node is None:
            return

        # Case 1: 삭제할 노드가 리프 노드인 경우
        if current_node.left is None and current_node.right is None:
            if parent is None:  # 루트 노드인 경우
                self.root = None
            elif parent.left == current_node:
                parent.left = None
            else:
                parent.right = None

        # Case 2: 삭제할 노드가 자식 하나만 가진 경우
        elif current_node.left is None or current_node.right is None:
            child = current_node.left if current_node.left else current_node.right
            if parent is None:  # 루트 노드인 경우
                self.root = child
            elif parent.left == current_node:
                parent.left = child
            else:
                parent.right = child

        # Case 3: 삭제할 노드가 두 자식을 가진 경우
        else:
            # 후계자 찾기(오른쪽 서브트리의 최솟값)
            successor_parent = current_node
            successor = current_node.right
            while successor.left:
                stack.append((successor, successor_parent))
                successor_parent = successor
                successor = successor.left

            # 삭제할 노드에 후계자 데이터 복사
            current_node.data = successor.data

            # 후계자의 자식 노드 처리 (후계자가 오른쪽 자식을 가진 경우)
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.left

        while stack:
            node, parent = stack.pop()
            if parent and parent.left == node:
                parent.left = node
            elif parent and parent.right == node:
                parent.right = node

    def visualize(self):
        def add_edges(graph, node):
            if node is not None:
                if node.left:
                    graph.add_edge(node.data, node.left.data)
                    add_edges(graph, node.left)
                if node.right:
                    graph.add_edge(node.data, node.right.data)
                    add_edges(graph, node.right)

        graph = nx.DiGraph()

        add_edges(graph, self.root)

        plt.figure(figsize=(4, 3))
        pos = graphviz_layout(graph, prog='dot')
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color='lightblue',
                font_size=10, font_weight='bold', arrows=True)
        plt.show()

bt = LinkedBTree()

data_list = [10, 5, 15, 3, 7, 12, 18]
for data in data_list:
    bt.append(data)

bt.visualize()

bt.delete(10)

bt.visualize()
