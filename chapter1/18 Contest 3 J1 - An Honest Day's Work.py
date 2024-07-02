"""
Woburn Challenge 2018-19 Round 3 - Junior Division

Jessie, James, and Meowth, members of the honourable Team Rocket, have unfortunately fallen on hard times. 
With their funds necessarily allocated to constructing all manner of giant robots and other devices, 
they've been having difficulty affording any food lately. But that's nothing that an honest day's work can't fix!

James has a can of leftover paint, containing 1 <= P <= 100 litres of the stuff. When combined with his 
boundless collection of bottlecaps, this can result in some high-quality wares. When a bottlecap is artfully covered with 
1 <= B <= 100 litres of paint, it turns into a completely legitimate, Pokémon league-certified gym badge!

James will produce as many badges as he can using the paint, using exactly B litres each. 
Pokémon trainers love their gym badges, so each such badge is sure to sell for 1 <= D <= 100 Pokédollars.

There might still be some extra paint left over, once there's not enough for another complete badge. 
However, there's no need for it to go to waste - James will sell any remaining paint at a rate of 1 Pokédollar per litre.

How much money will James make for Team Rocket in total, from his sales of badges and leftover paint? Hopefully it'll be enough for at least a loaf of bread!

Input Specification
The first line of input consists of a single integer, P.
The second line consists of a single integer, B.
The third line consists of a single integer, D.

Output Specification
Output a single integer, the amount of money which James will make (in Pokédollars).

Sample Input
14
3
10

Sample Output
42

Sample Explanation
James has enough paint for 4 badges, which he'll then sell for 40 Pokédollars. That will leave him with 2 unused litres
of paint, which he'll sell for an additional 2 Pokédollars.
"""

paint_litres = int(input())
litres_per_badge = int(input())
badge_price = int(input())

badges_count = paint_litres // litres_per_badge
remaining_paint = paint_litres % litres_per_badge
total_sell_price = badges_count * badge_price + remaining_paint

print(total_sell_price)