"""
------- Link for the challenge: https://codeforces.com/contest/1790/problem/A -----

On March 14, the day of the number π is celebrated all over the world.
This is a very important mathematical constant equal to the ratio of the circumference of a circle to its diameter.

Polycarp was told at school that the number π is irrational, therefore it has an infinite number of digits in decimal notation.
He wanted to prepare for the Day of the number π by memorizing this number as accurately as possible.

Polycarp wrote out all the digits that he managed to remember. For example, if Polycarp remembered π as 3.1415, he wrote out 31415.

Polycarp was in a hurry and could have made a mistake, so you decided to check how many first digits of the number π Polycarp actually remembers correctly.

Input
The first line of the input data contains the single integer t (1 ≤ t ≤ 10^3) — the number of test cases in the test.

Each test case is described by a single string of digits n, which was written out by Polycarp.

The string n contains up to 30 digits.

Output
Output t integers, each of which is the answer to the corresponding test case,
that is how many first digits of the number π Polycarp remembers correctly.

Input:
9
000
3
4141592653
141592653589793238462643383279
31420
31415
314159265358
27182
314159265358979323846264338327
Output:
0
1
0
0
3
5
12
0
30

"""
cases = int(input())
piStr = "314159265358979323846264338327"
for i in range(cases):
    tempStr = list(input())
    ans = 0
    for j in range(30):
        ch = piStr[j]
        if(j < len(tempStr)):
            temp = tempStr[j]
            if(ch == temp):
                ans += 1
            else:
                break
        else:
            break
    print(ans)