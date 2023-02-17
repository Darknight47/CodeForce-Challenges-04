"""
---------- Link for the challenge: https://codeforces.com/contest/146/problem/B ------------

Petya loves lucky numbers very much. Everybody knows that lucky numbers are positive integers whose
decimal record contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and
5, 17, 467 are not.

Petya calls a mask of a positive integer n the number that is obtained after successive writing of all
lucky digits of number n from the left to the right. For example, the mask of number 72174994 is number
7744, the mask of 7 is 7, the mask of 9999047 is 47. Obviously, mask of any number is always a lucky number.

Petya has two numbers — an arbitrary integer a and a lucky number b. Help him find the minimum number
c (c > a) such that the mask of number c equals b.

Input
The only line contains two integers a and b (1 ≤ a, b ≤ 10^5). It is guaranteed that number b is lucky.

Output
In the only line print a single number — the number c that is sought by Petya.

Input:
1 7

Output:
7

"""
a, b = map(int, input().split())
ans = 0
while True:
    a += 1
    if(a == b):
        ans = b
        break
    else:
        temp = list(str(a))
        tempAns = ""
        for ch in temp:
            if(ch == '7' or ch == '4'):
                tempAns += ch
        if(len(tempAns) > 0):
            tempNum = int(tempAns)
            if(tempNum == b):
                ans = a
                break
print(ans)