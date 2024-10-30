#!/usr/bin/python3
'''  Least Recently Used eviction '''
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    ''' Least Recently Used eviction'''

    def __init__(self):
        ''' Least Recently Used eviction'''
        super().__init__()
        self.order = []

    def put(self, key, item):
        ''' Least Recently Used eviction'''
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                popped = self.order.pop(0)
                self.cache_data.pop(popped)
                print("DISCARD: {}".format(popped))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        ''' Least Recently Used eviction'''
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
