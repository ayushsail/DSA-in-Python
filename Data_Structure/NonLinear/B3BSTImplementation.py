class BinarySearchTreeNode :
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None


# DISPLAY
    def display(self,level=0) :
        if self.right :
            self.right.display(level+1)
        
        space = '     ' * level
        print(f"{space} {self.data}")

        if self.left :
            self.left.display(level+1)


# ADD NODE
    def add_node(self,data) :
        if self.data == data : return self    # duplicate case

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
                return self.right
            
            elif self.right is None :   # if self has no right child - return left child
                return self.left
            
            
            # if self has two child
            else : 
                # find min_val in right subtree or max_val in left subtree and replace it with self
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)
                

            # alternate method by using left subtree's max_val
            # else : 
            #     # find min_val in right subtree or max_val in left subtree and replace it with self
            #     max_val = self.left.find_max()
            #     self.data = max_val
            #     self.left = self.left.delete(max_val)

        return self




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
    root.display()

    print("Preorder Traversal :", (root.preorder_traversal()))
    print("Inorder Traversal :", (root.inorder_traversal()))
    print("Postorder Traversal :", (root.postorder_traversal()))

    print("Search 1 :", root.search_tree(1))
    print("Search 99 :", root.search_tree(99))
    
    print("Maximum :", root.find_max())
    print("Minimum :", root.find_min())
    

    root = root.delete(45)
    print("After Deleting 45 :", root.inorder_traversal())
    root.display()

    root = root.delete(1)      # leaf case
    print("After Deleting 1 :", root.inorder_traversal())
    root.display()
    
    root = root.delete(34)     # root case
    print("After Deleting 34 :", root.inorder_traversal())
    root.display()

    # while deleting, incase you are deleting the root node - thus, write it like this "root = root.delete(34)"
    # So that new root is assigned again




    countries = ["India","Germany","USA","China","India","UK","Brazil","France"]
    countries_tree = build_tree(countries)
    countries_tree.display()
    print("Preorder Traversal :", (countries_tree.preorder_traversal()))
    print("Inorder Traversal :", (countries_tree.inorder_traversal()))
    print("Postorder Traversal :", (countries_tree.postorder_traversal()))

    print("Search Brazil :", countries_tree.search_tree("Brazil"))
    print("Search UK :", countries_tree.search_tree("UK"))
    print("Search Pakistan :", countries_tree.search_tree("Pakistan"))
        
    print("Maximum :", countries_tree.find_max())
    print("Minimum :", countries_tree.find_min())


    countries_tree = countries_tree.delete("USA")
    print("After Deleting USA :", countries_tree.inorder_traversal())
    countries_tree.display()

    countries_tree = countries_tree.delete("Brazil")      # leaf case
    print("After Deleting Brazil :", countries_tree.inorder_traversal())
    countries_tree.display()
    
    countries_tree = countries_tree.delete("India")     # root case
    print("After Deleting India :", countries_tree.inorder_traversal())
    countries_tree.display()