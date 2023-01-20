"""
A few years ago, Hitagi encountered a giant crab, who stole the whole of her body weight.
Ever since, she tried to avoid contact with others, for fear that this secret might be noticed.

To get rid of the oddity and recover her weight, a special integer sequence is needed.
Hitagi's sequence has been broken for a long time, but now Kaiki provides an opportunity.

Hitagi's sequence a has a length of n. Lost elements in it are denoted by zeros.
Kaiki provides another sequence b, whose length k equals the number of lost elements in a (i.e. the number of zeros).
Hitagi is to replace each zero in a with an element from b so that each element in b should be used exactly once.
Hitagi knows, however, that, apart from 0, no integer occurs in a and b more than once in total.

If the resulting sequence is not an increasing sequence, then it has the power to recover Hitagi from the oddity.
You are to determine whether this is possible, or Kaiki's sequence is just another fake.
In other words, you should detect whether it is possible to replace each zero in a with an integer from b
so that each integer from b is used exactly once, and the resulting sequence is not increasing.

Input
The first line of input contains two space-separated positive integers n (2 ≤ n ≤ 100) and k (1 ≤ k ≤ n) —
the lengths of sequence a and b respectively.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 200) —
Hitagi's broken sequence with exactly k zero elements.

The third line contains k space-separated integers b1, b2, ..., bk (1 ≤ bi ≤ 200) —
the elements to fill into Hitagi's sequence.

Input guarantees that apart from 0, no integer occurs in a and b more than once in total.

Output
Output "Yes" if it's possible to replace zeros in a with elements in b and make the resulting sequence not increasing,
and "No" otherwise.

Input:
4 2
11 0 0 14
5 4

Output:
Yes
"""
sentimentSze, k = map(int, input().split())
sentiment = list(map(int, input().split()))
replacement = sorted(list(map(int, input().split())))
indx = k - 1
for i in range(sentimentSze):
    temp = sentiment[i]
    if(temp == 0):
        sentiment[i] = replacement[indx]
        indx -= 1
ok = False
for t in range(sentimentSze - 1):
    temp2 = sentiment[t + 1]
    temp1 = sentiment[t]
    if(temp2 < temp1):
        ok = True
        break
print("Yes" if ok else "No")

    