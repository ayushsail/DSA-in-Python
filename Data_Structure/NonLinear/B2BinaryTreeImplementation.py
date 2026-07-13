class BinaryTree :
    def __init__(self,data=None) :
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)

    
    def add_left(self,child) :
        if not isinstance(child,BinaryTree  ) :
            raise Exception("Child must be a Binary TreeNode.")
        if child is self :
            raise ValueError("A node cannot be it's own child.")
        if child.parent is not None :
            raise ValueError("Node already has a parent.")
        
        if self.left is not None :
            raise ValueError("Left child already exists.")
        
        child.parent = self
        self.left = child

    def add_right(self,child) :
        if not isinstance(child,BinaryTree  ) :
            raise Exception("Child must be a Binary TreeNode.")
        if child is self :
            raise ValueError("A node cannot be it's own child.")
        if child.parent is not None :
            raise ValueError("Node already has a parent.")
        
        if self.right is not None :
            raise ValueError("Right child already exists.")
        
        child.parent = self
        self.right = child

    def remove_left(self) :
        if self.left is None :
            return None
        
        value = self.left
        value.parent = None
        self.left = None
        return value

    def remove_right(self) :
        if self.right is None :
            return None
        
        value = self.right
        value.parent = None
        self.right = None
        return value

    
if __name__ == "__main__" :
    root = BinaryTree(10)
    root.add_left(BinaryTree(5))
    root.add_right(BinaryTree(3))
    
    # print("removed :", root.remove_left())
    # print("removed :", root.remove_right())

















