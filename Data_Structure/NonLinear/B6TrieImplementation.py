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
            raise ValueError("Prefix cannot be empty!")
        
        current = self.root
        for c in prefix :
            if c not in current.children :
                return False
            current = current.children[c]

        return True
    

# FIND NODE - if word/prefix exist in Trie, It returns last node, otherwise None
    def _find_node(self,text) -> TrieNode | None :
        if not text : raise ValueError("Word cannot be empty!")

        current = self.root
        for c in text :
            if c not in current.children :
                return None
            current = current.children[c]

        return current


# DFS - Depth First Search
    def _dfs(self, current,current_word, wordlist) -> None :
        if current.EndOfWord : 
            wordlist.append(current_word)

        for c,child in current.children.items() :
            self._dfs(child,current_word + c,wordlist)


# GET_WORD_LIST - same like _dfs, it just returns the list
    def get_word_list(self) -> list :
        wordlist = []
        self._dfs(self.root,"",wordlist)

        return wordlist


# ISEMPTY
    def isEmpty(self) -> bool :
        return not self.root.children


# DISPLAY
    def display(self) -> None:
        if self.isEmpty(): raise ValueError("Trie is Empty!")

        print("\nTrie Words :")
        for word in self.get_word_list():
            print("-", word)

        print("\nTrie Tree :\n")
        print("root")
        self._display_tree(self.root)
        print("\n")


# DISPLAY TREE
    def _display_tree(self,current,prefix="") :
        children = list(current.children.items())
        for i,(c,child) in enumerate(children) :
            child_is_last = True if i == len(children)-1 else False

            branch = "└── " if child_is_last else "├── "

            marker = "*" if child.EndOfWord else ""

            print(prefix + branch + c + marker)

            new_prefix = prefix + ("    " if child_is_last else "│   ")

            self._display_tree(child, new_prefix)


# WORD COUNT
    def word_count(self) -> int :
        return len(self.get_word_list())


# PREFIX COUNT - return the number of complete words that start with that prefix
    def prefix_count(self,prefix) -> int :
        if not prefix : raise ValueError("Prefix cannot be empty!")

        node = self._find_node(prefix)
        if not node : return 0

        wordlist = []
        self._dfs(node,"",wordlist)
        return len(wordlist)


# AUTOCOMPLETE - return a list of all complete words that start with that prefix, same like prefix-count
    def auto_complete(self,prefix) -> list :
        if not prefix : raise ValueError("Prefix cannot be empty!")

        node = self._find_node(prefix)             # difference between prefix-count and auto-complete
        if not node : return []

        wordlist = []
        self._dfs(node,prefix,wordlist)             # difference between prefix-count and auto-complete
        return wordlist

# LONGEST COMMON PREFIX - finds the longest prefix shared by all words in the Trie.
    def longest_common_prefix(self) -> str:
        if self.isEmpty() : raise ValueError("Trie is Empty!")

        current = self.root
        prefix = "" 

        while len(current.children) == 1 and not current.EndOfWord :
            for c,child in current.children.items() :
                prefix += c
                current = child
        return prefix

# CLEAR
    def clear(self) -> None:
        self.root = TrieNode()


if __name__ == "__main__" :
    root = Trie()

    # # Insertions
    print("Inserted : ", root.insert("abcd"))
    print("Inserted : ", root.insert("ablg"))
    print("Inserted : ", root.insert("efgh"))
    print("Inserted : ", root.insert("eflk"))
    print("Inserted : ", root.insert("eflks"))

    print("List of Words : ", root.get_word_list())
    print("Word count : ",root.word_count())
    root.display()

    # search
    print("Search 'abcd' : ",root.search("abcd"))
    print("Search 'abc' : ",root.search("abc"))

    # starts with
    print("Starts with 'abc' : ",root.starts_with("abc"))
    print("Starts with 'efg' : ",root.starts_with("efg"))
    print("Starts with 'lg' : ",root.starts_with("lg"))

    # deletion
    print("Deleted : ", root.delete("ablg"))
    print("Deleted : ", root.delete("efgh"))
    print("List of Words : ", root.get_word_list())
    print("Word count : ",root.word_count())
    root.display()

    # find node - returns last node, not the letter
    print("Find 'abcd': ", root._find_node("abcd"))
    print("Find 'abc': ", root._find_node("efg"))
    print("Find 'abcdi': ", root._find_node("efghi"))


    # DFS
    words = []
    root._dfs(root.root,"",words)
    print(words)


    # word count
    print("Word count : ",root.word_count())

    # prefix count
    print("Prefix count of 'ab': ",root.prefix_count("ab"))
    print("Prefix count of 'ef': ",root.prefix_count("ef"))

    # auto-complete
    print("auto-complete of 'ab': ",root.auto_complete("ab"))
    print("auto-complete of 'ef': ",root.auto_complete("ef"))


    # clear
    root.clear()


    print("Inserted : ", root.insert("efgh"))
    print("Inserted : ", root.insert("eflk"))
    print("Inserted : ", root.insert("eflks"))
    root.display()

    # longest_common_prefix
    print("Longest common prefix : ",root.longest_common_prefix())


    
