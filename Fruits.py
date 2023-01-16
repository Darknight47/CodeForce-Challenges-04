"""
------- Link for the challenge: https://codeforces.com/contest/12/problem/C ------------

The spring is coming and it means that a lot of fruits appear on the counters.
One sunny day little boy Valera decided to go shopping. He made a list of m fruits he wanted to buy.
If Valera want to buy more than one fruit of some kind, he includes it into the list several times.

When he came to the fruit stall of Ashot, he saw that the seller hadn't distributed price tags to the goods,
but put all price tags on the counter. Later Ashot will attach every price tag to some kind of fruits,
and Valera will be able to count the total price of all fruits from his list. But Valera wants to know now what
can be the smallest total price (in case of the most «lucky» for him distribution of price tags) and the largest
total price (in case of the most «unlucky» for him distribution of price tags).

Input
The first line of the input contains two integer number n and m (1 ≤ n, m ≤ 100) — the number of price tags
(which is equal to the number of different kinds of fruits that Ashot sells) and the number of items in Valera's list.
The second line contains n space-separated positive integer numbers. Each of them doesn't exceed 100 and stands for
the price of one fruit of some kind. The following m lines contain names of the fruits from the list.
Each name is a non-empty string of small Latin letters which length doesn't exceed 32.
It is guaranteed that the number of distinct fruits from the list is less of equal to n.
Also it is known that the seller has in stock all fruits that Valera wants to buy.

Output
Print two numbers a and b (a ≤ b) — the minimum and the maximum possible sum which Valera may need to buy all fruits from his list.

Input:
5 3
4 2 1 10 5
apple
orange
mango

Output:
7 19

"""
tags, lstSze = map(int, input().split())
fruits = list(map(int, input().split()))
sorted_fruits = sorted(fruits)
dicFruit = {}
for i in range(lstSze):
    tempKey = input()
    tempValue = dicFruit.setdefault(tempKey, 0)
    tempValue += 1
    dicFruit[tempKey] = tempValue
sorted_fruits_by_numbers = sorted(dicFruit.items(), key= lambda x:x[1])
min = 0
max = 0
indxForward = 0
indxBackward = tags - 1
for tempFruit in reversed(sorted_fruits_by_numbers):
    tempNum = tempFruit[1]
    tempCostMin = sorted_fruits[indxForward]
    tempCostMax = sorted_fruits[indxBackward]
    indxForward += 1
    indxBackward -= 1
    min += tempNum * tempCostMin
    max += tempNum * tempCostMax
print(min ,  max)