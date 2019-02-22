class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left :
                    self.left.insert(data)
                else:
                    self.left = node(data)
            elif data > self.data:
                if self.right :
                    self.right.insert(data)
                else:
                    self.right = node(data)
            else:
                self.data = data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def findval(self, number):
        if number < self.data:
            if not self.left:
                return "{0} not found".format(number)
            return self.left.findval(number)
        elif number > self.data:
            if not self.right:
                return "{0} not found".format(number)
            return self.right.findval(number)
        else:
            return "{0} is found".format(number)

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

    #Postorder Traversal : left => right => root
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.data)
        return res

root = node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))
print(root.findval(21))
print(root.findval(10))