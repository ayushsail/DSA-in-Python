# BASICALLY THE FUNCTION ARE SAME BUT GIVING INPUTS & TAKING OUTPUTS ARE SAME LIKE DICTIONARY
# THIS IS NOT EXACTLY SAME LIKE DICTIONARY, BUT IT GIVES UNDERSTANDING OF HOW DICTIONARY WORKS USING HASH TABLE.

# DEFINE CLASS HASHTABLE WITH ARRAY WHOSE SIZE IS 50 OR 100, INITIALIZE WITH "NONE" AS VALUE
class Dictionary :
    def __init__(self) :
        self.MAX = 50
        self.arr = [None for i in range(self.MAX)]      # LIST COMPREHENSION

# HASH FUNCTION
    def get_hash(self,key) :
        h = 0
        for char in key :
            h += ord(char)
        return h % self.MAX

# ADD FUNCTION
    def __setitem__(self,key,value) :
        h = self.get_hash(key)
        self.arr[h] = value

# GET FUNCTION
    def __getitem__(self,key) :
        h = self.get_hash(key)
        return self.arr[h]
    
# REMOVE FUNCTION
    def __delitem__(self,key) :
        h = self.get_hash(key)
        self.arr[h] = None

# LENGHT OF DICT
    def __len__(self):
        count = 0
        for item in self.arr :
            if item is not None :
                count += 1
        return count
    


if __name__ == "__main__" :
    dict = Dictionary()
    # INPUT/OUTPUT SYNTAX IS SAME LIKE DICT
    dict["march 6"] = 320      # calls setitem operator
    dict["march 7"] = 340
    dict["march 8"] = 470
    dict["march 9"] = 510
    dict["march 10"] = 100

    print(len(dict))        # calls len operator

    print(dict["march 10"] )      # calls getitem operator

    del dict["march 8"]    # calls delitem operator
    print(dict["march 8"])

    print(len(dict))

    print(dict.arr)