# class AVL :
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.height = -1

#     def display(self,level=0) :
#         if self.right : self.right.display(level+1)       
        
#         space = '      ' * level
#         print(f"{space} {self.data} [{self.height}]")

#         if self.left : self.left.display(level+1)


#     def update_height(self) :
#         left_height = right_height = -1    # if left,right subtree not exist, then -1 for left,right subtree.     
#         if self.left : left_height = self.left.height
#         if self.right : right_height = self.right.height

#         self.height = 1 + max(left_height,right_height)


#     def get_balance(self) :
#         left_height = right_height = -1    # if left,right subtree not exist, then -1 for left,right subtree.     
#         if self.left : left_height = self.left.height
#         if self.right : right_height = self.right.height

#         return left_height - right_height
    
#     def right_rotate(self) :
#         old_root = self
#         new_root = old_root.left
#         transfered_subtree = new_root.right

#         # swap root
#         new_root.right = old_root
#         old_root.left = transfered_subtree

#         parent = old_root.parent    
#         if parent :
#             if old_root is parent.left :
#                 parent.left = new_root
#             else :
#                 parent.right = new_root
        
#         # update parents
#         new_root.parent = parent
#         if transfered_subtree : transfered_subtree.parent = old_root
#         old_root.parent = new_root

#         # update height
#         old_root.update_height()
#         new_root.update_height()

#         return new_root

#     def left_rotate(self) :
#         old_root = self
#         new_root = old_root.right
#         transfered_subtree = new_root.left

#         # swap root
#         new_root.left = old_root
#         old_root.right = transfered_subtree

#         parent = old_root.parent
#         if parent :
#             if old_root is parent.right :
#                 parent.right = new_root
#             else :
#                 parent.left = new_root


#         # update parent
#         new_root.parent = parent
#         if transfered_subtree : transfered_subtree.parent = old_root
#         old_root.parent = new_root


#         # update height
#         old_root.update_height()
#         new_root.update_height()

#         return new_root
    
#     def rebalance(self) :
#         self.update_height()        # first update height

#         balance = self.get_balance()

#         if balance > 1 :
#             if self.left.get_balance() >= 0 :
#                 return self.right_rotate()
            
#             else :
#                 self.left = self.left.left_rotate()
#                 return self.right_rotate()
            
#         elif balance < -1 :
#             if self.right.get_balance() <= 0 :
#                 return self.left_rotate()
            
#             else :
#                 self.right = self.right.right_rotate()
#                 return self.left_rotate()
            
#         return self
    

#     def insert(self,data) :
#         if data == self.data :  return

#         elif data < self.data :
#             if self.left : self.left.insert(data)
#             else : 
#                 node = AVL(data)
#                 node.parent = self
#                 self.left = node

#         else :
#             if self.right : self.right.insert(data)
#             else : 
#                 node = AVL(data)
#                 node.parent = self
#                 self.right = node

#         return self.rebalance()


#     def find_max(self) :
#         if self.right : return self.right.find_max()
#         else : return self

#     def find_min(self) :
#         if self.left : return self.left.find_min()
#         else : return self

#     def delete(self,data) :
#         if data < self.data :
#             if self.left : self.left = self.left.delete(data)
#             else : return "data not found !"
#         elif data > self.data :
#             if self.right : self.right = self.right.delete(data)
#             else : return "data not found !"

#         else : 
#             if self.left is None and self.right is None :
#                 return None
            
#             elif self.left is None :
#                 self.right.parent = self.parent

#             elif self.right is None :
#                 self.left.parent = self.parent

#             else :
#                 min_val = self.right.find_min()
#                 self.data = min_val.data
#                 self.right = self.right.delete(min_val.data)

#         return self.rebalance()
            
# def build_tree(elements) :
#     if not elements : return None

#     root = AVL(elements[0])

#     for element in elements[1:len(elements)]:
#         root = root.insert(element)
    
#     return root

# if __name__ == "__main__" :
#     print("\nAVL TREE IMPLEMENTATION\n")
#     elements = [50,30,70,20,40,35,80,25,35,45,95,105,10]
#     root = build_tree(elements)
#     print("\nORIGINAL TREE :\n")
#     root.display()
#     print(f"Balance of root :{root.get_balance()}\n")


#     root = root.delete(40)
#     root.display()
#     print(f"Balance of root :{root.get_balance()}\n")

#     root = root.delete(10)
#     root.display()
#     print(f"Balance of root :{root.get_balance()}\n")

#     root = root.delete(35)
#     root.display()
#     print(f"Balance of root :{root.get_balance()}\n")

#     root = root.delete(25)
#     root.display()
#     print(f"Balance of root :{root.get_balance()}\n")
        
#     root = root.delete(30)
#     root.display()
#     print(f"Balance of root :{root.get_balance()}\n")
        
#     root = root.delete(20)
#     root.display()
#     print(f"Balance of root :{root.get_balance()}\n")
        