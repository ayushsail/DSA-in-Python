# COLLISION HANDLING USING CHAINING

class HashTable :
    def __init__(self) :
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]      # NOW WE ARE STORING AN EMPTY ARRAY INSIDE AT ALL 10 INDEXES

# HASH FUNCTION
    def get_hash(self,key) :
        h = 0
        for char in key :
            h += ord(char)
        return h % self.MAX

# ADD FUNCTION
    def add(self,key,value) :
        h = self.get_hash(key)
        found = False
        for index, tuple in enumerate(self.arr[h]) :
            if tuple[0] == key and len(tuple) == 2 :    # this is the case of updating key's data
                self.arr[h][index] = (key,value)      # so here we are storing key,value in form of tuple inside a list
                found = True
                break
            
        if not found :      # this is the case of key dosen't exist, so we just append it
            self.arr[h].append((key,value))        

# GET FUNCTION
    def get(self,key) :
        h = self.get_hash(key)
        for tuple in (self.arr[h]) :
            if tuple[0] == key :
                return tuple[1]
    
# REMOVE FUNCTION
    def remove(self,key) :
        h = self.get_hash(key)
        for index,tuple in enumerate(self.arr[h]) :
            if tuple[0] == key :
                del self.arr[h][index]


t = HashTable()
t.add("march 6",320)
t.add("march 7",340)
t.add("march 8",470)
t.add("march 9",510)


# THEY BOTH HAVE SAME HASH NUMBER(INDEX)
print(t.get_hash("march 6"))
print(t.get_hash("march 17"))

t.add("march 17",520)

print(t.get("march 6"))
print(t.get("march 17"))
print(t.arr)

t.remove("march 6")
t.remove("march 9")
print(t.arr)    