my function takes input of suffix, path and list of required files which are found until that point in time. Each time I find a file ending with .c will be appended to this file. I have implemented this using the concept of recursion.

Run time complexity: O(Depth * Directories at every level on an average)

Space complexity: O(Depth)