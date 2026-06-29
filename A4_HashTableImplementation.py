# DEFINE CLASS HASHTABLE WITH ARRAY WHOSE SIZE IS 50 OR 100, INITIALIZE WITH "NONE" AS VALUE
class HashTable :
    def __init__(self) :
        self.MAX = 50
        self.arr = [None] * self.MAX      # LIST COMPREHENSION

# HASH FUNCTION
    def get_hash(self,key) :
        h = 0
        for char in key :
            h += ord(char)
        return h % self.MAX

# ADD FUNCTION
    def add(self,key,value) :
        h = self.get_hash(key)
        self.arr[h] = value

# GET FUNCTION
    def get(self,key) :
        h = self.get_hash(key)
        return self.arr[h]
    
# REMOVE FUNCTION
    def remove(self,key) :
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
print(t.get_hash("march 6"))
t.add("march 6",320)
t.add("march 7",340)
t.add("march 8",470)
t.add("march 9",510)
t.add("march 10",100)

# print(t.arr)      # THIS FUNCTION WILL GIVE YOU THE LIST WITH STORED VALUES


print(t.get("march 7"))
print(t.get("march 8"))
print(t.get("march 9"))

t.remove("march 8")
print(t.arr)
print(t.get("march 8"))

# SINCE DICTIONARY IS IMPLEMENTED USING HASH TAABLE
# WE CAN ALSO IMPLEMENT DICTIONARY USING HASH TABLE WITH HELP OF SPECIAL INBUILT FEATURES.