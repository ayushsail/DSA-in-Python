class BinarySearchTreeNode :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None


# ADD NODE
    def add_node(self,data) :
        if self.data == data : return       # duplicate case

        elif data < self.data :
            # add data in left subree
            if self.left : 
                self.left.add_node(data)
            else : 
                self.left = BinarySearchTreeNode(data)
        
        else :
            # add data in right subree
            if self.right : 
                self.right.add_node(data)
            else : 
                self.right = BinarySearchTreeNode(data)


# TRAVERSAL -  TRAVERSAL METHODS ARE IDENTICAL TO EACH OTHER, JUST CHANGE OF ORDER

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



# SEARCH TREE
    def search_tree(self,data) :
        if self.data == data : return True

        elif data < self.data :
            # search in left subtree
            if self.left : 
                return self.left.search_tree(data)
            else : return False
        
        else : 
            # search in right subtree
            if self.right :
                return self.right.search_tree(data)
            else : return False


# FIND MAX
    def find_max(self) :
        if self.right :
            return self.right.find_max()
        else :
            return self.data


# FIND MIN
    def find_min(self) :
        if self.left :
            return self.left.find_min()
        else :
            return self.data



def build_tree(elements) :
    if not elements : return None

    root = BinarySearchTreeNode(elements[0])

    for element in elements[1:len(elements)]:
        root.add_node(element)
    
    return root

if __name__ == "__main__" :
    print("\nBINARY TREE IMPLEMENTATION\n")
    elements = [34,62,6,2,34,87,45,12,24,62,2,1]
    root = build_tree(elements)

    print("Preorder Traversal :", (root.preorder_traversal()))
    print("Inorder Traversal :", (root.inorder_traversal()))
    print("Postorder Traversal :", (root.postorder_traversal()))

    print("Search 1 :", root.search_tree(1))
    print("Search 99 :", root.search_tree(99))

    print("Maximum :", root.find_max())
    print("Minimum :", root.find_min())




    # countries = ["India","Germany","USA","China","India","UK","Brazil","France"]
    # countries_tree = build_tree(countries)
    # print("Preorder Traversal :", (countries_tree.preorder_traversal()))
    # print("Inorder Traversal :", (countries_tree.inorder_traversal()))
    # print("Postorder Traversal :", (countries_tree.postorder_traversal()))

    # print("Search Brazil :", countries_tree.search_tree("Brazil"))
    # print("Search UK :", countries_tree.search_tree("UK"))
    # print("Search Pakistan :", countries_tree.search_tree("Pakistan"))
        
    # print("Maximum :", countries_tree.find_max())
    # print("Minimum :", countries_tree.find_min())