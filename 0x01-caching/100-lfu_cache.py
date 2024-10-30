#!/usr/bin/python3
''' LFU Caching '''
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    '''LFU Caching'''

    def __init__(self):
        '''Initialize LFU Cache'''
        super().__init__()
        self.f = {}

    def put(self, k, i):
        '''Add item to cache'''
        if k is None or i is None:
            return

        if k in self.cache_data:
            self.cache_data[k] = i
            self.f[k] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_f = min(self.f.values())
                min_keys = [x for x, v in self.f.items() if v == min_f]
                lfu_k = min(min_keys, key=self.f.get)
                self.cache_data.pop(lfu_k)
                self.f.pop(lfu_k)
                print("DISCARD:", lfu_k)

            self.cache_data[k] = i
            self.f[k] = 1
