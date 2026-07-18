from Data_Structure.Linear.A8QueueImplementation import QueueLL     # for BFS - LEVELORDER

class AVLTree :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0     # maintain height

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)


# DISPLAY
    def display(self,level=0) :
        if self.right : self.right.display(level+1)
        
        space = '        ' * level
        print(f"{space} {self.data} [{self.height}]")

        if self.left : self.left.display(level+1)


# UPDATE HEIGHT - Update height, after performing balancing operation,NOTE - this is not recursive
    def update_height(self) :
        left_height = right_height = -1    # if left,right subtree not exist, then -1 for left,right subtree.  
        if self.left : left_height = self.left.height
        if self.right : right_height = self.right.height
        
        self.height = 1 + max(left_height,right_height)


# GET BALANCE - returns balance of node, left_height - right_height, NOTE - this is not recursive
    def get_balance(self) :
        left_height = right_height = -1     # if left,right subtree not exist, then -1 for left,right subtree. 
        if self.left : left_height = self.left.height
        if self.right : right_height = self.right.height
        
        return left_height - right_height
    

# RIGHT ROTATE - if balance is  +2 or +1 - perform this rotation
    def right_rotate(self) :
        if self.left is None: raise ValueError("Right rotation not possible.")

        old_root = self
        new_root = old_root.left
        transfered_subtree = new_root.right

        # swap root
        new_root.right = old_root
        old_root.left = transfered_subtree

        parent = old_root.parent
        if parent:
            if old_root is parent.left:
                parent.left = new_root
            else:
                parent.right = new_root

        # updating parent of new_root, transfered_subtree & old_root
        new_root.parent = parent
        old_root.parent = new_root
        if transfered_subtree : transfered_subtree.parent = old_root

        # update height of all nodes
        old_root.update_height()
        new_root.update_height()

        return new_root
    

# LEFT ROTATE - if balance is  -2 or -1 - perform this rotation
    def left_rotate(self) :
        if self.right is None : raise ValueError("Left rotation not possible.")

        old_root = self
        new_root = old_root.right
        transfered_subtree = new_root.left

        # swapping root
        new_root.left = old_root
        old_root.right = transfered_subtree

        parent = old_root.parent
        if parent:
            if old_root is parent.right:
                parent.right = new_root
            else:
                parent.left = new_root

        # updating parent of new_root, transfered_subtree & old_root
        new_root.parent = parent
        old_root.parent = new_root
        if transfered_subtree : transfered_subtree.parent = old_root

        # update height of all nodes
        old_root.update_height()
        new_root.update_height()

        return new_root


# REBALANCE - Balance tree using Left and Right Rotate function
    def rebalance(self) :
        self.update_height()

        balance = self.get_balance()

        if balance > 1 :
            if self.left.get_balance() >= 0 :       # LL - case
                return self.right_rotate()
            
            else :                                  # LR - case
                self.left = self.left.left_rotate()
                return self.right_rotate()
        
        elif balance < -1 :
            if self.right.get_balance() <= 0 :      # RR - case
                return self.left_rotate()
            
            else :                                  # RL - case
                self.right = self.right.right_rotate()
                return self.left_rotate()
        
        return self


# INSERT
    def insert(self,data) :
        if self.data == data :  ValueError("Duplicate data")    # duplicate case

        elif data < self.data :
            # add data in left subree
            if self.left :  
                self.left = self.left.insert(data)
            else :
                node = AVLTree(data)
                node.parent = self
                self.left = node

        else :
            # add data in right subree
            if self.right :
                self.right = self.right.insert(data)
            else :
                node = AVLTree(data)
                node.parent = self
                self.right = node

        return self.rebalance()


# FIND MAX
    def find_max(self) :
        if self.right :
            return self.right.find_max()
        else :
            return self


# FIND MIN
    def find_min(self) :
        if self.left :
            return self.left.find_min()
        else :
            return self


# DELETE
    def delete(self,data) :
        if data < self.data :   # if data < self - search left subtree recursively
            if self.left : 
                self.left = self.left.delete(data)
            else : raise ValueError("Data Not Found !")

        elif data > self.data :     # if data > self - search right subtree recursively
            if self.right : 
                self.right = self.right.delete(data)
            else : raise ValueError("Data Not Found !")
        
        else :  # data = self.data

            # if self has no child - return None
            if self.right is None and self.left is None : 
                return None
            
            # if self has one child either left or right
            elif self.left is None :    # if self has no left child - return right child
                self.right.parent = self.parent
                return self.right
            
            elif self.right is None :   # if self has no right child - return left child
                self.left.parent = self.parent
                return self.left
            
            # if self has two child
            else : 
                # find min_val in right subtree or max_val in left subtree and replace it with self
                min_val = self.right.find_min()
                self.data = min_val.data
                self.right = self.right.delete(min_val.data)
    
        return self.rebalance()
    

