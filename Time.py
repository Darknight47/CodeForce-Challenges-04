"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/622/B --------

You are given the current time in 24-hour format hh:mm. Find and print the time after a minutes.

Note that you should find only the time after a minutes, see the examples to clarify the problem statement.

You can read more about 24-hour format here https://en.wikipedia.org/wiki/24-hour_clock.

Input
The first line contains the current time in the format hh:mm (0 ≤ hh < 24, 0 ≤ mm < 60).
The hours and the minutes are given with two digits (the hours or the minutes less than 10 are given with the leading zeroes).

The second line contains integer a (0 ≤ a ≤ 104) — the number of the minutes passed.

Output
The only line should contain the time after a minutes in the format described in the input.
Note that you should print exactly two digits for the hours and the minutes (add leading zeroes to the numbers if needed).

See the examples to check the input/output format.

Input:
23:59
10

Output:
00:09
"""
time = input().split(":")
extraTime = int(input())
tempMin = (int(time[0]) * 60) + int(time[1]) + extraTime
ansHour = int(tempMin / 60)
ansMin = tempMin % 60
hour = str(ansHour)
minutes = str(ansMin)
if(ansHour > 24):
    ansHour = ansHour % 24
    hour = str(ansHour)
if(ansHour == 24):
    hour = "00"
elif(ansHour < 10):
    hour = "0" + str(ansHour)
if(ansMin < 10):
    minutes = "0" + str(ansMin)

print(f"{hour}:{minutes}")
