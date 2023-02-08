"""
------------- Link for the challenge: https://codeforces.com/problemset/problem/1272/A -------------

Three friends are going to meet each other. Initially, the first friend stays at the position x=a, the second friend stays at the position x=b and the third friend stays at the position
x = c on the coordinate axis Ox.

In one minute each friend independently from other friends can change the position x
by 1 to the left or by 1 to the right (i.e. set x:=x−1 or x:= x + 1) or even don't change it.

Let's introduce the total pairwise distance — the sum of distances between each pair of friends. Let a′
, b′ and c′ be the final positions of the first, the second and the third friend, correspondingly.
Then the total pairwise distance is |a′−b′|+|a′−c′|+|b′−c′|, where |x| is the absolute value of x.

Friends are interested in the minimum total pairwise distance they can reach if they will move optimally.
Each friend will move no more than once. So, more formally, they want to know the minimum total pairwise
distance they can reach after one minute.

You have to answer q independent test cases.

Input:
The first line of the input contains one integer q (1 ≤  q ≤ 1000) — the number of test cases.

The next q lines describe test cases. The i-th test case is given as three integers
a,b and c (1 ≤ a,b,c ≤ 10^9) — initial positions of the first, second and third friend correspondingly.
The positions of friends can be equal.

Output
For each test case print the answer on it — the minimum total pairwise distance
(the minimum sum of distances between each pair of friends) if friends change their positions optimally.
Each friend will move no more than once. So, more formally, you have to find the minimum total pairwise
distance they can reach after one minute.

Input:
8
3 3 4
10 20 30
5 5 5
2 4 3
1 1000000000 1000000000
1 1000000000 999999999
3 2 5
3 2 6

Output:
0
36
0
0
1999999994
1999999994
2
4


"""

cases = int(input())
for i in range(cases):
    lst = sorted(list(map(int, input().split())))
    same = False
    ans = 0
    if(lst[0] == lst[2]):
        same = True
    else:
        a = lst[0]
        b = lst[1]
        c = lst[2]
        if(a == b and a < c):
            a += 1
            b += 1
            if(c != a):
                c -= 1
        elif(a == b and a > c):
            a -= 1
            b -= 1
            if(c != a):
                c += 1
        elif(a == c and a < b):
            a += 1
            c += 1
            if(b != a):
                b -= 1
        elif(a == c and a > b):
            a -= 1
            c -= 1
            if(a != b):
                b += 1
        elif(b == c and b < a):
            b += 1
            c += 1
            if(b != a):
                a -= 1
        elif(b == c and b > a):
            b -= 1
            c -= 1
            if(a != b):
                a += 1
        else:
            if(a > b):
                a -= 1
            elif(a < b):
                a += 1
            if(b > a):
                b -= 1
            elif(b < a):
                b += 1
            if(c > a):
                c -= 1
            elif(c < a):
                c += 1
        ab = abs(a - b)
        ac = abs(a - c)
        bc = abs(b - c)
        ans = ab + ac + bc
    if(same):
        print(0)
    else:
        print(ans)