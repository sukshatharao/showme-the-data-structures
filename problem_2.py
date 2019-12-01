#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
def find_files(suffix, path , files= []):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    temp = suffix
    if path:
        temp = suffix + '/' + path
    for i in os.listdir(temp):
        temp1 = temp +  '/' + i
        if os.path.isfile(temp1) and temp1.endswith(".c"):
            files.append(temp1)
            #print(temp1)

        elif os.path.isdir(temp1):
            files = find_files(temp, i, files)
    return files
    return None

print(find_files('.', 'testdir'))

print("\n",find_files('.', ''))

print("\n",find_files('.', 'testdir/subdir3'))


# In[ ]:





# In[ ]:




