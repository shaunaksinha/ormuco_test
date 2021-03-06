#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:15:50 2018

@author: univac
"""
import time
def check_line_overlap(x1, x2, x3, x4):
    """
    QUESTION A: 
    Accepts coordinates for 2 lines on the X-axis: (x1,x2) and (x3,x4) respectively
    and returns True is there is an overlap or False otherwise
    :param x1: float
    :param x2: float
    :param x3: float
    :param x4: float
    :return: boolean
    """
    # swapping coordinates to make x1>x2 for line 1 and x3>x4 for line 2
    if x2 < x1:
        temp = x1
        x1 = x2
        x2 = temp
    if x4 < x3:
        temp = x3
        x3 = x4
        x4 = temp
    
    if x3<x2 and x4>x1: # overlap conditions
        return True
    else: 
        return False
    
        
        
def compare_versions(version1, version2):
    """
    QUESTION B: 
    Accepts 2 string versions and returns 0 if they are equal, 1 if version1 > version2,
    or -1 if version1 < version2
    :param version1: A string
    :param version2: A string
    :return: integer
    """
    try:
        numeric_v1=float(version1) # convertion to numeric type
        numeric_v2=float(version2)
    except ValueError as e:
        print(e)
        return
 
    if numeric_v1==numeric_v2:
        return 0
    elif numeric_v1>numeric_v2:
        return 1
    else:
        return -1
    
def test_lru_cache():
    """ 
    QUESTION C:
    Function to test LruCache class
    """
    l = LruCache(5,10) # length of cache=5 and expiry time=10 secs
    l.add_items(90)
    l.add_items(87)
    l.add_items(36)
    l.add_items(50)
    l.add_items(10)
    print('Cache after adding 5 items')
    print(l.cache)
    print('Causing program to pause for 10 secs to demonstrate cache expiry')
    time.sleep(10)
    print('Adding item 36 which is already in cache')
    l.add_items(36)
    print(l.cache)
    l.remove_expired_items()
    print('cache after removing expired items')
    print(l.cache)