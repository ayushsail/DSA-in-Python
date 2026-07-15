from Data_Structure.Linear.A8QueueImplementation import QueueLL       # for BFS - Level Order

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

# ADD LEFT
    def add_left(self,child) :
        if not isinstance(child,BinaryTree  ) :
            raise Exception("Child must be a Binary TreeNode.")
        if child is self :
            raise ValueError("A node cannot be its own child.")
        if child.parent is not None :
            raise ValueError("Node already has a parent.")
        
        if self.left is not None :
            raise ValueError("Left child already exists.")
        
        child.parent = self
        self.left = child


# ADD RIGHT
    def add_right(self,child) :
        if not isinstance(child,BinaryTree  ) :
            raise Exception("Child must be a Binary TreeNode.")
        if child is self :
            raise ValueError("A node cannot be its own child.")
        if child.parent is not None :
            raise ValueError("Node already has a parent.")
        
        if self.right is not None :
            raise ValueError("Right child already exists.")
        
        child.parent = self
        self.right = child


# REMOVE LEFT
    def remove_left(self) :
        if self.left is None :
            return None
        
        value = self.left
        value.parent = None
        self.left = None
        return value


# REMOVE RIGHT
    def remove_right(self) :
        if self.right is None :
            return None
        
        value = self.right
        value.parent = None
        self.right = None
        return value


# DISPLAY
    def display(self,level=0) :
        
        if self.right :
            self.right.display(level+1)
        
        space = '     ' * level
        print(space + str(self.data))

        if self.left :
            self.left.display(level+1)
        

# FIND DATA
    def find(self,data) :
        if self.data == data : return self

        if self.left : 
            result = self.left.find(data)
            if result is not None : return result
        if self.right : 
            result = self.right.find(data)
            if result is not None : return result

        return None


# CONTAIN DATA - same like find(), just return True/False 
    def contains(self,data) : 
        return self.find(data) is not None

# IS ROOT
    def is_root(self) : 
        return self.parent is None
    
# IS LEAF
    def is_leaf(self) :
        return self.left is None and self.right is None 


# GET ROOT - return root form any node
    def get_root(self) :
        node = self
        while node.parent :
            node = node.parent
        return node


# GET LEVEL - level == No. of ancestor from root
    def get_level(self) :
        level = 0
        p = self.parent
        while p :
            level += 1
            p = p.parent
        
        return level


# GET HEIGHT - The number of edges in the longest path from that node to any leaf node.
    def get_height(self) :
        if self.is_leaf() :
            return 0
        left_height = 0
        right_height = 0
        if self.left :
            left_height = self.left.get_height()
        if self.right :
            right_height = self.right.get_height()
        
        return 1 + max(left_height,right_height)


# GET PATH - return path from node to the root
    def get_path(self) :
        node = self
        path = []
        while node :
            path.append(node.data)
            node = node.parent
        
        path.reverse()
        return " --> ".join(map(str, path))


# COUNT NODE - total number of nodes in the subtree rooted at the current node.
    def count_node(self) :
        count = 1
        if self.left :
            count += self.left.count_node()
        if self.right :
            count += self.right.count_node()
        return count
            

# COUNT LEAF NODE - total number of leaf nodes in the subtree rooted at the current node.
    def count_leaf_node(self) :
        count = 0
        if self.is_leaf() :
            return 1
        if self.left :
            count += self.left.count_leaf_node()
        if self.right :
            count += self.right.count_leaf_node()
        
        return count


# COUNT INTERNAL NODE - any node that is not a leaf, thus it also include root node
    def count_internal_node(self) :
        count = 1
        if self.is_leaf() :
            return 0
        if self.left :
            count += self.left.count_internal_node()
        if self.right :
            count += self.right.count_internal_node()
        
        return count
        

# DEPTH FIRST SEARCH(DFS) - INORDER, PREORDER, POSTORDER TRAVERSAL
# INORDER TRAVERSAL 
    def inorder_traversal(self) :   # L-N-R
        elements = []

        # visit left subtree
        if self.left :
            elements += self.left.inorder_traversal()
        
        # visit base node
        elements.append(self.data)

        # visit right subtree
        if self.right :
            elements += self.right.inorder_traversal()
        
        return elements


# PREORDER TRAVERSAL
    def preorder_traversal(self) :   # N-L-R
        elements = []

        # visit base node
        elements.append(self.data)

        # visit left subtree
        if self.left :
            elements += self.left.preorder_traversal()
        
        # visit right subtree
        if self.right :
            elements += self.right.preorder_traversal()
        
        return elements


# POSTORDER TRAVERSAL
    def postorder_traversal(self) :   # L-R-N
        elements = []

        # visit left subtree
        if self.left :
            elements += self.left.postorder_traversal()
        
        # visit right subtree
        if self.right :
            elements += self.right.postorder_traversal()
        
        # visit base node
        elements.append(self.data)
        return elements

    
# BREADTH FIRST SEARCH(BFS) - LEVEL ORDER
    def bfs_levelorder(self) :
        elements = []
        q = QueueLL()
        q.enqueue(self)
        while not q.isEmpty() :
            node = q.dequeue()
            elements.append(node.data)
            if node.left : 
                q.enqueue(node.left)
            if node.right : 
                q.enqueue(node.right)
        
        return elements
    

    

