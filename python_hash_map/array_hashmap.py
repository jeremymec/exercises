class LinkedListNode:
    
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next_node = next_node

class HashMap:

    def __init__(self, size):
        self.map = [None] * size

    def insert(self, key, value):
        key_hash = hash(key)
        index = key_hash % len(self.map)
        node = LinkedListNode(key, value, None)
        if (self.map[index] is None):
            self.map[index] = node
        else:
            self.map[index].next_node = node
    
    def get(self, key):
        key_hash = hash(key)
        index = key_hash % len(self.map)
        node = self.map[index]
        while (node.key != key):
            node = node.next_node
        return node.value


if __name__ == "__main__":
    hash_map = HashMap(10)
    hash_map.insert("Grapefruit", "Is Good")
    hash_map.insert("Orange", "Is Bad")
    hash_map.insert("Apple", "Is Okay")
    print(hash_map.get("Orange"))