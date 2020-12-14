import collections

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class solution(object):

    def levelorder(self, root):

        if root is None:
            return []

        result = []
        q = collections.deque([root])
        while len(q) != 0:
            numnodes = len(q)
            temp = []
            for _ in range(numnodes):
                node = q.popleft()
                temp.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            result.append(temp)

        return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

sol = solution()
print(sol.levelorder(root))

