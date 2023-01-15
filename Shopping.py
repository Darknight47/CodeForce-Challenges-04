"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/1009/A ------------

Maxim wants to buy some games at the local game shop. There are n games in the shop, the i-th game costs ci.

Maxim has a wallet which can be represented as an array of integers. His wallet contains m bills,
the j-th bill has value aj.

Games in the shop are ordered from left to right, Maxim tries to buy every game in that order.

When Maxim stands at the position i in the shop, he takes the first bill from his wallet
if his wallet is empty then he proceeds to the next position immediately) and tries to buy the i-th game
using this bill. After Maxim tried to buy the n-th game, he leaves the shop.

Maxim buys the i-th game if and only if the value of the first bill (which he takes) from his wallet is greater
or equal to the cost of the i-th game. If he successfully buys the i-th game, the first bill from his wallet
disappears and the next bill becomes first. Otherwise Maxim leaves the first bill in his wallet
(this bill still remains the first one) and proceeds to the next game.

For example, for array c=[2,4,5,2,4] and array a=[5,3,4,6] the following process takes place: Maxim buys the first game using the first bill (its value is 5), the bill disappears, after that the second bill (with value 3) becomes the first one in Maxim's wallet, then Maxim doesn't buy the second game because c2>a2, the same with the third game, then he buys the fourth game using the bill of value a2 (the third bill becomes the first one in Maxim's wallet) and buys the fifth game using the bill of value a3.

Your task is to get the number of games Maxim will buy.

Input:
The first line of the input contains two integers n and m (1 ≤ n , m ≤ 1000) — the number of games and the number of bills in Maxim's wallet.

The second line of the input contains n integers c1,c2,…,cn (1 ≤ c(i) ≤ 1000), where c(i) is the cost of the i-th game.

The third line of the input contains m integers a1,a2,…,am (1 ≤ a(j) ≤ 1000), where a(j) is the value of the j-th bill from the Maxim's wallet.

Output:
Print a single integer — the number of games Maxim will buy.

Input:
5 4
2 4 5 2 4
5 3 4 6
Output:
3

"""

games, bills = map(int, input().split())
costs = list(map(int, input().split()))
moneys = list(map(int, input().split()))
tempMon = 0
goNext = True
answer = 0
tempMoney = moneys.pop(0)
for cost in costs:
    if(tempMoney >= cost):
        answer += 1
        if moneys:
            tempMoney = moneys.pop(0)
        else:
            break 
     
print(answer)    

    
