"""
One summer evening, while curled up with her beloved Cheese-kun plushie, C.C. begins craving pizza. 
Although she would really like a large, extra-cheesy pizza, her stomach is willing to settle for anything. 
Without hesitation, she snatches up Lelouch's credit card and makes a very important phone call…

C.C. will be "absolutely" satisfied if the pizza she gets has a width of 3 units and an extra-cheesiness of at least 95%.
C.C. will be "fairly" satisfied if the pizza she gets has a width of 1 unit and an extra-cheesiness of at most 50%.
C.C. will be "very" satisfied with any other pizza she receives.

Input Specification
The first line of input will contain a single integer W (1 <= W <= 3), denoting the width of the pizza C.C. receives.
The second line of input will contain another integer C (0 <= C <= 100), representing the percentage of the pizza covered in extra cheese.

Output Specification
A single line containing C.C.'s satisfaction with her order in the form: "C.C. is M satisfied with her pizza."

Make sure your output matches this exactly, including any spacing and punctuation.

Here, M is a string describing her satisfaction, which will be one of: "absolutely", "fairly" or "very".

Sample Input
2
70
Sample Output
C.C. is very satisfied with her pizza.

Explanation
The pizza has a width of 2 units and a cheesiness of 70%. Since C.C. is neither absolutely nor fairly satisfied, she is very satisfied.
"""

width = int(input())
extra_cheesiness = int(input())

if width == 3 and extra_cheesiness >= 95:
    print("C.C. is absolutely satisfied with her pizza.")
elif width == 1 and extra_cheesiness <= 50:
    print("C.C. is fairly satisfied with her pizza.")
else:
    print("C.C. is very satisfied with her pizza.")