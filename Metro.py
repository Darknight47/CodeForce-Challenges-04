"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/1055/A ----------------

Alice has a birthday today, so she invited home her best friend Bob. Now Bob needs to find a way to commute to the Alice's home.

In the city in which Alice and Bob live, the first metro line is being built. This metro line contains n stations numbered from 1 to n.
Bob lives near the station with number 1, while Alice lives near the station with number s. The metro line has two tracks.
Trains on the first track go from the station 1 to the station n and trains on the second track go in reverse direction.
Just after the train arrives to the end of its track, it goes to the depot immediately, so it is impossible to travel on it after that.

Some stations are not yet open at all and some are only partially open — for each station and for each track it is known whether the station is closed for that track or not.
If a station is closed for some track, all trains going in this track's direction pass the station without stopping on it.

When the Bob got the information on opened and closed stations, he found that traveling by metro may be unexpectedly complicated.
Help Bob determine whether he can travel to the Alice's home by metro or he should search for some other transport.

Input
The first line contains two integers n and s (2 ≤ s ≤ n ≤ 1000) — the number of stations in the metro and the number of the station where Alice's home is located.
Bob lives at station 1.

Next lines describe information about closed and open stations.

The second line contains n integers a1,a2,…,an (a(i)=0 or a(i)=1). If a(i)=1, then the i-th station is open on the first track
(that is, in the direction of increasing station numbers). Otherwise the station is closed on the first track.

The third line contains n integers b1,b2,…,bn (b(i)=0 or b(i)=1). If b(i)=1, then the i-th station is open on the second track
(that is, in the direction of decreasing station numbers). Otherwise the station is closed on the second track.

Output
Print "YES" (quotes for clarity) if Bob will be able to commute to the Alice's home by metro and "NO" (quotes for clarity) otherwise.

You can print each letter in any case (upper or lower).

Input:
5 3
1 1 1 1 1
1 1 1 1 1

Output:
YES

"""

stations, alice = map(int, input().split())
leftToRight = list(map(int, input().split()))
rightToLeft = list(map(int, input().split()))
firstStation = leftToRight[0]
aliceFirstTrack = leftToRight[alice - 1]
aliceSecondTrack = rightToLeft[alice - 1]
backStationOpen = False
ok = False
if(firstStation == 1 and aliceFirstTrack == 1):
    ok = True
elif(firstStation == 1):
    for i in range(stations):
        templTr = leftToRight[i]
        temprTl = rightToLeft[i]
        tempInd = i + 1
        if(templTr == 1 and temprTl == 1 and tempInd > alice):
            backStationOpen = True
            break
if(backStationOpen and aliceSecondTrack == 1):
    ok = True

print("YES" if ok else "NO")
            