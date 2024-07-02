"""
After seeing the first problem, you are probably very angry at the fact that you wasted a lot of time reading. 
For this problem, you should just count the number of words you have to read in a text. 
That's it. No tricks, no hidden catches. For the purposes of this problem, 
a word is any maximal contiguous group of non-whitespace characters.

Input Specification
The input will be a text with only lowercase letters and spaces (ASCII code 32). 
You should count how many words there are. The only constraint is that the length of the entire text will not exceed 80 
characters (because nobody likes essays). Also, there won't be anything tricky like double whitespace in a row, l
eading whitespace, or trailing whitespace because we don't roll like that. In fact, 
we won't even give you a trailing newline to deal with.

Output Specification
Output the number of words in the text.

Sample Input
Copy
problem one is really long
Sample Output
Copy
5

"""

text = input()
print(len(text.split()))