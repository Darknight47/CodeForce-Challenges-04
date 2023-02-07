"""
-------------- Link for the challenge: https://codeforces.com/problemset/problem/1791/C ---------------

Timur initially had a binary string† s (possibly of length 0).
He performed the following operation several (possibly zero) times:

Add 0 to one end of the string and 1 to the other end of the string. For example, starting from the string 1011,
you can obtain either 010111 or 110110. You are given Timur's final string.
What is the length of the shortest possible string he could have started with?
A binary string is a string (possibly the empty string) whose characters are either 0 or 1.

Input:
The first line of the input contains an integer t (1 ≤ t ≤ 100) — the number of testcases.

The first line of each test case contains an integer n (1 ≤ n ≤ 2000) — the length of Timur's final string.

The second line of each test case contains a string s of length n consisting of characters 0 or 1, denoting the final string.

Output:
For each test case, output a single nonnegative integer — the shortest possible length of
Timur's original string. Note that Timur's original string could have been empty, in which case you should output 0.

Input:
9
3
100
4
0111
5
10101
6
101010
7
1010110
1
1
2
10
2
11
10
1011011010

Output:
1
2
5
0
3
1
0
2
4

"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    strTemp = input()
    ans = 0
    if(sze >= 2):
        while True:
            if(len(strTemp) == 0):
                ans == 0
                break
            elif(len(strTemp) >= 2):
                first = strTemp[0]
                second = strTemp[len(strTemp) - 1]
                if(first == '0' and second == '1' or 
                first == '1' and second == '0'):
                    strTemp = strTemp[1:-1]
                else:
                    ans = len(strTemp)
                    break
            elif(len(strTemp) == 1):
                ans = 1
                break
    elif(sze == 1):
        ans = 1
    print(ans)
    
    
    