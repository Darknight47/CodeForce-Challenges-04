"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/837/A ---------

You are given a text of single-space separated words, consisting of small and capital Latin letters.

Volume of the word is number of capital letters in the word.
Volume of the text is maximum volume of all words in the text.

Calculate the volume of the given text.

Input
The first line contains one integer number n (1 ≤ n ≤ 200) — length of the text.

The second line contains text of single-space separated words s1, s2, ..., si,
consisting only of small and capital Latin letters.

Output
Print one integer number — volume of text.

Input:
7
NonZERO

Output:
5

"""
leng = int(input())
strTemp = input().split()
answer = 0
for word in strTemp:
    wordLst = list(word)
    answerTemp = 0
    for ch in wordLst:
        if(ch.isupper()):
            answerTemp += 1
    if(answerTemp > answer):
        answer = answerTemp
print(answer)