# UTILITY FUNCTIONS
    def find(self,data) :
        if data == self.data : return self
        elif data < self.data : 
            if self.left : return self.left.find(data)
        elif data > self.data : 
            if self.right : return self.right.find(data)

        return None
    
    def contains(self,data) :
        return  self.find(data) is not None
    
    def is_root(self) :
        return self.parent is None
    
    def is_leaf(self) :
        return self.right is None and self.left is None
    
    def get_root(self) :
        node = self
        while node.parent :
            node = node.parent
        return node

    def get_level(self) :
        level = 0
        node = self
        while node.parent :
            level += 1
            node = node.parent
        return level
    
    def get_height(self) :
        return self.height
    
    def get_path(self) :
        path = []
        node = self
        while node :
            path.append(node.data)
            node = node.parent
        path.reverse()
        return " --> ".join(map(str,path))
    
    def count_node(self) :
        count = 1
        if self.left : count += self.left.count_node()
        if self.right : count += self.right.count_node()
        return count
    
    def count_leaf_node(self) :
        count = 0
        if self.is_leaf() : return 1
        if self.left : count += self.left.count_leaf_node()
        if self.right : count += self.right.count_leaf_node()
        return count
    
    def count_internal_node(self) :
        count = 1
        if self.is_leaf() : return 0
        if self.left : count += self.left.count_internal_node()
        if self.right : count += self.right.count_internal_node()
        return count
    

# TRAVERSAL FUNCTIONS
# DFS - INORDER,PREORDER,POSTORDER

    def inorder_traversal(self) :     # L - N - R
        elements = []

        # visit left subtree
        if self.left : elements += self.left.inorder_traversal()
        
        # visit Base Node
        elements.append(self.data)

        # visit right subtree
        if self.right : elements += self.right.inorder_traversal()

        return elements
    
    def preorder_traversal(self) :     # N - L - R
        elements = []

        # visit Base Node
        elements.append(self.data)

        # visit left subtree
        if self.left : elements += self.left.preorder_traversal()

        # visit right subtree
        if self.right : elements += self.right.preorder_traversal()

        return elements
    
    def postorder_traversal(self) :     # L - R - N
        elements = []

        # visit left subtree
        if self.left : elements += self.left.postorder_traversal()
        
        # visit right subtree
        if self.right : elements += self.right.postorder_traversal()

        # visit Base Node
        elements.append(self.data)

        return elements
    
    def bfs_levelorder(self) :
        elements = []
        q = QueueLL()
        q.enqueue(self)
        while not q.isEmpty() :
            node = q.dequeue()
            elements.append(node.data)
            if node.left : q.enqueue(node.left)
            if node.right : q.enqueue(node.right)
        
        return elements
    
# CLEAR() FUNCTIONS
    def clear_detach(self) :
        if self.is_root() : raise ValueError("Cannot detach the root node.")
        if self is self.parent.left : self.parent.left = None
        else : self.parent.right = None

        self.parent = None

    def clear_destroy(self) :
        if self.is_root() : raise ValueError("Cannot detach the root node.")
        if self.left : self.left.clear_destroy()
        if self.right : self.right.clear_destroy()
        if self is self.parent.left: self.parent.left = None
        else: self.parent.right = None

        # Remove all references
        self.parent = None
        self.left = None
        self.right = None



def build_tree(elements) :
    if not elements : return None

    root = AVLTree(elements[0])

    for element in elements[1:len(elements)]:
        root = root.insert(element)
    
    return root

