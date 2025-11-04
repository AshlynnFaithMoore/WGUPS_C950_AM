# creating a hashmap w/o libraries
class HashTable:
    """
        Custom hash table implementation using chaining for collision resolution.

    Time Complexity:
        - Insert: O(1) average case, O(n) worst case (all items hash to same bucket)
        - Lookup: O(1) average case, O(n) worst case
        - Delete: O(1) average case, O(n) worst case

    Space Complexity: O(n) where n is the number of items stored
    """

    def __init__(self, size = 20):
        # initializing the hashtable with 20 buckets or empty lists
        self.list = []
        for i in range(size):
            self.list.append([])

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.

        If the key already exists, its value is updated. Otherwise, a new
        key-value pair is added to the appropriate bucket.

        """
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for keyval in bucket_list:
            if keyval[0] == key:
                keyval[1] = value
                return True
        # if not found in bucket, add
        key_val = [key, value]
        bucket_list.append(key_val)
        return True

    def lookup(self, key):
        """
        Checks if the key exists in the hash table. If it does, returns value associated with key.
        Otherwise, returns None.
        """
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None

    def hash_remove(self, key):
        """
        Removes a key from the hash table.
        If the key does not exist, returns False.

        """
        slot = hash(key) % len(self.list)
        bucket_list = self.list[slot]
        for pair in bucket_list:
            if pair[0] == key:
                bucket_list.remove(pair)
                return True
        return False
