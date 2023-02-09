"""
Alperen is standing at the point (0,0). He is given a string s of length n and performs n moves.
The i-th move is as follows:

if s(i) = L, then move one unit left; if s(i) = R, then move one unit right;
if s(i) = U, then move one unit up; if s(i) = D, then move one unit down.

There is a candy at (1,1) (that is, one unit above and one unit to the right of Alperen's starting point).
You need to determine if Alperen ever passes the candy.
Input
The first line of the input contains an integer t(1 ≤ t ≤ 1000) — the number of testcases.

The first line of each test case contains an integer n(1 ≤ n ≤ 50) — the length of the string.

The second line of each test case contains a string s of length n
consisting of characters L, R, D, and U, denoting the moves Alperen makes.

Output
For each test case, output "YES" (without quotes) if Alperen passes the candy, and "NO" (without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Input:
7
7
UUURDDL
2
UR
8
RRRUUDDD
3
LLL
4
DUUR
5
RUDLL
11
LLLLDDRUDRD

Output:
YES
YES
NO
NO
YES
YES
NO


"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(input())
    y = 0
    x = 0
    ok = False
    for ch in lst:
        if(ch == 'U'):
            y += 1
        elif(ch == 'D'):
            y -= 1
        elif(ch == 'R'):
            x += 1
        elif(ch == 'L'):
            x -= 1
        if(x == 1 and y == 1):
            ok = True
            break
    print("YES" if ok else "NO")