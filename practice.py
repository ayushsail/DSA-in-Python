# from A1_ArrayImplementation import DynamicArray

# # STACK ARRAY IMPLEMENTATION
# print("STACK ARRAY IMPLEMENTATION\n")
# class StackArr :
#     def __init__ (self,size) :
#         self.size = size
#         self.arr = DynamicArray(size)
#         self.TOP = -1
    
#     # def isFull(self) :
#     #     if self.TOP == self.size -1 :
#     #         return True
#     #     else :
#     #         return False
    
#     # def isEmpty(self) :
#     #     if self.TOP == -1 :
#     #         return True
#     #     else :
#     #         return False
        
#     def push(self,data) :
#         if self.isFull() :
#             raise Exception ("Stack Overflow !")
#         self.TOP += 1
#         self.arr[self.TOP] = data
#         return data
    
#     def pop(self) :
#         if self.isEmpty() :
#             raise Exception ("Stack Underflow !")
        
#         value = self.arr[self.TOP]
#         self.arr[self.TOP] = None
#         self.TOP -= 1
#         return value
    
#     def peek(self) :
#         if self.isEmpty() :
#             raise Exception ("Stack Underflow !")
        
#         return self.arr[self.TOP]
    
#     def get_size(self) :
#         return self.TOP + 1
    
#     def display(self) :
#         if self.isEmpty() :
#             print("Stack Underflow !")
#             return
        
#         for i in range(self.TOP,-1,-1) :
#             print(self.arr[i])
    
#     def clear(self) :
#         self.arr = [None] * self.size
#         self.TOP = -1

    


# s = StackArr(5)








# # print("Pushed :",sa.push(100))
# # print("Pushed :",sa.push(200))
# # print("Pushed :",sa.push(300))
# # print("Pushed :",sa.push(400))
# # print("Pushed :",sa.push(500))
# # print(sa.arr)

# # print("Popped :",sa.pop())
# # print("Popped :",sa.pop())
# # print("Popped :",sa.pop())
# # print(sa.arr)

# # print("Topmost element :",sa.peek())

# # print("No. of element :",sa.get_size())

# # print("Pushed :",sa.push(300))
# # print("Pushed :",sa.push(400))
# # print("Pushed :",sa.push(500))
# # sa.display()

# # sa.clear()
# # sa.display()







