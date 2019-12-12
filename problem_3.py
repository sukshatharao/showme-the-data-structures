#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sys
import queue

class Huffman_Node(object):
    def __init__(self, left = None, right = None, frequency = None, element = None):
        self.left = left
        self.right = right
        self.frequency = frequency
        self.element = element
    def __gt__(self, other):
        return self.frequency > other.frequency

def frequency_count(sentence):
    char_count = {}
    if not isinstance(sentence, str):
        return False
    for char in sentence:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    sorted_freq = [(value, key) for key, value in char_count.items()]
    return sorted_freq


def create_huffman_tree(frequencies):
    if not frequencies:
        return False
    priority_queue = queue.PriorityQueue()
    if len(frequencies) == 1:
        node = Huffman_Node(None, None, 0, None)
        priority_queue.put(node)
    for val in frequencies:
        node = Huffman_Node(frequency = val[0], element = val[1])
        priority_queue.put(node)
    while priority_queue.qsize() > 1:
        huff1 = priority_queue.get() # left
        huff2 = priority_queue.get() # right
        parent = Huffman_Node(huff1, huff2,  huff1.frequency + huff2.frequency)
        priority_queue.put(parent)

    tree = priority_queue.get()
    del priority_queue
    return tree


def encode_string(node, encoding_string = None, codes = None):
    if not node:
        return False
    if codes is None:
        codes = {}
    if encoding_string is None:
        encoding_string = ""
    if node.element:
        codes[node.element] = encoding_string
    encode_string(node.left, encoding_string + "0", codes)
    encode_string(node.right, encoding_string + "1", codes)
    return codes


def encode(codes, sentence):
    if not codes:
        return False
    output = "".join([codes[letter] for letter in sentence])
    return output


def decode_string(root, encoded_string):
    if not root or not encoded_string:
        return False
    node = root
    result = ""
    for char in encoded_string:
        if (node.left is None and node.right is None):
            result += node.element
            node = root;
        if char == '0':
            node = node.left
        else:
            node = node.right
    result += node.element
    return result


sentence = "The bird is the word."
frequencies = frequency_count(sentence)
print("frequencies is", frequencies)    
tree = create_huffman_tree(frequencies)
codes = {}
codes = encode_string(tree, "", codes)
encoded_string = encode(codes, sentence)
print("Encoded string:", encoded_string)
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_string, base=2))))
print("Decoded string:", decode_string(tree, encoded_string))


sentence = ""
frequencies = frequency_count(sentence)
print("\nfrequencies is", frequencies)    
tree = create_huffman_tree(frequencies)
codes = {}
codes = encode_string(tree, "", codes)
encoded_string = encode(codes, sentence)
print("Encoded string:", encoded_string)
if encoded_string:
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_string, base=2))))
print("Decoded string:", decode_string(tree, encoded_string))


sentence = "A"    
frequencies = frequency_count(sentence)
print("\nfrequencies is", frequencies)    
tree = create_huffman_tree(frequencies)
codes = {}
codes = encode_string(tree, "", codes)
encoded_string = encode(codes, sentence)
print("Encoded string:", encoded_string)
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_string, base=2))))
print("Decoded string:", decode_string(tree, encoded_string))

sentence = "AAA"
frequencies = frequency_count(sentence)
print("\nfrequencies is", frequencies)    
tree = create_huffman_tree(frequencies)
codes = {}
codes = encode_string(tree, "", codes)
encoded_string = encode(codes, sentence)
print("Encoded string:", encoded_string)
print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_string, base=2))))
print("Decoded string:", decode_string(tree, encoded_string))


# In[ ]:




