"""
------- Link for the challenge: https://codeforces.com/problemset/problem/1150/A ------------

Welcome to Codeforces Stock Exchange! We're pretty limited now as we currently allow trading on one stock,
Codeforces Ltd. We hope you'll still be able to make profit from the market!

In the morning, there are n opportunities to buy shares.
The i-th of them allows to buy as many shares as you want, each at the price of s(i) bourles.

In the evening, there are m opportunities to sell shares.
The i-th of them allows to sell as many shares as you want, each at the price of b(i) bourles.
You can't sell more shares than you have.

It's morning now and you possess r bourles and no shares.

What is the maximum number of bourles you can hold after the evening?

Input
The first line of the input contains three integers n,m,r (1 ≤ n ≤ 30, 1 ≤ m ≤ 30 , 1 ≤ r ≤ 1000) —
the number of ways to buy the shares on the market, the number of ways to sell the shares on the market,
and the number of bourles you hold now.

The next line contains n integers s1,s2,…,sn (1 ≤ s(i) ≤ 1000);
s(i) indicates the opportunity to buy shares at the price of s(i) bourles.

The following line contains m integers b1,b2,…,bm (1 ≤ b(i) ≤ 1000);
b(i) indicates the opportunity to sell shares at the price of b(i) bourles.

Output
Output a single integer — the maximum number of bourles you can hold after the evening.

Input:
3 4 11
4 2 5
4 4 5 4

Output:
26

"""
import math
n, m, r = map(int, input().split())
buys = sorted(list(map(int, input().split())))
sells = sorted(list(map(int, input().split())))
buy = buys[0]
sell = sells[m - 1]
numOfStocks = math.floor(r / buy)
spent = numOfStocks * buy
left = r - spent
sold = numOfStocks * sell
ans = sold + left
if(ans < r):
    ans = r
print(ans)