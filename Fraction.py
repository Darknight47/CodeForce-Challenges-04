"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/854/A --------

Petya is a big fan of mathematics, especially its part related to fractions.
Recently he learned that a fraction is called proper iff its numerator is smaller
than its denominator (a < b) and that the fraction is called irreducible if its
numerator and its denominator are coprime (they do not have positive common divisors except 1).

During his free time, Petya thinks about proper irreducible fractions and converts them
to decimals using the calculator. One day he mistakenly pressed addition button ( + )
instead of division button (÷) and got sum of numerator and denominator that was equal
to n instead of the expected decimal notation.

Petya wanted to restore the original fraction, but soon he realized that it might
not be done uniquely. That's why he decided to determine maximum possible proper
irreducible fraction  such that sum of its numerator and denominator equals n.
Help Petya deal with this problem.

Input
In the only line of input there is an integer n (3 ≤ n ≤ 1000),
the sum of numerator and denominator of the fraction.

Output
Output two space-separated positive integers a and b, numerator and denominator
of the maximum possible proper irreducible fraction satisfying the given sum.

Input:
3
Output:
1 2

"""
import math
num = int(input())
arr = []
first = num - 1
second = 1
ans1 = 0
ans2 = 0
while True:
    gcd = math.gcd(first, second )
    diff = abs(first - second)
    if(gcd == 1):
        ans1 = second
        ans2 = first
    if(diff <= 1):
        break
    second += 1
    first -= 1
print(ans1, ans2)