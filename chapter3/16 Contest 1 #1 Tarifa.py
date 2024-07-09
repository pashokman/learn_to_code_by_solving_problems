"""
Pero has negotiated a Very Good data plan with his internet provider. The provider will let Pero use up X megabytes 
to surf the internet per month. Each megabyte that he doesn't spend in that month gets transferred to the next month 
and can still be spent. Of course, Pero can only spend the megabytes he actually has.

If we know how many megabytes Pero has spent in each of the first N months of using the plan, 
determine how many megabytes Pero will have available in the N+1 month of using the plan.

Input Specification
The first line of input contains the integer X (1 <= X <= 100).
The second line of input contains the integer N (1 <= N <= 100).
Each of the following N lines contains an integer Pi (0 <= X <= 10000), the number of megabytes spent in each of the first N
months of using the plan. Numbers Pi will be such that Pero will never use more megabytes than he actually has.

Output Specification
The first and only line of output must contain the required value from the task.

Sample Input 1
10
3
4
6
2
Sample Output 1
28
Explanation for Sample Output 1
In the first month, out of 10 total megabytes, Pero has spent 4 and transferred 6 into the next month. In the second month, out of 
16 = (10+6) total megabytes, Pero has spent 6 and transferred 10. In the third month, out of 20 = (10 + 10) total megabytes, 
Pero has spent 2 and transferred 18. In the fourth month, he had a total of 28 megabytes to spend.

Sample Input 2
10
3
10
2
12
Sample Output 2
16

Sample Input 3
15
3
15
10
20
Sample Output 3
15
"""


data_plan = int(input())
month_count = int(input())
mb_spent = []

for i in range(month_count):
    mb_in_month = int(input())
    mb_spent.append(mb_in_month)

total_mb = data_plan * (month_count + 1)
mb_used = sum(mb_spent)

print(total_mb - mb_used)