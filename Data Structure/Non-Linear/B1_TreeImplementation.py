class TreeNode :
    def __init__(self,data) :
        self.data = data
        self.children = []
        # each of the element in the child list will be an instance of Tree node class.
        # child node will be an another TreeNode in it self, RECURSIVE.
        self.parent = None

    def add_child(self, child) :
        child.parent = self
        # here self => parent variable of TreeNode, which translates to add_child(parent, child)
        # use this function as <parent.add_child("child")>
        self.children.append(child)

    def get_level(self) :       # no. of ancestor == leve
        level = 0
        p = self.parent
        while p :
            level += 1
            p = p.parent
        
        return level


    def print_tree(self) :
        # since child is also an object of TreeNode class, RECURSION CAN PRINT SUBTREES

        spaces = ' ' * self.get_level() * 3      # spaces given according to level
        prefix = spaces +'|___' if self.parent else ""


        print(prefix + self.data)        # gives data

        if self.children :          # same as if len(self.children) > 0 :
            for child in self.children :    # give childrens
                child.print_tree()


def build_tree() :
    root = TreeNode("Electronics")      # main TreeNode

    laptop = TreeNode("Laptop")     # child of electronic(root), which as an another TreeNode
    # adding children of laptop
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Thinkpad"))
    laptop.add_child(TreeNode("Surface"))

    phone = TreeNode("Phones")       # child of electronic(root), which as an another TreeNode
    # adding children of phone
    phone.add_child(TreeNode("iPhone"))
    phone.add_child(TreeNode("Nothing"))
    phone.add_child(TreeNode("Google Pixel"))

    tv = TreeNode("TV")     # child of electronic(root), which as an another TreeNode
    # adding children of tv
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))


    root.add_child(laptop)      # adding laptop as child
    root.add_child(phone)      # adding phone as child
    root.add_child(tv)      # adding tv as child

    return root



if __name__ == "__main__" :
    root = build_tree()
    print("level of root : ", root.get_level())
    root.print_tree()

