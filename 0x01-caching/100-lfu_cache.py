#!/usr/bin/env python3
""" LFUCache that inherits from BaseCaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.order = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                value = self.order[key] + 1
                self.order.pop(key)
                self.order[key] = value
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least = min(self.order, key=self.order.get)
                self.cache_data.pop(least)
                self.order.pop(least)
                print("DISCARD: {}".format(least))
            self.cache_data[key] = item
            self.order[key] = 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.order[key] += 1
        value = self.order[key]
        self.order.pop(key)
        self.order[key] = value
        return self.cache_data[key]
