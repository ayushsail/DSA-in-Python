''' (1) Design a General Tree to represent a company's management hierarchy.
where each employee has a name and designation.
Implement methods to add an employee,remove an employee recursively, and display the hierarchy in different format -
(name, designation, or both). '''
class TreeNode :
    def __init__(self,data=None) :
        self.data = data       # name of node
        self.children = []      # children of node
        self.parent = None      # parent on node
    
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)
    

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
    

# REMOVED CHILD
    def remove_child(self, data):

        for i, child in enumerate(self.children):

            if child.data[0] == data:
                value = data
                child.parent = None
                self.children.pop(i)
                return value

            removed = child.remove_child(data)

            if removed is not None:
                return removed

        return None

    
# DISPLAY
    def print_tree(self, mode="both", level=0):

        if mode not in ("name", "designation", "both"):
            raise ValueError("mode must be 'name', 'designation', or 'both'")

        space = "    " * level
        prefix = space + "|___" if self.parent else ""

        if mode == "name": text = self.data[0]

        elif mode == "designation": text = self.data[1]

        else: text = f"{self.data[0]} ({self.data[1]})"

        print(prefix + text)

        for child in self.children:
            child.print_tree(mode, level + 1)

def build_management_tree() :
    root = TreeNode(["Nilpul","CEO"])

    chinmay = TreeNode(["Chinmay","CTO"])

    vishwa = TreeNode(["Vishwa","Infrastructure Head"])
    vishwa.add_child(TreeNode(["Dhaval","Cloud Manager"]))
    vishwa.add_child(TreeNode(["Abhijit","App Manager"]))

    aamir = TreeNode(["Aamir","Application Head"])

    chinmay.add_child(vishwa)
    chinmay.add_child(aamir)

    gels = TreeNode(["Gels","HR Head"])
    gels.add_child(TreeNode(["Peter","Recruitment Manager"]))
    gels.add_child(TreeNode(["Waqas","Policy Manager"]))

    root.add_child(chinmay)
    root.add_child(gels)

    return root

if __name__ == "__main__" :
    print("\nPROBLEM - 1\n")

    root = build_management_tree()
    print("\nTree with only names :\n")
    root.print_tree("name")
    print("\nTree with only designation :\n")
    root.print_tree("designation")
    print("\nTree with both :\n")
    root.print_tree()


    print("Removed :", root.remove_child("Dhaval"))
    root.print_tree()

    print("Removed :", root.remove_child("Waqas"))
    root.print_tree()




'''(2) Given a General Tree and an integer level,
print all nodes from the root up to the specified level.'''
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
    def add_child(self,child) :
        if child.parent is not None :       # duplicate case
            raise Exception("Node already has a parent !")
        
        child.parent = self
        self.children.append(child)
    

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
    
# GET LEVEL - level == No. of ancestor from root
    def get_level(self) :
        p = self.parent
        level = 0
        while p :
            level += 1
            p = p.parent

        return level
    
# DISPLAY
    def print_tree(self, max_level, current_level=0):

        if current_level > max_level:
            return

        space = "    " * current_level
        prefix = space + "|___" if self.parent else ""

        print(prefix + self.data)
        for child in self.children:
            child.print_tree(max_level, current_level + 1)


def build_location_tree() :
    print("\nPROBLEM - 2\n")
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)


    usa = TreeNode("USA")

    newjersey = TreeNode("New Jersey")
    newjersey.add_child(TreeNode("Princeton"))
    newjersey.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Fancisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(newjersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root
        
if __name__ == "__main__" : 

    root = build_location_tree()
    root.print_tree(0)
    root.print_tree(1)
    root.print_tree(2)
    root.print_tree(3)