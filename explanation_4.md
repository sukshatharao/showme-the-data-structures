I have used recursion to solve the problem. Initial check is to find if the user is in names or if the given user is in the list of users in the particular group. 
Else then I recursively check if the user in the group of users, if found I return true 
Else false
We can think of this as working with a tree structure here where user act as leaves and groups act as internal nodes. I have implemented this using the concept of recursion. This traverses the entire tree to find match the given string.
Then estimate the number of nodes in the tree which will be = number of files + directories; since we have to visit every node once.

Run time complexity: O(n); n = number of nodes

Space Complexity : O(n*m) ; n is the number of calls and m being the space required for each frame.

however recursion does use additional overhead as it requires additional stack space for the functions arguments, rewinding the stack, passing control back to where the function was called, etc. Also, requires some additional time to complete these steps. The memory or space used is based on the number of recursive calls, which determines the number of stack frames times the space required for each stack frame. 