# CLEAR DETACH - it detach the subtree from root, subtree still exist
    def clear_detach(self) :       # detach subtree
        if self.is_root() : raise ValueError("Cannot detach the root node.")

        if self is self.parent.left :
            self.parent.left = None
        else :
            self.parent.right = None
        self.parent = None

        
# CLEAR DESTROY - it detach each node from their parent, subtree do not exist
    def clear_destroy(self) :       # destroy subtree
        # Destroy left subtree
        if self.left:
            self.left.clear_destroy()

        # Destroy right subtree
        if self.right:
            self.right.clear_destroy()

        # Detach from parent (if not root)
        if not self.is_root():
            if self is self.parent.left:
                self.parent.left = None
            else:
                self.parent.right = None

        # Remove all references
        self.parent = None
        self.left = None
        self.right = None

    
    
if __name__ == "__main__" :
    root = BinaryTree(10)
    root.add_left(BinaryTree(3))
    root.add_right(BinaryTree(5))

    root.find(3).add_left(BinaryTree(7))
    root.find(3).add_right(BinaryTree(9))

    root.find(5).add_left(BinaryTree(11))
    root.find(5).add_right(BinaryTree(13))

    root.find(7).add_left(BinaryTree(15))
    root.find(7).add_right(BinaryTree(17))

    root.find(9).add_left(BinaryTree(19))
    root.find(9).add_right(BinaryTree(21))

    root.find(11).add_left(BinaryTree(23))
    root.find(11).add_right(BinaryTree(25))

    root.find(13).add_left(BinaryTree(27))
    root.find(13).add_right(BinaryTree(29))

    print("Original Tree : \n")
    root.display()

    # # remove
    # print("\nremoved :", root.find(13).remove_left())   # removed 27
    # print("removed :", root.find(9).remove_right(),"\n")    # removed 21
    # root.display()


    # find()
    result = root.find(13)
    print(f"Found : {result}" if result else "Data Not Found !")
    result = root.find(0)
    print(f"Found : {result}" if result else "Data Not Found !")

    # contain()
    print(f"does {root} contains 30 :", root.contains(30))   # False
    print(f"does {root} contains 17 :", root.contains(17))   # True

    # is_root()
    print("5 is root :",root.find(5).is_root())   # False
    print("29 is root :",root.find(29).is_root())   # False
    print(f"{root} is root :",root.is_root())   # True

    # is_leaf()
    print(f"{root} is leaf node :", root.is_leaf())     # False
    print("3 is leaf node :",root.find(3).is_leaf())    # False
    print(f"{root.find(23)} is leaf node :",root.find(23).is_leaf())    # True

    # get_root()
    print(f"root of {root.find(19)} :", root.find(19).get_root())
    print(f"root of {root.find(23)} :", root.find(23).get_root())

    # get_level()
    print(f"level of {root.find(17)} :",root.find(17).get_level())
    print(f"level of {root.find(11)} :",root.find(11).get_level())
    print(f"level of {root.find(5)} :",root.find(5).get_level())
    print(f"level of {root} :",root.get_level())

    # get_height()
    print(f"height of {root.find(23)} :", root.find(23).get_height())
    print(f"height of {root.find(7)} :", root.find(7).get_height())
    print(f"height of {root.find(3)} :", root.find(3).get_height())
    print(f"height of {root} :", root.get_height())

    # get_path()
    print(f"path from {root.find(23)} :", root.find(23).get_path())
    print(f"path from {root.find(7)} :", root.find(7).get_path())

    # count_node()
    print(f"number of nodes from {root} :", root.count_node())
    print(f"number of nodes from {root.find(5)} :",root.find(5).count_node())
    print(f"number of nodes from {root.find(7)} :",root.find(7).count_node())
    print(f"number of nodes from {root.find(23)} :",root.find(23).count_node())
    
    # count_leaf_node()
    print(f"count of leaf nodes from {root} :", root.count_leaf_node())
    print(f"count of leaf nodes from {root.find(5)} :",root.find(5).count_leaf_node())
    print(f"count of leaf nodes from {root.find(7)} :",root.find(7).count_leaf_node())
    print(f"count of leaf nodes from {root.find(23)} :",root.find(23).count_leaf_node())

    # count_internal_node()
    print(f"count of internal nodes from {root} :", root.count_internal_node())
    print(f"count of internal nodes from {root.find(5)} :",root.find(5).count_internal_node())
    print(f"count of internal nodes from {root.find(7)} :",root.find(7).count_internal_node())
    print(f"count of internal nodes from {root.find(23)} :",root.find(23).count_internal_node())

    
    # DFS - INORDER, PREORDER, POSTORDER TRAVERSAL
    print("Inorder Traversal :", root.inorder_traversal())
    print("Preorder Traversal :", root.preorder_traversal())
    print("Postorder Traversal :", root.postorder_traversal())

    # BFS - LEVEL ORDER
    print("BFS Level Order :", root.bfs_levelorder())




    # clear()
    print("\nCLEAR TREE :\n")

    # CLEAR DETACH
    node = root.find(3)
    node.clear_detach()
    print("\nAfter removing 3 subtree :\n")
    root.display()     # Tree without 3 - subtree
    print("\nremoved subtree :\n")
    node.display()     # Detached subtree rooted at 3


    # # CLEAR DESTROY
    # node = root.find(3)
    # node.clear_destroy()
    # print("\nAfter removing 3 subtree :\n")
    # root.display()     # Tree without 3 - subtree
    # print("\nremoved subtree :\n")
    # node.display()     # Detached subtree rooted at 3 dosen't exist