"""
Canadian Computing Competition: 2015 Stage 1, Junior #2
We often include emoticons in our text messages to indicate how we are feeling. 
The three consecutive characters :-) indicate a happy face and the three consecutive characters :-( indicate a sad face. 
Write a program to determine the overall mood of a message.

Input Specification
There will be one line of input that contains between 1 and 255 characters.

Output Specification
The output is determined by the following rules:

If the input line does not contain any happy or sad emoticons, output - none.
Otherwise, if the input line contains an equal number of happy and sad emoticons, output - unsure.
Otherwise, if the input line contains more happy than sad emoticons, output - happy.
Otherwise, if the input line contains more sad than happy emoticons, output - sad.

Sample Input 1
How are you :-) doing :-( today :-)?
Output for Sample Input 1
happy

Sample Input 2
:)
Output for Sample Input 2
none

Sample Input 3
This :-(is str :-(:-a(nge te:-)xt.
Output for Sample Input 3
sad
"""


input_str = input()
happy = 0
sad = 0

if ":-)" in input_str or ":-(" in input_str:
    happy = input_str.count(":-)")
    sad = input_str.count(":-(")
    if happy == sad:
        print("unsure")
    elif happy > sad:
        print("happy")
    else:
        print('sad')
else:
    print("none")