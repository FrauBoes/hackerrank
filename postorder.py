# Helper code @Hackerrank


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left
self.right
self.info
"""


def postOrder(root):
    if root is None:
        return None

    postOrder(root.left)
    postOrder(root.right)
    print(root.info, end=" ")


# Driver code
bst = BinarySearchTree()
t = 6
arr = [1,2,5,3,6,4]

for i in range(t):
    bst.create(arr[i])

postOrder(bst.root)


