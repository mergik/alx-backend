#!/usr/bin/env python3
""" Module that defines BasicCache class/caching system """
from typing import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Class that inherits from BaseCaching and implements LIFO cache """
    def __init__(self):
        """ Override cache_data instance variable """
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Put method to assign item value to key and delete most recent """
        if (key and item):
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                cache_list = list(self.cache_data.keys())
                discard = cache_list[self.MAX_ITEMS - 1]
                print('DISCARD: {}'.format(discard))
                del self.cache_data[discard]

    def get(self, key):
        """ Get method to return value at key """
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
