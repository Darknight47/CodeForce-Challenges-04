"""
------ Link for the challenge: https://codeforces.com/problemset/problem/863/A -------

Let quasi-palindromic number be such number that adding some leading zeros (possible none) to it produces a palindromic string.

String t is called a palindrome, if it reads the same from left to right and from right to left.

For example, numbers 131 and 2010200 are quasi-palindromic, they can be transformed to strings "131" and "002010200", respectively, which are palindromes.

You are given some integer number x. Check if it's a quasi-palindromic number.

Input
The first line contains one integer number x (1 ≤ x ≤ 109). This number is given without any leading zeroes.

Output
Print "YES" if number x is quasi-palindromic. Otherwise, print "NO" (without quotes).

Input:
131

Output:
YES

"""
inputStr = input()
tempRev = inputStr[::-1]
ok = False
if(inputStr == tempRev):
    ok = True
else:
    zerosAdded = 0
    temp = list(inputStr)
    for i in reversed(temp):
        if(i != '0'):
            break
        else:
            zerosAdded += 1
    inputStr =inputStr.rjust(len(inputStr) + zerosAdded, "0")
    tempRev = inputStr[::-1]
    if(inputStr == tempRev):
        ok = True
print("YES" if ok else "NO")