#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache_capacity = capacity
        self.cache_value = {}
        self.cache = deque()
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key is None:
            return -1
        return self.cache_value.get(key, -1)
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) >= self.cache_capacity:
            self.cache.popleft()
            self.cache_value= {}
        self.cache.append(key)
        self.cache_value[key] = value
        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(''))    # returns -1


# In[ ]:




