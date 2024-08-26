class HashTable:

    # Creates empty buckets with default size of 40
    def __init__(self, size = 40):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    # Accesses a value given a key from the hash table
    def get_value(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.buckets[hashed_key]

        for key_value in bucket:
            if key_value[0] == key:
                return key_value[1]

        return []

    # Inserts or updates a key value pair in the hash table
    def set_value(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.buckets[hashed_key]

        for key_value in bucket:
            if key_value[0] == key:
                key_value[1] = value
                return

        bucket.append((key, value))
