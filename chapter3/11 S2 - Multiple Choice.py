"""
Canadian Computing Competition: 2011 Stage 1, Senior #2
Your teacher likes to give multiple choice tests. One benefit of giving these tests is that they are easy to mark, 
given an answer key. The other benefit is that students believe they have a one-in-five chance of getting the 
correct answer, assuming the multiple choice possibilities are A, B, C, D or E.

Write a program that your teacher can use to grade one multiple choice test.

Input Specification
The input will contain the number N (0 <= N <= 10 000) followed by 2N lines. 
The 2N lines are composed of N lines of student responses (with one of A, B, C, D or E on each line), 
followed by N lines of correct answers (with one of A, B, C, D or E on each line), 
in the same order as the student answered the questions (that is, if line "i" is the student response, 
then line N+i will contain the correct answer to that question).

Output Specification
Output the integer C (0 <= C <= N) which corresponds to the number of questions the student answered correctly.

Sample Input 1
3
A
B
C
A
C
B
Output for Sample Input 1
1

Sample Input 2
3
A
A
A
A
B
A
Output for Sample Input 2
2
"""

question_number = int(input())
student_responses = []
correct_answers = []
correct_count = 0

for i in range(question_number):
    response = input()
    student_responses.append(response)

for j in range(question_number):
    answer = input()
    correct_answers.append(answer)

for r in range(question_number):
    if student_responses[r] == correct_answers[r]:
        correct_count += 1
    else:
        continue

print(correct_count)