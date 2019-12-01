Design Least Recently Used (LRU) cache with O(1) operations. 
Dictionary in python stores the key value pairs and stores single value of keys as key:value pairs.  I have used Deques to keep track of values most used and least recently used. They support append, pop with approximately the same O(1) performance in either direction

Get Time complexity: O(1) Set Time complexity: O(1)

Space complexity of the LRU: O(5); [it is O(capacity); capacity defined by udacity is 5]