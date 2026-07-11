from Data_Structure.Linear.A8QueueImplementation import QueueLL       # for BFS - Level Order

# TREE IMPLEMENTATION
class TreeNode :
    def __init__(self,data) :
        self.data = data        # name of node
        self.children = []      # children of node
        self.parent = None      # parent on node
    
    def __str__(self):
        return self.data

    def __repr__(self):
        return self.__str__()
    
# ADD CHILD
    def add_child(self, child):

        if not isinstance(child, TreeNode):
            raise TypeError("Child must be a TreeNode.")

        if child is self:
            raise ValueError("A node cannot be its own child.")

        if child.parent is not None:
            raise ValueError("Node already has a parent.")

        child.parent = self
        self.children.append(child)

    def add_child_list(self,child_list) :
        for child in child_list :
            self.add_child(child)
    

# REMOVED CHILD
    def remove_child(self,data) :
        for child in self.children :
            if child.data == data :
                child.parent = None
                self.children.remove(child)
                return child

            value = child.remove_child(data)    # make it recursive to search subtree

            if value is not None : return value

        
        return None

    
# DISPLAY
    def print_tree(self,level = 0) :
        space = '    ' * level      # space == 4 spaces(default) * level
        prefix = ""
        if self.parent : prefix = space + '|___'


        print(prefix + self.data)        # give data of node
        for child in self.children :
            child.print_tree(level + 1)
    

# FIND DATA
    def find(self,data) :
        if self.data == data :
            return self
        for child in self.children :
            result = child.find(data)

            if result is not None : return result
        
        return None


# CONTAIN DATA - same like find(), just return True/False
    def contains(self,data) :
        return self.find(data) is not None
    
    def is_root(self) :
        return self.parent is None
    
    def is_leaf(self) :
        return not self.children    # or len(self.children == 0)
    

# GET LEVEL - level == No. of ancestor from root
    def get_level(self) :
        p = self.parent
        level = 0
        while p :
            level += 1
            p = p.parent

        return level
    

# GET HEIGHT - The number of edges in the longest path from that node to any leaf node.
    def get_height(self) :
        if self.is_leaf() :
            return 0
        max_height = 0
        for child in self.children :
            child_height = child.get_height()
            if child_height > max_height : max_height = child_height
        
        return 1 + max_height


# COUNT NODE - total number of nodes in the subtree rooted at the current node.
    def count_node(self) :
        count = 1
        for child in self.children :
            count += child.count_node()
        
        return count
    

# COUNT LEAF NODE - total number of leaf nodes in the subtree rooted at the current node.
    def count_leaf_node(self) :
        if self.is_leaf() :
            return 1
        
        count = 0
        for child in self.children :
            count += child.count_leaf_node()
    
        return count
    

# COUNT INTERNAL NODE - any node that is not a leaf, thus it also include root node
    def count_internal_node(self) :
        if self.is_leaf() :
            return 0
        count = 1
        for child in self.children :
            count += child.count_internal_node()
        
        return count
    

# GET ROOT - return root form any node
    def get_root(self) :
        node = self 
        while node.parent :
            node = node.parent
        return node
    

# GET PATH - return path from node to the root
    def get_path(self) :
        node = self
        path = []
        while node:
            path.append(node.data)
            node = node.parent
        
        path.reverse()
        return " --> ".join(path)


# DEPTH FIRST SERACH (DFS) - PREORDER - visit parent before children
    def dfs_preorder(self,result) :
        result.append(self.data)        # visit before
        for child in self.children :
            child.dfs_preorder(result)


# DEPTH FIRST SERACH (DFS) - POSTORDER - visit children before parent
    def dfs_postorder(self,result) :
        for child in self.children:
            child.dfs_postorder(result)
        result.append(self.data)        # visit after
        


# BREADTH FIRST SERACH (BFS) - LEVEL ORDER - visit level - by - level
    def bfs_levelorder(self,result) :
        q = QueueLL()
        q.enqueue(self)
        while not q.isEmpty() :
            node = q.dequeue()
            result.append(node.data)
            for child in node.children :
                q.enqueue(child)
            
        
# CLEAR DESTROY - it detach each node from their parent, subtree do not exist
    def clear_destroy(self) :       # destroy subtree
        for child in self.children :
            child.clear_destroy()
            child.parent = None
        self.children.clear()

# CLEAR DETACH - it detach the subtree from root, subtree still exist
    def clear_detach(self) :       # detach subtree
        for child in self.children :
            child.parent = None
        self.children.clear()
        


if __name__ == "__main__" :
    # Create root
    root = TreeNode("Electronics")

    # Create Laptop subtree
    laptop = TreeNode("Laptop")
    # laptop.add_child(TreeNode("Mac"))
    # laptop.add_child(TreeNode("ThinkPad"))
    # laptop.add_child(TreeNode("Surface"))
    laptop.add_child_list([TreeNode("Mac"),TreeNode("ThinkPad"),TreeNode("Surface")])

    # Create Phone subtree
    phone = TreeNode("Phone")
    phone.add_child(TreeNode("iPhone"))
    phone.add_child(TreeNode("Nothing"))
    phone.add_child(TreeNode("Google Pixel"))

    # Create TV subtree
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))

    # Attach to root
    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    # Original Tree
    print(f"children of {root.data}", root.children)    
    print("Original Tree")
    root.print_tree()


    # remove_child() & add_child()
    removed = root.remove_child("iPhone")
    print(f"removed : {removed}" if removed else "Data Not Found !")
    root.print_tree()

    removed = root.remove_child("Laptop")
    print(f"removed : {removed}" if removed else "Data Not Found !")
    root.print_tree()

    removed = root.remove_child("LG")
    print(f"removed : {removed}" if removed else "Data Not Found !")
    root.print_tree()

    root.add_child(laptop)
    root.print_tree()

    tv.add_child(TreeNode("LG"))
    print("\nsubtree TV :")
    tv.print_tree()
    
    phone.add_child(TreeNode("iPhone"))
    print("\nsubtree Phone :")
    phone.print_tree()

    root.print_tree()


    # find()
    result = root.find("TV")
    print(f"Found : {result}" if result else "Data Not Found !")
    result = root.find("Surface")
    print(f"Found : {result}" if result else "Data Not Found !")

    # contain()
    print(f"does {root} contains 'camera'", root.contains("camera"))   # False
    print(f"does {root} contains 'LG'", root.contains("LG"))   # True

    # is_root()
    print(f"{tv} is root :",tv.is_root())   # False
    print(f"{laptop} is root :",laptop.is_root())   # False
    print(f"{root} is root :",root.is_root())   # True
    print(f"{root.find("Mac")} is root :",root.find("Mac").is_root())   # False, for descendent use it like this.
    print(f"{root.find("Electronics")} is root :",root.find("Electronics").is_root())   # True

    # is_leaf()
    print(f"{root} is leaf node :", root.is_leaf())
    print(f"{tv} is leaf node :",tv.is_leaf())
    print(f"{root.find("LG")} is leaf node :",root.find("LG").is_leaf())
    print(f"{root.find("Mac")} is leaf node :",root.find("Mac").is_leaf())

    # get_height()
    print(f"height of {root} :", root.get_height())
    print(f"height of {root.find("Mac")} :", root.find("Mac").get_height())
    print(f"height of {root.find("Laptop")} :", root.find("Laptop").get_height())

    # count_node()
    print(f"number of nodes from {root} :", root.count_node())
    print(f"number of nodes from {root.find("Laptop")} :",root.find("Laptop").count_node())
    print(f"number of nodes from {root.find("Mac")} :",root.find("Mac").count_node())

    # count_leaf_node()
    print(f"count of leaf nodes from {root} :", root.count_leaf_node())
    print(f"count of leaf nodes from {root.find("Laptop")} :",root.find("Laptop").count_leaf_node())
    print(f"count of leaf nodes from {root.find("Mac")} :",root.find("Mac").count_leaf_node())

    # count_internal_node()
    print(f"count of internal nodes from {root} :", root.count_internal_node())
    print(f"count of internal nodes from {root.find("Laptop")} :",root.find("Laptop").count_internal_node())
    print(f"count of internal nodes from {root.find("Mac")} :",root.find("Mac").count_internal_node())

    # get_root()
    print(f"root of {root.find("Mac")} :", root.find("Mac").get_root())
    print(f"root of {root.find("Phone")} :", root.find("Phone").get_root())

    # get_path()
    print(f"path from {root.find("Mac")} :", root.find("Mac").get_path())
    print(f"path from {root.find("Sony")} :", root.find("Sony").get_path())



    # DFS - PREORDER
    result = []
    root.dfs_preorder(result)
    print("\nDFS - PREORDER :")
    print(" --> ".join(result))

    # DFS - POSTORDER
    result = []
    root.dfs_postorder(result)  
    print("\nDFS - POSTORDER :") 
    print(" --> ".join(result))

    # BFS - LEVEL ORDER
    result = []
    root.bfs_levelorder(result)  
    print("\nBFS - LEVEL ORDER :") 
    print(" --> ".join(result))



    # clear()
    print("\nCLEAR TREE :\n")

    root.clear_detach()
    root.print_tree()
    print(laptop.children)      # has children

    root.clear_destroy()
    root.print_tree()
    print(laptop.children)      # no children