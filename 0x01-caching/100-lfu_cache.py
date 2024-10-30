#!/usr/bin/python3
""" doc doc doc """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """doc doc doc"""

    def __init__(self):
        """doc doc doc"""
        super().__init__()
        self.use_count = {}

    def put(self, k, v):
        """doc doc doc"""
        if k is None or v is None:
            return

        if k in self.cache_data:
            self.cache_data[k] = v
            self.use_count[k] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_use = min(self.use_count.values())
                least_used_keys = [
                    x for x, count in self.use_count.items() if count == min_use
                ]
                lfu_key = min(least_used_keys, key=self.use_count.get)
                self.cache_data.pop(lfu_key)
                self.use_count.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[k] = v
            self.use_count[k] = 1

    def get(self, k):
        """doc doc doc"""
        if k in self.cache_data:
            self.use_count[k] += 1
            return self.cache_data.get(k)