if __name__ == "__main__" :
    print("\nAVL TREE IMPLEMENTATION\n")
    elements = [50,30,70,20,40,35,80,25,35,45,95,105,10]
    root = build_tree(elements)
    print("\nORIGINAL TREE :\n")
    root.display()
    print(f"Balance of root :{root.get_balance()}\n")


    # DELETE OPERATIONS
    print("\nDeleted : 80\n")
    root = root.delete(80)
    root.display()
    print(f"Balance of root :{root.get_balance()}\n")

    print("\nDeleted : 20\n")
    root = root.delete(20)
    root.display()
    print(f"Balance of root :{root.get_balance()}\n")

    print("\nDeleted : 10\n")
    root = root.delete(10)
    root.display()
    print(f"Balance of root :{root.get_balance()}\n")

    print("\nDeleted : 40\n")
    root = root.delete(40)
    root.display()
    print(f"Balance of root :{root.get_balance()}\n")

    print("\nDeleted : 35\n")
    root = root.delete(35)
    root.display()
    print(f"Balance of root :{root.get_balance()}\n")

    print("\nDeleted : 25\n")
    root = root.delete(25)
    root.display()
    print(f"Balance of root :{root.get_balance()}\n")


    # UTILITY OPERATION
    elements = [50,30,70,20,40,35,80,25,35,45,95,105,10]
    root = build_tree(elements)
    print("\nORIGINAL TREE :\n")
    root.display()
    print(f"Balance of root :{root.get_balance()}\n")

    # find_max() & find_min()
    print("Max :",root.find_max())
    print("Min :",root.find_min())

    # find()
    result = root.find(80)
    print(f"Found : {result}" if result else "Data Not Found !")
    result = root.find(0)
    print(f"Found : {result}" if result else "Data Not Found !")

    # contain()
    print(f"does root - {root} contains 30 :", root.contains(30))   # False
    print(f"does root - {root} contains 43 :", root.contains(43))   # True

    # is_root()
    print("10 is root :",root.find(10).is_root())   # False
    print("105 is root :",root.find(105).is_root())   # False
    print(f"{root} is root :",root.is_root())   # True

    # is_leaf()
    print(f"{root} is leaf node :", root.is_leaf())     # False
    print("50 is leaf node :",root.find(50).is_leaf())    # False
    print(f"{root.find(105)} is leaf node :",root.find(105).is_leaf())    # True

    # get_root()
    print(f"root of {root.find(35)} :", root.find(35).get_root())
    print(f"root of {root.find(50)} :", root.find(50).get_root())

    # get_level()
    print(f"level of {root} :",root.get_level())
    print(f"level of {root.find(30)} :",root.find(30).get_level())
    print(f"level of {root.find(50)} :",root.find(50).get_level())
    print(f"level of {root.find(25)} :",root.find(25).get_level())

    # get_height()
    print(f"height of {root.find(80)} :", root.find(80).get_height())
    print(f"height of {root.find(95)} :", root.find(95).get_height())
    print(f"height of {root.find(70)} :", root.find(70).get_height())
    print(f"height of {root} :", root.get_height())

    # get_path()
    print(f"path till {root.find(95)} :", root.find(95).get_path())
    print(f"path till {root.find(25)} :", root.find(25).get_path())

    # count_node()
    print(f"number of nodes from {root.find(10)} :",root.find(10).count_node())
    print(f"number of nodes from {root.find(95)} :",root.find(95).count_node())
    print(f"number of nodes from {root.find(70)} :",root.find(70).count_node())
    print(f"number of nodes from {root} :", root.count_node())
    
    # count_leaf_node()
    print(f"count of leaf nodes from {root} :", root.count_leaf_node())
    print(f"count of leaf nodes from {root.find(50)} :",root.find(50).count_leaf_node())
    print(f"count of leaf nodes from {root.find(70)} :",root.find(70).count_leaf_node())
    print(f"count of leaf nodes from {root.find(105)} :",root.find(105).count_leaf_node())

    # count_internal_node()
    print(f"count of internal nodes from {root} :", root.count_internal_node())
    print(f"count of internal nodes from {root.find(50)} :",root.find(50).count_internal_node())
    print(f"count of internal nodes from {root.find(70)} :",root.find(70).count_internal_node())
    print(f"count of internal nodes from {root.find(105)} :",root.find(105).count_internal_node())

    
    # DFS - INORDER, PREORDER, POSTORDER TRAVERSAL
    print("\nORIGINAL TREE :\n")
    root.display()
    print("Inorder Traversal :", root.inorder_traversal())
    print("Preorder Traversal :", root.preorder_traversal())
    print("Postorder Traversal :", root.postorder_traversal())

    # BFS - LEVEL ORDER
    print("BFS Level Order :", root.bfs_levelorder())




    # clear()
    print("\nCLEAR TREE :\n")

    # CLEAR DETACH
    node = root.find(70)
    node.clear_detach()
    print("\nAfter removing 70 subtree :\n")
    root = root.rebalance()
    root.display()     # Tree without 70 - subtree
    print("\nremoved subtree :\n")
    node.display()     # Detached subtree rooted at 70


    # # CLEAR DESTROY
    # node = root.find(70)
    # node.clear_destroy()
    # print("\nAfter removing 70 subtree :\n")
    # root = root.rebalance()
    # root.display()     # Tree without 70 - subtree
    # print("\nremoved subtree :\n")
    # node.display()     # Detached subtree rooted at 70 dosen't exist