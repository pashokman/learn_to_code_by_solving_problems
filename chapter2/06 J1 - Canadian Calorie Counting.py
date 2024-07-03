"""
Canadian Computing Competition: 2006 Stage 1, Junior #1
At Chip's Fast Food emporium there is a very simple menu. Each food item is selected by entering a digit choice.

Here are the three burger choices:
1 – Cheeseburger (461 Calories)
2 – Fish Burger (431 Calories)
3 – Veggie Burger (420 Calories)
4 – no burger	Here are the three drink choices:
1 – Soft Drink (130 Calories)
2 – Orange Juice (160 Calories)
3 – Milk (118 Calories)
4 – no drink

Here are the three side order choices:
1 – Fries (100 Calories)
2 – Baked Potato (57 Calories)
3 – Chef Salad (70 Calories)
4 – no side order	Here are the three dessert choices:
1 – Apple Pie (167 Calories)
2 – Sundae (266 Calories)
3 – Fruit Cup (75 Calories)
4 – no dessert
Write a program that will compute the total Calories of a meal.

Input Specification
The program should input a number for each type of item then calculate and display the Calorie total. The first line will be the customer's choice of burger, the second will be the choice of side, then drink, then dessert. You may assume that each input will be a number from 1 to 4. That is, each customer has to pick exactly one number from each of the four options out of each of the four categories.

Output Specification
The program prints out the total Calories of the selected meal, and stops executing after this output.

Sample Input
2
1
3
4

Sample Output
Your total Calorie count is 649.

Explanation
The customer chose Burger #2, Side #1, Drink #3 and Dessert #4.
"""
# This solution works but did not submiting
# burgers_cal = [461, 431, 420, 0]
# other_cal = [100, 57, 70, 0]
# drink_cal = [130, 160, 118, 0]
# desert_cal = [167, 266, 75, 0]
# orders = []
# sum_cal = 0

# for i in range(4):
#     order_n = int(input())
#     orders.append(order_n)

# sum_cal = burgers_cal[orders[0]-1] + other_cal[orders[1]-1] + drink_cal[orders[2]-1] + desert_cal[orders[3]-1]

# print(f"Your total Calorie count is {sum_cal}.")


# This solution submits correct.
burgerlist = [0, 461, 431, 420, 0]
sideslist = [0, 100, 57, 70, 0]
drinklist = [0, 130, 160, 118, 0]
dessertlist = [0, 167, 266, 75, 0]
 
print("Welcome to Chip’s Fast Food Emporium")
burger_no = int(input("Please enter a burger choice: "))
side_no = int(input("Please enter a side order choice: "))
drink_no = int(input("Please enter a drink choice: "))
dessert_no = int(input("Please enter a dessert choice: "))
 
totalCalorie = burgerlist[burger_no] 
+ sideslist[side_no] + drinklist[drink_no] + dessertlist[dessert_no]
 
print("Your total Calorie count is {}.".format(totalCalorie))