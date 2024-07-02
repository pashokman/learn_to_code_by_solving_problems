"""
Canadian Computing Competition: 2013 Stage 1, Junior #1
You know a family with three children. Their ages form an arithmetic sequence: 
the difference in ages between the middle child and youngest child is the same as the difference 
in ages between the oldest child and the middle child. 
For example, their ages could be 5, 10 and 15, since both adjacent pairs have a difference of 5 years.

Given the ages of the youngest and middle children, what is the age of the oldest child?

Input Specification
The input consists of two integers, each on a separate line. The first line is the age Y of the youngest child 0 <= Y <= 50. 
The second line is the age M of the middle child Y <= M <= 50.

Output Specification
The output will be the age of the oldest child.

Sample Input 1
12
15

Output for Sample Input 1
18

Sample Input 2
10
10

Output for Sample Input 2
10

"""


y = int(input())
m = int(input())

o = m - y
if m == y:
    print(y)
else:
    print(m - y + m)