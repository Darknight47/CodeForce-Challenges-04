"""
------ Link for the challenge: https://codeforces.com/problemset/problem/808/A ----------

Apart from having lots of holidays throughout the year, residents of Berland also have whole lucky years.
Year is considered lucky if it has no more than 1 non-zero digit in its number. So years 100, 40000, 5 are lucky
and 12, 3001 and 12345 are not.

You are given current year in Berland. Your task is to find how long will residents of Berland wait till
the next lucky year.

Input
The first line contains integer number n (1 ≤ n ≤ 109) — current year in Berland.

Output
Output amount of years from the current year to the next lucky one.

Input:
4 
Output:
1

"""
num = int(input())
if(num < 10):
    print(1)
else:
    zeros = len(str(num))
    firstNum = str(int(str(num)[0]) + 1)
    tempAns = int(firstNum + "0" * (zeros - 1))
    temp = abs(num - tempAns)
    print(temp)