"""
13 Contest 3 #1 Riječi
https://dmoj.ca/problem/coci13c3p1
"""
def fibonacci(n):
    if n == 0:
        return 1, 0  # 1 A, 0 B
    elif n == 1:
        return 0, 1  # 0 A, 1 B
    
    # Starting values
    a, b = 1, 0
    c, d = 0, 1
    
    for _ in range(2, n+1):
        a, b = b, a + b
        c, d = d, c + d
    
    return c, d

# Number of presses
K = int(input())
A, B = fibonacci(K)
print(f"{A} {B}")