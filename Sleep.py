"""
------------- Link for the challenge: https://codeforces.com/contest/387/problem/A -----------

George woke up and saw the current time s on the digital clock. Besides, George knows that he has slept for time t.

Help George! Write a program that will, given time s and t, determine the time p when George went to bed.
Note that George could have gone to bed yesterday relatively to the current time (see the second test sample).

Input
The first line contains current time s as a string in the format "hh:mm".
The second line contains time t in the format "hh:mm" — the duration of George's sleep.
It is guaranteed that the input contains the correct time in the 24-hour format, that is, 00 ≤ hh ≤ 23, 00 ≤ mm ≤ 59.

Output
In the single line print time p — the time George went to bed in the format similar to the format of the time in the input.

Input:
05:50
05:44

Output:
00:06

"""
wakeup = input().split(":")
sleepTime = input().split(":")
wakeupHour = int(wakeup[0])
wakeupMinute = int(wakeup[1])
sleepHour = int(sleepTime[0])
sleepMinute = int(sleepTime[1])
answerHour = wakeupHour - sleepHour
answerMinute = wakeupMinute - sleepMinute
answerSeconds = 0
minTxt = ""
hourTxt = ""
if(answerMinute < 0):
    answerMinute += 60
    answerHour -= 1
if(answerHour < 0):
    answerHour += 24

if(answerMinute < 10):
    minTxt = "0" + str(answerMinute)
else:
    minTxt = answerMinute
if(answerHour < 10):
    hourTxt = "0" + str(answerHour)
else:
    hourTxt = answerHour
    
print(f"{hourTxt}:{minTxt}")