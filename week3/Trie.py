class Node:
    def __init__(self, isKey):
        self.isKey = isKey
        self.children = dict()

class Trie:

    def __init__(self):
        self.root = Node(False)

    def insert(self, word):
        walk = self.root
        for i in range(len(word)):
            finish = i == len(word) - 1
            if word[i] not in walk.children.keys():
                walk.children[word[i]] = Node(False)
            walk = walk.children[word[i]]
        walk.isKey = True

    def search(self, word):
        walk = self.root
        for i in range(len(word)):
            if word[i] in walk.children.keys():
                walk = walk.children[word[i]]
            else:
                return False
        return walk.isKey

    def startsWith(self, prefix):
        walk = self.root
        for c in prefix:
            if c in walk.children.keys():
                walk = walk.children[c]
            else:
                return False
        return True

trie = Trie()

# trie.insert("jam")
# print(trie.search("apple"))
# print(trie.search("app"))
# print(trie.startsWith("appl"))
# trie.insert("app")
# trie.search("app")


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
lst1 = ["insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]

args = [["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]

def test(command, args, trie):
    for i in range(len(command)):
        if command[i] == "insert":
            trie.insert(args[i][0])
            print("inserted")
        elif command[i] == "search":
            print(trie.search(args[i][0]))
        elif command[i] == "startsWith":
            print(trie.startsWith(args[i][0]))

# test(lst1, args, trie)

commands2 = ["insert","search","search","search","startsWith","startsWith","startsWith"]
args2 = [["hello"],["hell"],["helloa"],["hello"],["hell"],["helloa"],["hello"]]
test(commands2, args2, trie)
