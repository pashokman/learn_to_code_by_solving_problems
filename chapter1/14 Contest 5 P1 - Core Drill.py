"""
Simon got a new drill recently. Everyone knows that a drill is shaped like a right circular cone. 
Simon knows his drill has radius r and height h. But now he wants to calculate the volume. Write a program to help Simon!

Input Specification
The first line of input will have an integer  1 <= r <= 100.

The second line of input will have an integer 1 <= h <= 100.

Output Specification
The first line of output should have the volume of Simon's drill. 
The output will be accepted if it's within an absolute or relative error of 10**(-2)
.

Sample Input

3
5
Sample Output

47.12

Hint
V is the volume of the right circular cone with radius r and height h.

V = (pi * r**2 * h) / 3

"""
import math

r = int(input())
h = int(input())

V = (math.pi * r**2 * h) / 3

print(V)