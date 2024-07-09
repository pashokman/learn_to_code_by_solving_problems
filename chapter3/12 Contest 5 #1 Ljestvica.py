"""
link to the task - https://dmoj.ca/problem/coci12c5p1
"""
n = input()

lenght_n = len(n)

C = ''
A = ''

if n[0]=='C' or n[0] == 'F' or n[0]=='G':
    C = C + n[0]
elif n[0] == 'A' or n[0] == 'D' or n[0] == 'E':
    A = A + n[0]

for i in range (lenght_n):
    if ((n[i]=='|' and n[i+1] == 'A') or (n[i]=='|' and n[i+1] == 'D') or 
        (n[i]=='|' and n[i+1] == 'E')):
        A = A + n[i+1]
    elif ((n[i]=='|' and n[i+1] == 'C') or (n[i]=='|' and n[i+1] == 'F') or 
        (n[i]=='|' and n[i+1] == 'G')):
        C = C + n[i+1]

if len(C) > len(A):
    print('C-dur')
elif len(C)< len(A):
    print('A-mol')

elif len(C) == len(A):
    if n[-1]== 'C':
        print('C-dur')
    elif n[-1] == 'A':
        print('A-mol')