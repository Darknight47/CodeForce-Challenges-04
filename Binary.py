"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/976/A -----------

String can be called correct if it consists of characters "0" and "1" and there are no redundant leading zeroes.
Here are some examples: "0", "10", "1001".

You are given a correct string s.

You can perform two different operations on this string:

swap any pair of adjacent characters (for example, "101"  "110");
replace "11" with "1" (for example, "110"  "10").
Let val(s) be such a number that s is its binary representation.

Correct string a is less than some other correct string b iff val(a) < val(b).

Your task is to find the minimum correct string that you can obtain from the given one using the operations
described above. You can use these operations any number of times in any order (or even use no operations at all).

Input
The first line contains integer number n (1 ≤ n ≤ 100) — the length of string s.

The second line contains the string s consisting of characters "0" and "1".
It is guaranteed that the string s is correct.

Output
Print one string — the minimum correct string that you can obtain from the given one.

Input:
4
1001

Output:
100

"""
sze = int(input())
arr = list(input())
ans = ""
first = False
for ch in arr:
    if(ch == '1' and first == False):
        ans += ch
        first = True
    elif(ch == '0'):
        ans += ch
print(ans)