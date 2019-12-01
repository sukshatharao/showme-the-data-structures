#!/usr/bin/env python
# coding: utf-8

# In[9]:


import hashlib
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
        
    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = "We are going to encode this string of data!".encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()


import datetime
class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp = self.last
            self.last = Block(timestamp, data, temp)
            self.last.previous_hash = temp

def get_utc_time():
      utc = datetime.datetime.utcnow()
      return utc.strftime("%d/%m/%Y %H:%M:%S")


blk0 = Block(get_utc_time(), "Indian Intelligence Information on Uri Attack", 0)
blk1 = Block(get_utc_time(), "Information on Ayodhya Verdict", blk0)
blk2 = Block(get_utc_time(), "Some more Information", blk1)
print(blk0.data)
print(blk0.hash)
print(blk0.timestamp)
print(blk1.previous_hash.data)

temp = LinkedList()
temp.append(get_utc_time(), "Some Information")
temp.append(get_utc_time(), "Another Information")
print(temp.last.data)
print(temp.last.previous_hash.data)


# In[ ]:





# In[ ]:




