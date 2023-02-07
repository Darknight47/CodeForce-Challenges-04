"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/931/A ------------

Two friends are on the coordinate axis Ox in points with integer coordinates.
One of them is in the point x1 = a, another one is in the point x2 = b.

Each of the friends can move by one along the line in any direction unlimited number of times.
When a friend moves, the tiredness of a friend changes according to the following rules:
the first move increases the tiredness by 1, the second move increases the tiredness by 2,
the third — by 3 and so on. For example, if a friend moves first to the left, then to the right
(returning to the same point), and then again to the left his tiredness becomes equal to 1 + 2 + 3 = 6.

The friends want to meet in a integer point. Determine the minimum total tiredness they should gain,
if they meet in the same point.

Input
The first line contains a single integer a (1 ≤ a ≤ 1000) — the initial position of the first friend.

The second line contains a single integer b (1 ≤ b ≤ 1000) — the initial position of the second friend.

It is guaranteed that a ≠ b.

Output
Print the minimum possible total tiredness if the friends meet in the same point.

Input:
3
4
Output:
1

"""
import math
a = int(input())
b = int(input())
diff = abs(a - b)
half = 0
d = 0
asum = 0
bsum = 0
if(diff > 1):
    half = math.ceil(diff / 2)
    d = abs(diff - half)
    for i in range(half):
        asum += (i + 1)
    for j in range(d):
        bsum += (j + 1)
    ans = asum + bsum
elif(diff == 1):
    ans = 1
else:
    ans = 0
print(ans)