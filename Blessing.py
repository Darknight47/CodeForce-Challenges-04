"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/1749/B ----------

You are playing a computer game. To pass the current level, you have to kill a big horde of monsters.
In this horde, there are n monsters standing in the row, numbered from 1 to n. The i-th monster has a(i) health and a special
"Death's Blessing" spell of strength bi attached to it.

You are going to kill all of them one by one. It takes exactly h seconds to kill a monster with health h.

When the i-th monster dies, it casts its spell that increases the health of its neighbors by b(i)
(the neighbors of the j-th monster in the row are the monsters on places j−1 and j+1. The first and the last monsters
have only one neighbor each).

After each monster is killed, the row shrinks, so its former neighbors become adjacent to each other
(so if one of them dies, the other one is affected by its spell). For example, imagine a situation with 4 monsters
with health a=[2,6,7,3] and spells b=[3,6,0,5]. One of the ways to get rid of the monsters is shown below:

The first row represents the health of each monster, the second one — the power of the spells.
As a result, we can kill all monsters in 6+13+8+6 = 33 seconds. Note that it's only an example and may not be
the fastest way to get rid of the monsters.

What is the minimum time required to kill all monsters in the row?

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the number of monsters in the row.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the initial health of corresponding monsters.

The third line contains n integers b1,b2,…,bn (0 ≤ b(i) ≤ 10^9), where b(i) is the strength of the spell for the i-th monster.

It's guaranteed that the sum of n doesn't exceed 2⋅10^5.

Output
For each test case, print one integer — the minimum possible total time to kill all monsters.

Input:
4
1
10
0
3
100 1 100
1 100 1
4
2 6 7 3
3 6 0 5
2
1000000000 1000000000
1000000000 1000000000

Output:
10
203
26
3000000000

"""
cases = int(input())
while cases > 0:
    sze = int(input())
    keys = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    diction = list(zip(keys, values))
    sorted_by_value = sorted(diction, key= lambda x:x[1])
    answer = 0
    tempValue = 0
    for temp in sorted_by_value:
        answer += (temp[0] + tempValue)
        tempValue = temp[1]
    print(answer)
    cases -= 1