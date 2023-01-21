"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/810/A ----------

Noora is a student of one famous high school. It's her final year in school — she is going to study in university next year.
However, she has to get an «A» graduation certificate in order to apply to a prestigious one.

In school, where Noora is studying, teachers are putting down marks to the online class register, which are integers from 1 to k.
The worst mark is 1, the best is k. Mark that is going to the certificate, is calculated as an average of all the marks, rounded to 
the closest integer. If several answers are possible, rounding up is produced. For example, 7.3 is rounded to 7, but 7.5 and 7.8784 — to 8.

For instance, if Noora has marks [8, 9], then the mark to the certificate is 9, because the average is equal to 8.5 and rounded to 9,
but if the marks are [8, 8, 9], Noora will have graduation certificate with 8.

To graduate with «A» certificate, Noora has to have mark k.

Noora got n marks in register this year. However, she is afraid that her marks are not enough to get final mark k.
Noora decided to ask for help in the internet, where hacker Leha immediately responded to her request.
He is ready to hack class register for Noora and to add Noora any number of additional marks from 1 to k.
At the same time, Leha want his hack be unseen to everyone, so he decided to add as less as possible additional marks.
Please help Leha to calculate the minimal number of marks he has to add, so that final Noora's mark will become equal to k.

Input
The first line contains two integers n and k (1 ≤ n ≤ 100, 1 ≤ k ≤ 100) denoting the number of marks,
received by Noora and the value of highest possible mark.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ k) denoting marks received by Noora before Leha's hack.


Output
Print a single integer — minimal number of additional marks, that Leha has to add in order to change Noora's final mark to k.

Input:
2 10
8 9

Output:
4

"""
n, k = map(int, input().split())
nums = list(map(int, input().split()))
temp = 0
for i in nums:
    temp += i
grade = temp / n
if grade - int(grade) >= 0.5:
    grade = int(grade) + 1
else:
    grade = int(grade)
answer = 0
while(grade != k):
    temp += k
    answer += 1
    n += 1   
    grade =  temp / n
    if grade - int(grade) >= 0.5:
        grade = int(grade) + 1
    else:
        grade = int(grade)
print(answer)