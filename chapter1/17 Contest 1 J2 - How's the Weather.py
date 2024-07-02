"""
Woburn Challenge 2017-18 Round 1 - Junior Division

"Ugh, It's been so hot out lately, why does it have to be 32 degrees…"
"32 degrees? That's freezing!"

You've had quite enough of confusing conversations with Americans who assume you're using Fahrenheit when Celsius 
is clearly the way to go. Rather than argue with them, you've settled for writing a program to conveniently 
convert temperatures measured in degrees Celsius to Fahrenheit instead.

You came across the following formula, which holds true given that F is a temperature in degrees Fahrenheit while C
is that same temperature in degrees Celsius:

C = 5 / 9 * (F - 32)

Given a value of C, which is an integer between -40 and 40 (inclusive), determine the corresponding value of F, 
so that you can express the equivalent temperature in degrees Fahrenheit for the Americans' benefit.

It's guaranteed that C will be chosen such that F will come out to exactly an integer, but you may output it with 0 
or more digits after the decimal point.

Input Specification
The first and only line of input consists of a single integer, C.

Output Specification
Output a single integer, the temperature in degrees Fahrenheit which is equivalent to C degrees Celsius.

F = C / (5/9) + 32

Sample Input
20
Sample Output
68
"""


c_temp = int(input())
f_temp = c_temp / (5 / 9) + 32
print(int(f_temp))