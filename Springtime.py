"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/989/A -----------

The landscape can be expressed as a row of consecutive cells, each of which either contains a flower of colour amber or buff or canary yellow, or is empty.

When a flower withers, it disappears from the cell that it originally belonged to, and it spreads petals of its colour in its two neighbouring cells
(or outside the field if the cell is on the side of the landscape). In case petals fall outside the given cells, they simply become invisible.

You are to help Kanno determine whether it's possible that after some (possibly none or all) flowers shed their petals,
at least one of the cells contains all three colours, considering both petals and flowers. Note that flowers can wither in arbitrary order.

Input
The first and only line of input contains a non-empty string s consisting of uppercase English letters 'A', 'B', 'C' and characters '.' (dots)
only (|s|≤100) — denoting cells containing an amber flower, a buff one, a canary yellow one, and no flowers, respectively.

Output
Output "Yes" if it's possible that all three colours appear in some cell, and "No" otherwise.

You can print each letter in any case (upper or lower).

Input:
.BAC.

Output:
Yes
"""
str = list(input())
lst = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
found = False
for i in range(len(str) - 2):
    temp = ""
    temp += str[i]
    temp += str[i + 1]
    temp += str[i + 2]
    if(lst.count(temp) > 0):
        found = True
        break
print("Yes" if found else "No")