"""
---------- Link for the challenge: https://codeforces.com/contest/710/problem/A ---------

The only king stands on the standard chess board. You are given his position in format
"cd", where c is the column from 'a' to 'h' and d is the row from '1' to '8'.
Find the number of moves permitted for the king.

Check the king's moves here https://en.wikipedia.org/wiki/King_(chess).

Input
The only line contains the king's position in the format "cd", where 'c' is the column from 'a' to 'h' and 'd' is the row from '1' to '8'.

Output
Print the only integer x — the number of moves permitted for the king.

Input:
e4
Output:
8
"""
pos = input()
column = pos[0]
row = pos[1]
ans = 0
if(row == '1' or row == '8'):
    if(column == 'a' or column == 'h'):
        ans = 3
    else:
        ans = 5
elif(column == 'a' or column == 'h'):
    if(row == '1' or row == '8'):
        ans = 3
    else:
        ans = 5
else:
    ans = 8  
print(ans)