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
        
        if self.right :
            self.right.display(level+1)
        
        space = '        ' * level
        print(f"{space}{self.data} [{self.height}]")

        if self.left :
            self.left.display(level+1)


# UPDATE HEIGHT - Update height, after performing balancing operation
    def update_height(self) :
        left_height = right_height = -1

        if self.left :
            left_height = self.left.height
        
        if self.right :
            right_height = self.right.height
        
        self.height = 1 + max(left_height,right_height)


# GET BALANCE - returns balance of node, left_height - right_height
    def get_balance(self) :
        left_height = right_height = -1
        
        if self.left :
            left_height = self.left.height

        if self.right :
            right_height = self.right.height
        
        return left_height - right_height
    

# RIGHT ROTATE - if balance is  +2 or +1 - perform this rotation
    def right_rotate(self) :
        if self.left is None: raise ValueError("Right rotation not possible.")
        
        old_root = self
        new_root = old_root.left
        transfered_subtree = new_root.right


        # swapping old_root & new_root
        new_root.right = old_root
        old_root.left = transfered_subtree


        # updating parent of new_root, transfered_subtree & old_root
        parent = old_root.parent

        if parent:
            if old_root is parent.left:
                parent.left = new_root
            else:
                parent.right = new_root

        new_root.parent = parent

        if transfered_subtree : transfered_subtree.parent = old_root

        old_root.parent = new_root


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

        # swapping old_root & new_root
        new_root.left = old_root
        old_root.right = transfered_subtree


        # updating parent of new_root, transfered_subtree & old_root
        parent = old_root.parent

        if parent:
            if old_root is parent.right:
                parent.right = new_root
            else:
                parent.left = new_root

        new_root.parent = parent

        if transfered_subtree : transfered_subtree.parent = old_root

        old_root.parent = new_root


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
            
            else :          # LR - case
                self.left = self.left.left_rotate()
                return self.right_rotate()
        
        elif balance < -1 :
            if self.right.get_balance() <= 0 :      # RR - case
                return self.left_rotate()
            
            else :          # RL - case
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

    print("\nDeleted : 80\n")
    root = root.delete(80)
    root.display()

    print("\nDeleted : 20\n")
    root = root.delete(20)
    root.display()

    print("\nDeleted : 10\n")
    root = root.delete(10)
    root.display()

    print("\nDeleted : 40\n")
    root = root.delete(40)
    root.display()