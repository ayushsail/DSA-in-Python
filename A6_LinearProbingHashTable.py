# COLLISION HANDLING USING LINEAR PROBING

class HashTable :
    def __init__(self) :
        self.MAX = 10
        self.arr = [None] * self.MAX     # NOW WE ARE STORING A "NONE" INSIDE AT ALL 10 INDEXES
        self.DELETED = object()     # "DELETED" MARKER

# HASH FUNCTION
    def get_hash(self,key) :
        h = 0
        for char in key :
            h += ord(char)
        return h % self.MAX
    
# FIND PROBE RANGE
# this will give you the range starting from the key(index) where we try to insert value
# for example, index is 3 so it will give a list [3,4,5,6,7,8,9,0,1,2]
    def get_probe_range(self,index) :       
        return [*range(index,len(self.arr))] + [*range(0,index)]


# FIND SLOT
# this will go through the probe range list and find a empty bucket
    def find_slot(self,key,index) :
        probe_range = self.get_probe_range(index)
        deleted_index = None

        for probe_index in probe_range :
            element = self.arr[probe_index]

            if element is None :      # this is case of empty bucket and deleted bucket
                if deleted_index is not None :
                    return deleted_index
                return probe_index
            
            if  element is self.DELETED :     # this is case of deleted, just remember the index of it
                if deleted_index is None :
                    deleted_index = probe_index
                continue
            
            if element[0] == key :        # this is case of updating existing key's value
                return probe_index
            
        if deleted_index is not None :
            return deleted_index
    
        raise Exception("Hashmap full")


# ADD FUNCTION
    def add(self,key,value) :
        h = self.get_hash(key)
        if self.arr[h] is None or self.arr[h] is self.DELETED :
            self.arr[h] = (key,value)
        else :
            new_h = self.find_slot(key,h)
            self.arr[new_h] = (key,value)

        

# GET FUNCTION
    def get(self,key) :
        h = self.get_hash(key)
        if self.arr[h] is None :
            return "item not found"

        probe_range = self.get_probe_range(h)
        for probe_index in probe_range :
            element = self.arr[probe_index]
            if element is None :
                return "item not found"
            if element is self.DELETED :
                continue

            if element[0] == key :
                return element[1]
            
        return "item not found"
            
    
# REMOVE FUNCTION   - Tombstones (also called deleted markers)
    def remove(self,key) :
        h = self.get_hash(key)
        if self.arr[h] is None :
            return "item not found"

        probe_range = self.get_probe_range(h)
        for probe_index in probe_range :
            element = self.arr[probe_index]
            if element is None :
                return "item not found"

            if element is self.DELETED :
                continue

            if element[0] == key :
                self.arr[probe_index] = self.DELETED
                return

        return "item not found"

t = HashTable()
t.add("march 6",320)
t.add("march 7",340)
t.add("march 8",470)
t.add("march 9",510)

# THEY BOTH HAVE SAME HASH NUMBER(INDEX)
print(t.get_hash("march 6"))    # 9
print(t.get_hash("march 17"))   # 9
print(t.arr)

t.add("march 17",520)
print(t.arr)

print(t.get("march 6"))
print(t.get("march 17"))

print(t.remove("march 9"))
print(t.remove("march 17"))
print(t.arr)    

t.add("march 17",520)
t.add("march 8",5000)

print(t.arr)




# EXPLAINING GET PROBE RANGE FUNCTION
# print(t.get_probe_range(3))
# print(t.get_probe_range(8))
# print([*range(5,10)] + [*range(0,5)])         # output of print(t.get_probe_range(5))


# HASHMAP FULL CONDITION
# t.add("march 6",320)
# t.add("march 7",340)
# t.add("march 8",470)
# t.add("march 9",510)
# t.add("march 1",6000)
# t.add("march 2",7000)
# t.add("march 3",1000)
# t.add("march 4",3000)
# t.add("march 5",8000)
# t.add("march 17",5000)
# t.add("march 10",0000)