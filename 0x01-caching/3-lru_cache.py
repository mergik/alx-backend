#!/usr/bin/env python3
""" Module that defines BasicCache class/caching system """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Class that inherits from BaseCaching and implements LRU cache """
    def __init__(self):
        """ Init new instance variable as OrderedDict instead of dict """
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Put method to assign item value to key """
        if (key and item):
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        if (len(self.cache_data) > self.MAX_ITEMS):
            discard = self.cache_data.popitem(last=False)
            print('DISCARD: {}'.format(discard[0]))

    def get(self, key):
        """ Get method to return value at key """
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
