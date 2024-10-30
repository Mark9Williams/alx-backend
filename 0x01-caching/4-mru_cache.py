#!/usr/bin/env python3
""" MRUCache that inherits from BaseCaching and is a caching system """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class """

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
                most_recent = self.order[-1]
                self.order.pop(-1)
                self.cache_data.pop(most_recent)
                print("DISCARD: {}".format(most_recent))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
