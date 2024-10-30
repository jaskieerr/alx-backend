#!/usr/bin/python3
''' 0x01-caching '''
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    '''class cachiiing'''

    def put(self, key, item):
        '''adds keyvalue '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''retreives value for a key'''
        return self.cache_data.get(key)
