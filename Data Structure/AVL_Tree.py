import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

class AVLNode:
    def __init__(self, data, height=1):
        self.data = data
        self.height = height
        self.left = None
        self.right = None

class AVL_Tree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        if node is None:
            return
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    # LL 불균형 -> RR 회전
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # 회전 실행
        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    # RR 불균형 -> LL 회전
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # 회전 실행
        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)

        return y

    def _rebalance(self, node):
        balance = self._balance_factor(node)

        if balance > 1:     # LL
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:    # RR
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert(self, node, data):
        if node is None:
            return AVLNode(data)

        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        else:
            return node

        self._update_height(node)
        return self._rebalance(node)

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._find_min(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)

        self._update_height(node)
        return self._rebalance(node)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.data] + self._inorder(node.right)

    def inorder(self):
        return self._inorder(self.root)

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

        plt.figure(figsize=(5, 5))
        pos = graphviz_layout(graph, prog='dot')
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color='lightblue',
                font_size=10, font_weight='bold', arrows=True)
        plt.show()

if __name__ == "__main__":
    avl = AVL_Tree()

    elements = [5, 17, 8, 42, 24]
    for elem in elements:
        avl.insert(elem)

    print("Inorder traversal after insertion:", avl.inorder())

    avl.visualize()

    avl.delete(42)

    print("Inorder traversal after deletion:", avl.inorder())

    avl.visualize()
