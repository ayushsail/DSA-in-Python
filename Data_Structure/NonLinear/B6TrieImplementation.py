class TrieNode :
    def __init__(self) :
        self.children = {}          # storing childrens in dict/hash map
        self.EndOfWord = False      # word end marker

class Trie : 
    def __init__(self):
        self.root = TrieNode()


# INSERT WORD
    def insert(self,word:str) -> str : 
        # empty string validation
        if not word:
            raise ValueError("Word cannot be empty!")
        
        current = self.root
        for c in word :
            if c not in current.children :
                current.children[c] = TrieNode()
            current = current.children[c]

        current.EndOfWord = True
        return word


# DELETE WORD
    def delete(self, word:str) -> str :
        # empty string validation
        if not word:
            raise ValueError("Word cannot be empty!")
        
        current = self.root

        # word validation
        for c in word :
            if c not in current.children :
                raise ValueError("The word doesn't exist in Trie !")
            current = current.children[c]

        if current.EndOfWord is False :
            raise ValueError("The word doesn't exist in Trie !")

        # recursively delete the word backward
        self._delete_helper(self.root, word, 0)

        # return deleted word
        return word


# DELETE HELPER METHOD
    def _delete_helper(self, current, word:str, depth:int) -> bool :
        if depth == len(word) :
            current.EndOfWord = False

            # keep this word if another word continues from here
            if current.children :
                return False
            
            # if node has no child and it's not a EndOfWord, So node is now useless - delete it
            else :
                return True

        c = word[depth]
        child = current.children[c]

        # recursively process the child
        should_delete = self._delete_helper(child,word,depth+1)         # return True/False

        if should_delete :
            del current.children[c]

        # Current node can be removed if:
        # 1. It has no other children
        # 2. It is not the end of another word
        if not current.children and not current.EndOfWord : return True
        else : return False
                

# SEARCH
    def search(self, word:str) -> bool :
        # empty string validation
        if not word:
            raise ValueError("Word cannot be empty!")
        
        current = self.root
        for c in word :
            if c not in current.children :
                return False
            current = current.children[c]

        return current.EndOfWord


# STARTS_WITH
    def starts_with(self, prefix:str) -> bool :
        # empty string validation
        if not prefix:
            raise ValueError("Word cannot be empty!")
        
        current = self.root
        for c in prefix :
            if c not in current.children :
                return False
            current = current.children[c]

        return True



if __name__ == "__main__" :
    root = Trie()
    print("Inserted : ", root.insert("abcd"))
    print("Inserted : ", root.insert("ablg"))
    print("Inserted : ", root.insert("efgh"))

    print("Search 'abcd' : ",root.search("abcd"))
    print("Search 'abc' : ",root.search("abc"))

    print("Starts with 'abc' : ",root.starts_with("abc"))
    print("Starts with 'lg' : ",root.starts_with("lg"))

    print("Deleted : ", root.delete("ablg"))
    print("Deleted : ", root.delete("efgh"))

    
