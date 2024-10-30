#!/usr/bin/python3
'''first in first out '''
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    '''first in first out'''

    def __init__(self):
        '''first in first out'''
        super().__init__()

    def put(self, key, item):
        '''u already know what's this'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                poped = next(iter(self.cache_data))
                self.cache_data.pop(poped)
                print("DISCARD: {}".format(poped))
            self.cache_data[key] = item

    def get(self, key):
        '''u already know what's this'''
        return self.cache_data.get(key)
