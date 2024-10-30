#!/usr/bin/python3
''' LFU Caching '''
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    '''LFU Caching'''

    def __init__(self):
        '''LFU Caching'''
        super().__init__()
        self.usage = {}

    def put(self, k, v):
        '''LFU Caching'''
        if k is None or v is None:
            return

        if k in self.cache_data:
            self.cache_data[k] = v
            self.usage[k] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_use = min(self.usage.values())
                lfu_keys = [x for x, u in self.usage.items() if u == min_use]
                lfu_key = min(lfu_keys, key=self.usage.get)
                self.cache_data.pop(lfu_key)
                self.usage.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[k] = v
            self.usage[k] = 1

    def get(self, k):
        '''LFU Caching'''
        if k in self.cache_data:
            self.usage[k] += 1
            return self.cache_data.get(k)
