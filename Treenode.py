class TreeNode: 
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def insert(self,value):
        if value < self.value :
            if self.left is None:
                self.left = TreeNode(value)
            else : 
                self.left.insert(value)
        else :
            if self.right is None:
                self.right= TreeNode(value)
            else : 
                self.right.insert(value)

    def find(self,value):
        if value < self.value:
            if self.left is None:
                return False
            return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.find(value)
        return True  # value == self.value

    def inorder(self):
        if self.left :
            self.left.inorder()
        print(self.value)
        if self.right : 
            self.right.inorder()

    def preorder(self):
        print(self.value)
        if self.left :
            self.left.preorder()
        if self.right : 
            self.right.preorder()
            
    
    def postorder(self):
        if self.left :
            self.left.postorder()
        if self.right : 
            self.right.postorder()
        print(self.value)

   
