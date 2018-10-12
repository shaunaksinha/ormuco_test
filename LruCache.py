#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:28:57 2018

@author: univac
"""
from collections import deque
from datetime import datetime

class LruCache():
    """ QUESTION C:
        Class for LRU Cache
    The implementation here uses a deque structure. It is not very 
    efficient for this requirement but to demonstrate the working of the LRU cache"""
    
    def __init__(self, size, expire_time):
        self.cache = deque(maxlen=size)
        self.time_cache = deque(maxlen=size) # queue to store time of addition of each element to cache
        self.expire_time = expire_time # time of expiry of elements in cache
        
    def add_items(self, item):
        """ Function to add items to self.cache and their corresponding addition time 
        to self.cache_time"""
        head = None
        tail = None
        if len(self.cache)>0:
            tail = self.cache[-1]
            head = self.cache[0]
        if item == head:
            self.time_cache.popleft()
            self.time_cache.appendleft(datetime.now())
            return # no modification to cache required
        if item == tail:
            self.cache.rotate(1) # move last element in cache to the front
            self.time_cache.pop()
            self.time_cache.appendleft(datetime.now())
            return
        elif item in self.cache:
            idx = self.cache.index(item)
            self.cache.remove(item) # remove item from cache using index
            del self.time_cache[idx] # remove corresponding time of entry
            
        self.cache.appendleft(item)
        self.time_cache.appendleft(datetime.now())        
        
    def remove_expired_items(self):
        """ Function to be called externally in order to remove expired items 
        from cache"""
        cache_items_to_remove = []
        time_cache_items_to_remove = []
        for i in range(len(self.cache)):
           diff_in_secs = (datetime.now()-self.time_cache[i]).total_seconds()
           if diff_in_secs > self.expire_time:
               #adding items to remove
               cache_items_to_remove.append(self.cache[i])
               time_cache_items_to_remove.append(self.time_cache[i])
       
        # removing expired items
        for i in range(len(cache_items_to_remove)):
            self.cache.remove(cache_items_to_remove[i])
            self.time_cache.remove(time_cache_items_to_remove[i])
               
    def print_items(self):
        print(self.cache)
        print(self.time_cache)
    
