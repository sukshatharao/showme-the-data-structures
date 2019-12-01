#!/usr/bin/env python
# coding: utf-8

# In[33]:


global dict

def huffman_encoding(data):
    global dict
    dict = {}
    for char in data:
        dict[char] = dict.get(char, 0) + 1
    huff_tree = {}
    temp = '1'
    for num in sorted(dict.items(), key = lambda x: x[1]):
        huff_tree[num[0]] = temp
        #print(huff_tree[num[0]], num, num[0])
        temp = '0' + temp

    encoded_data = ''
    for d in data:
        encoded_data += huff_tree[d]
    return encoded_data, huff_tree

def huffman_decoding(data,huff_tree):
    dict = {}
    for char in tree:
        dict[huff_tree[char]] = char
        #print(dict[huff_tree[char]])
    #print(huff_tree)
    temp = ''
    decoded_data = ''
    for d in data:
        if d == '1':
            decoded_data += dict[temp + d]
            temp = ''
        else:
            temp += d
            #print(temp)
    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    #print(tree)
    #print(encoded_data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))


# In[ ]:





# In[ ]:




