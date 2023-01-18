"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/373/A ---------

Cucumber boy is fan of Kyubeat, a famous music game.

Kyubeat has 16 panels for playing arranged in 4 × 4 table. When a panel lights up, he has to press that panel.

Each panel has a timing to press (the preffered time when a player should press it), and Cucumber boy is able to press at most k panels in a time with his one hand.
Cucumber boy is trying to press all panels in perfect timing, that is he wants to press each panel exactly in its preffered time.
If he cannot press the panels with his two hands in perfect timing, his challenge to press all the panels in perfect timing will fail.

You are given one scene of Kyubeat's panel from the music Cucumber boy is trying. Tell him is he able to press all the panels in perfect timing.

Input
The first line contains a single integer k (1 ≤ k ≤ 5) — the number of panels Cucumber boy can press with his one hand.

Next 4 lines contain 4 characters each (digits from 1 to 9, or period) — table of panels.
If a digit i was written on the panel, it means the boy has to press that panel in time i.
If period was written on the panel, he doesn't have to press that panel.

Output
Output "YES" (without quotes), if he is able to press all the panels in perfect timing.
If not, output "NO" (without quotes).

"""
presedWithOnHand = int(input())
total = presedWithOnHand * 2
diction = {}
for i in range(4):
    temp = list(input())
    for ch in temp:
        tempValue = diction.setdefault(ch, 0)
        tempValue += 1
        diction[ch] = tempValue
ok = True
for num in diction:
    tempKey = num
    tempValue = diction[num]
    if(tempValue > total and tempKey != "."):
        ok = False
        break

print("YES" if ok else "NO")