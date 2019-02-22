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
    
tree = TreeNode(51)
tree.insert(45)
tree.insert(75)
tree.insert(13)
tree.insert(25)
tree.insert(66)
tree.insert(5)
tree.printTree()