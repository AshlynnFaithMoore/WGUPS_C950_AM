# creating a hashmap w/o libraries
class HashTable:
    # constructor
    def __init__(self, size = 20):
        self.list = []
        for i in range(size):
            self.list.append([]) #using buckets to support collision chaining

    def insert(self, key, value):
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
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None

    def hash_remove(self, key):
        slot = hash(key) % len(self.list)
        bucket_list = self.list[slot]
        for pair in bucket_list:
            if pair[0] == key:
                bucket_list.remove(pair)
                return True
        return False
