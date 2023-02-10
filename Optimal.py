"""
--------- Link for the challenge: https://codeforces.com/contest/710/problem/B ---------

You are given n points on a line with their coordinates x(i).
Find the point x so the sum of distances to the given points is minimal.

Input
The first line contains integer n (1 ≤ n ≤ 3·10^5) — the number of points on the line.

The second line contains n integers xi ( - 10^9 ≤ x(i) ≤ 10^9) — the coordinates of the given n points.

Output
Print the only integer x — the position of the optimal point on the line.
If there are several optimal points print the position of the leftmost one.
It is guaranteed that the answer is always the integer.

Input:
4
1 2 3 4
Output:
2

"""
import math
sze = int(input())
lst = sorted(list(map(int, input().split())))
ans = math.ceil(sze / 2) - 1
print(lst[ans])