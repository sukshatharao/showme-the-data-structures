my function takes input of suffix, path until that point in time. I am using a set which is a unsorted collection. Each time I try to find a file ending with suffix will be appended to this set. Appending to the set is O(1) and for f files with "suffix", it is O(f)
We can think of this as working with a tree structure here where files act as leaves and directories act as internal nodes. I have implemented this using the concept of recursion. This traverses the entire tree to find matches given a query string.
Then estimate the number of nodes in the tree which will be = number of files + directories; since we have to visit every node once.

Run time complexity: O(n); n = number of nodes

Space Complexity : O(n*m) ; n is the number of calls and m being the space required for each frame.

however recursion does use additional overhead as it requires additional stack space for the functions arguments, rewinding the stack, passing control back to where the function was called, etc. Also, requires some additional time to complete these steps. The memory or space used is based on the number of recursive calls, which determines the number of stack frames times the space required for each stack frame. 
