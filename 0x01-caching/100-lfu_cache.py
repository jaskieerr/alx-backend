#!/usr/bin/python3
''' LFU Caching '''
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    '''LFU Caching'''

    def __init__(self):
        '''LFU Caching'''
        super().__init__()
        self.counter = {}

    def put(self, k, v):
        '''LFU Caching'''
        if k is None or v is None:
            return

        if k in self.cache_data:
            self.cache_data[k] = v
            self.counter[k] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                m_use = min(self.counter.values())
                least_used_keys = [
                    x for x, count in self.counter.items() if count == m_use
                ]
                lfu_key = min(least_used_keys, key=self.counter.get)
                self.cache_data.pop(lfu_key)
                self.counter.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[k] = v
            self.counter[k] = 1

    def get(self, k):
        '''LFU Caching'''
        if k in self.cache_data:
            self.counter[k] += 1
            return self.cache_data.get(k)

    def get(self, key):
        '''LFU Caching'''
        if key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data.get(key)
