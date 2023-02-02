"""
------- Link for the challenge: https://codeforces.com/contest/63/problem/B ------------

In a strategic computer game "Settlers II" one has to build defense structures to expand and protect the territory.
Let's take one of these buildings. At the moment the defense structure accommodates exactly n soldiers.
Within this task we can assume that the number of soldiers in the defense structure won't either increase or decrease.

Every soldier has a rank — some natural number from 1 to k. 1 stands for a private and k stands for a general.
The higher the rank of the soldier is, the better he fights. Therefore, the player profits from having the soldiers
of the highest possible rank.

To increase the ranks of soldiers they need to train. But the soldiers won't train for free,
and each training session requires one golden coin. On each training session all the n soldiers are present.

At the end of each training session the soldiers' ranks increase as follows.
First all the soldiers are divided into groups with the same rank, so that the least possible number of groups is formed.
Then, within each of the groups where the soldiers below the rank k are present, exactly one soldier increases his rank by one.

You know the ranks of all n soldiers at the moment.
Determine the number of golden coins that are needed to increase the ranks of all the soldiers to the rank k.

Input
The first line contains two integers n and k (1 ≤ n, k ≤ 100).
They represent the number of soldiers and the number of different ranks correspondingly.
The second line contains n numbers in the non-decreasing order. The i-th of them, a(i),
represents the rank of the i-th soldier in the defense building (1 ≤ i ≤ n, 1 ≤ a(i) ≤ k).

Output
Print a single integer — the number of golden coins needed to raise all the soldiers to the maximal rank.

"""

n, k = map(int, input().split())
soldiers = list(map(int, input().split()))
answer = 0
while True:
    diction = {}
    for i in range(n):
        tempSoldier = soldiers[i]
        diction.setdefault(tempSoldier, [])
        diction[tempSoldier].append(tempSoldier)
    soldiers.sort()
    if soldiers.count(soldiers[0]) == len(soldiers) and soldiers[0] == k:
        break
    else:
        answer +=1
    soldiers.clear()
    for j in diction.values():
        tempSorted = sorted(j)
        if(tempSorted[0] != k):
            tempSorted[0] += 1
        soldiers.extend(tempSorted)
   
print(answer)