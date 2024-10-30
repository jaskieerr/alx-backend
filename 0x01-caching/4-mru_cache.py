#!/usr/bin/python3
''' Most Recently Used '''
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    '''Most Recently Used'''

    def __init__(self):
        '''Most Recently Used'''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''Most Recently Used'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                popped = self.order.pop()
                self.cache_data.pop(popped)
                print("DISCARD: {}".format(popped))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        '''Most Recently Used'''
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
