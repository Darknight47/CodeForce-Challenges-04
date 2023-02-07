"""
-------- Link for the challenge: https://codeforces.com/contest/931/problem/B ------------

The last stage of Football World Cup is played using the play-off system.

There are n teams left in this stage, they are enumerated from 1 to n.
Several rounds are held, in each round the remaining teams are sorted in the order of their ids,
then the first in this order plays with the second, the third — with the fourth, the fifth — 
with the sixth, and so on. It is guaranteed that in each round there is even number of teams.
The winner of each game advances to the next round, the loser is eliminated from the tournament,
there are no draws. In the last round there is the only game with two remaining teams: the round
is called the Final, the winner is called the champion, and the tournament is over.

Arkady wants his two favorite teams to play in the Final. Unfortunately, the team ids are already determined,
and it may happen that it is impossible for teams to meet in the Final, because they are to meet in some earlier
stage, if they are strong enough. Determine, in which round the teams with ids a and b can meet.

Input
The only line contains three integers n, a and b (2 ≤ n ≤ 256, 1 ≤ a, b ≤ n) —
the total number of teams, and the ids of the teams that Arkady is interested in.

It is guaranteed that n is such that in each round an even number of team advance, and that a and b are not equal.

Output
In the only line print "Final!" (without quotes), if teams a and b can meet in the Final.

Otherwise, print a single integer — the number of the round in which teams a and b can meet.
The round are enumerated from 1.


"""
n, a, b = map(int, input().split())
teams = []
for i in range(n):
    teams.append(i + 1)
ans = 0
round = 1
tempLst = []
founded = False
final = False
while True:
    for x in range(0, len(teams), 2):
        first = teams[x]
        second = teams[x + 1]
        if((first == a and second == b) or (first == b and second == a)):
            ans = round
            founded = True
            if(len(teams) == 2):
                final = True
            break
        if(first == a and second != b):
            tempLst.append(first)
        elif(first == b and second != a):
            tempLst.append(first)
        elif(second == a and first != b):
            tempLst.append(second)
        elif(second == b and first != a):
            tempLst.append(second)
        elif(first != b and second != a):
            tempLst.append(first)
    if(founded == False):
        teams.clear()
        teams += tempLst
        tempLst.clear()
        if(len(teams) > 0):
            round += 1
        else:
            break
    else:
        break
if(final):
    print("Final!")
else:
    print(ans)
