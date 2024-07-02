"""
Woburn Challenge 2016-17 Round 1 - Junior Division

Late October can be a rather frightening time of year. Night begins to fall ever earlier, 
ancient Pagan rituals make demons stir, and at the end of the month, hordes of small creatures 
can even be seen roaming the streets! It's a spooky sight if there ever was one.

But just how spooky is this demonic festival? Its spookiness level can, in fact, 
be measured and represented as a single integer 2 <= S <= 20. 
However, a simple number doesn't truly do the spooky sensation justice. As such, 
it can also be described with the word spoo...ooky, with exactly S o's.

Given the integer S, can you cast a spooky incantation on your computer to have it produce the corresponding spooky word?

Input Specification
The first and only line of input consists of a single integer S.

Output Specification
Output a single line consisting of a single string – the spooky word corresponding to the given value of S.

Sample Input
5

Sample Output
spoooooky

"""


o_numb = int(input())

result = "sp" + "o" * o_numb + "ky"

print(result)