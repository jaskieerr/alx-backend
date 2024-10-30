#!/usr/bin/python3
'''lastinfirstout'''
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    '''lastinfirstout'''

    def __init__(self):
        '''lastinfirstout'''
        super().__init__()

    def put(self, key, item):
        '''lastinfirstout'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                popped = list(self.cache_data.keys())[-1]
                self.cache_data.pop(popped)
                print("DISCARD: {}".format(popped))
            self.cache_data[key] = item

    def get(self, key):
        '''lastinfirstout'''
        return self.cache_data.get(key)
