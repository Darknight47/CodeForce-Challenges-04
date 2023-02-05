"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/168/A --------

Some country is populated by wizards. They want to organize a demonstration.

There are n people living in the city, x of them are the wizards who will surely go to the demonstration.
Other city people (n - x people) do not support the wizards and aren't going to go to the demonstration.
We know that the city administration will react only to the demonstration involving at least y percent of the city people.
Having considered the matter, the wizards decided to create clone puppets which can substitute the city people on
the demonstration.

So all in all, the demonstration will involve only the wizards and their puppets.
The city administration cannot tell the difference between a puppet and a person,
so, as they calculate the percentage, the administration will consider the city to be
consisting of only n people and not containing any clone puppets.

Help the wizards and find the minimum number of clones to create to that the demonstration
had no less than y percent of the city people.

Input
The first line contains three space-separated integers, n, x, y (1 ≤ n, x, y ≤ 10^4, x ≤ n) —
the number of citizens in the city, the number of wizards and the percentage the administration needs, correspondingly.

Please note that y can exceed 100 percent, that is, the administration wants to see on a demonstration
more people that actually live in the city ( > n).

Output
Print a single integer — the answer to the problem, the minimum number of clones to create,
so that the demonstration involved no less than y percent of n (the real total city population).

Input:
10 1 14

Output:
1

"""
import math
n, x, y = map(int, input().split())
if(y <= 100):
    temp = n * y
    temp2 = math.ceil(temp / 100)
    if(temp2 < x):
        print(0)
    else:
        diff = abs(temp2 - x)
        print(diff)
else:
    t = y * n
    t2 = math.ceil(t / 100)
    d = math.ceil(t2 - x)
    print(d)