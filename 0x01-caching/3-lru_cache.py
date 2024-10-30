#!/usr/bin/env python3
""" class LRUCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key)
                self.order.append(key)
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_used = self.order[0]
                self.order.pop(0)
                self.cache_data.pop(least_used)
                print("DISCARD: {}".format(least_used))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
    