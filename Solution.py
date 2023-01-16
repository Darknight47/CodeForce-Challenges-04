"""
--------- Link for the challenge: https://codeforces.com/contest/12/problem/B ------------

One cold winter evening Alice and her older brother Bob was sitting at home near the fireplace and giving each other interesting problems to solve.
When it was Alice's turn, she told the number n to Bob and said:

—Shuffle the digits in this number in order to obtain the smallest possible number without leading zeroes.

—No problem! — said Bob and immediately gave her an answer.

Alice said a random number, so she doesn't know whether Bob's answer is correct. Help her to find this out, because impatient brother is waiting for the verdict.

Input
The first line contains one integer n (0 ≤ n ≤ 109) without leading zeroes. The second lines contains
one integer m (0 ≤ m ≤ 109) — Bob's answer, possibly with leading zeroes.

Output
Print OK if Bob's answer is correct and WRONG_ANSWER otherwise.

Input:
3310
1033

Output:
OK
"""
numStr = input()
bobs = input()
numLst = list(numStr)
numLst.sort(key=int)
temp = int(numLst[0])
if(temp == 0 and len(numLst) > 1):
    t = numLst[1]
    numLst[0] = t
    numLst[1] = temp
answer = "".join([str(i) for i in numLst])
if(answer.__eq__(bobs)):
    print("OK")
else:
    print("WRONG_ANSWER")