"""
Magnus lost a game of chess to Kile so he found comfort in competitive programming. Very soon, he heard of the iconic 
COCI competition and decided to try his luck there.

He wrote a mail to Kile: "Dear Kile, please, prepare me for COCI. Magnus".

Kile replied: "You want to participate in COCI? All right, here's your warm-up task. 
A series of four consecutive letters of some word that make up the subword HONI (Croatian acronym for COCI) is called 
the HONI-block. I will send you the word of length N and you will throw out as many letters as you want 
(it might be none as well) so that in the end there are as many HONI-blocks as possible in the word. Kile".

Magnus was very worried and asked you, COCI competitive scene, for help. 
Help him determine the maximum number of HONI-blocks he can get in the final word.

Input
The first line contains a word of length N (1 <= N <= 100000), consisting of uppercase letters of the English alphabet.

Output
In the first and only line, print out the required number of HONI-blocks.

Sample Input 1
MAGNUS
Sample Output 1
0

Sample Input 2
HHHHOOOONNNNIIII
Sample Output 2
1
Explanation for Sample Output 2
By throwing out three letters H, O, N and I Magnus can get the word HONI, which contains one HONI-block.

Sample Input 3
PROHODNIHODNIK
Sample Output 3
2
"""

# 6/11 cases works
# word = input().upper()
# result = 0

# HONI_list = []
# if "H" in word:
#     start_index = word.index("H")
#     HONI_list.append("H")
#     for i in range(start_index+1, len(word)):
#         if word[i] == "O" and word[i] not in :
#             HONI_list.append(word[i])

#     HONI_word = ""
#     for i in HONI_list:
#         if i in "HONI" and i not in HONI_word:
#             HONI_word += i
#         else:
#             continue
        
#         if HONI_word == "HONI":
#             result += 1
#             HONI_word = ""

#     print(result)
# else:
#     print(result)


# 5/11 cases works
# word = input().upper()
# result = 0
# HONI_word = ""

# if "H" in word:
#     start_index = word.index("H")
#     HONI_word += "H"

#     for i in range(start_index+1, len(word)):
#         if word[i] == "O" and "O" not in HONI_word:
#             HONI_word += "O"
#         else:
#             if word[i] == "N" and "O" in HONI_word and "N" not in HONI_word:
#                 HONI_word += "N"
#             else:
#                 if word[i] == "I" and "N" in HONI_word and "I" not in HONI_word:
#                     HONI_word += "I"
#                     result += 1
#                     HONI_word = ""
#                 else:
#                     continue

#     print(result)
# else:
#     print(result)


# GPT solution
def count_honi_blocks(word):
    state = 0
    count = 0
    
    for char in word:
        if state == 0 and char == 'H':
            state = 1
        elif state == 1 and char == 'O':
            state = 2
        elif state == 2 and char == 'N':
            state = 3
        elif state == 3 and char == 'I':
            count += 1
            state = 0
    
    return count

# Read input
word = input().strip()

# Output the result
print(count_honi_blocks(word))