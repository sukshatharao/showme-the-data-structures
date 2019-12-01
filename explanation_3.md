I have calculated the occurences of characters in the given string. Then I went on to encode the character with highest occurence using minimum code length. so at every step, the length is increased by appending zeros as follows: first, 1 then next character has 01 and then 001 and this goes on.

Time complexity: O(n) 
Space complexity: O(unique characters)