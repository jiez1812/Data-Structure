class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = TreeNode(data)
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = TreeNode(data)
        else:
            self.data = TreeNode(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

tree = TreeNode(52)
tree.insert(24)
tree.insert(75)
tree.insert(12)
tree.insert(96)
tree.insert(44)
tree.printTree()