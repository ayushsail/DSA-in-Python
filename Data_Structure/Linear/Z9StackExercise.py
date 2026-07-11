from collections import deque
class Stack :
    def __init__(self) :
        self.container = deque()
    
    def push(self,data) :
        self.container.append(data)
        return data
    
    def pop(self) :
        return self.container.pop()

    def size(self) :
        return len(self.container)
    
    def reverse_string(self,data) :
        for i in data :
            self.push(i)

        new_string = ''
        while self.size() != 0 :
            new_string += self.pop()
        
        return new_string
    
    def is_match(self, ch1, ch2):
        match_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        return match_dict[ch1] == ch2
    
    def isBalance(self,data) :
        for i in data :
            if i == '{' or i == '(' or i == '[' :
                self.push(i)

            if i == '}' or i == ')' or i == ']' :
                if self.size() == 0 :
                    return False
                
                if not self.is_match(i,self.pop()) :
                    return False
            
        return self.size() == 0


# 1.Write a function in python that can reverse a string using stack data structure.
# Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
s = Stack()
print(s.reverse_string("hello"))
print(s.reverse_string("We will conquere COVID-19"))




# 2. PARENTHESIS CHECKER
p = Stack()
print(p.isBalance("{([])}"))
print(p.isBalance("({a+b})"))
print(p.isBalance("))((a+b}{"))
print(p.isBalance("((a+b))"))
print(p.isBalance("((a+g))"))
print(p.isBalance("))"))
print(p.isBalance("[a+b]*(x+2y)*{gg+kk}"))
