I have used recursion to solve the problem. Initial check is to find if the user is in names or if the given user is in the list of users in the particular group. 
Else then I recursively check if the user in the group of users, if found I return true 
Else false


Time complexity: O(depth * no. of users) 
Space complexity: O(depth * no. of users)