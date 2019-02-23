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

    #Inorder Traversal : left => root => right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)
        return res

    #Preorder Traversal : root => left => right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
        return res

    # Postorder Traversal : left => right => root
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.data)
        return res

tree = TreeNode(52)
tree.insert(24)
tree.insert(75)
tree.insert(12)
tree.insert(96)
tree.insert(44)
tree.insert(61)
tree.insert(33)
tree.insert(79)
print(tree.inorderTraversal(tree))
print(tree.preorderTraversal(tree))
print(tree.postorderTraversal(tree))