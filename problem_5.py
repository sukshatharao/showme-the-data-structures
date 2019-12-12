#!/usr/bin/env python
# coding: utf-8

# In[41]:


import hashlib
class Block:
    def __init__(self, timestamp, data, previous_hash, previous_block, next= None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous_block = previous_block
        self.next = next
   
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp)+str(self.data)+str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

import datetime
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def append(self, timestamp, data):
        if len(data)<=0:
            return False
        if not self.head:
            self.head = Block(timestamp, data, None , None)
            self.tail = self.head
        else:
            temp = self.tail
            self.tail = Block(timestamp, data, temp , temp)
        self.size +=1     
            
    def printing(self):
        block_number = 0
        element = LinkedList()
        node = self.tail
        element.tail = Block(node.timestamp, node.data, node , None)
        prev = element.tail
        node = node.previous_block
        while(node):
            result = Block(node.timestamp, node.data, node , None)
            node = node.previous_block
            result.next = prev
            prev = result
        element.head = prev    
        while(block_number < self.size):
            print("Block number:", block_number)
            print("Data:", element.head.data)
            print("Hash:", element.head.hash)
            print("Timestamp:", element.head.timestamp)
            if element.head.next is None: print("None")
            else: print("Next Hash:",str.format(element.head.next.hash), "\n")
            element.head = element.head.next
            block_number+=1
        
        
def get_utc_time():
      utc = datetime.datetime.utcnow()
      return utc.strftime("%d/%m/%Y %H:%M:%S")


temp = LinkedList()
temp.append(get_utc_time(), "Some Information")
temp.append(get_utc_time(), "Another Information")
temp.append(get_utc_time(), "Indian Intelligence Information on Uri Attack")
temp.append(get_utc_time(), "Information on Ayodhya Verdict")
temp.printing()

result = temp.append(get_utc_time(), "")
print("Oooops!! you tried to append empty string into blockchain:" , result)  #result is false ; trying to append empty data


# In[ ]:





# In[ ]:





# In[ ]:




