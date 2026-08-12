from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # Initialize an OrderedDict to store key-value pairs and automatically track their order
        self.cache = OrderedDict()
        # Store the maximum number of items the cache is allowed to hold
        self.cap = capacity

    def get(self, key: int) -> int:
        # If the key is not in the cache, it's a cache miss; return -1
        if key not in self.cache:
            return -1
        
        # If it is found, mark it as "most recently used" by moving it to the end of the dictionary
        self.cache.move_to_end(key)
        # Return the value associated with the key
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If the key already exists, move it to the end because we are accessing/updating it
        if key in self.cache:
            self.cache.move_to_end(key)
            
        # Insert the new key-value pair (or update the value if the key already existed)
        self.cache[key] = value

        # If adding this item causes the cache to exceed its maximum capacity...
        if len(self.cache) > self.cap:
            # ...remove the oldest item (the Least Recently Used one at the front)
            self.cache.popitem(last=False)