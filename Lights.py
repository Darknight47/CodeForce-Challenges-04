"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/415/A ---------

Mashmokh works in a factory. At the end of each day he must turn off all of the lights.

The lights on the factory are indexed from 1 to n. There are n buttons in Mashmokh's room indexed from 1 to n as well.
If Mashmokh pushes button with index i, then each light with index not less than i that is still turned on turns off.

Mashmokh is not very clever. So instead of pushing the first button he pushes some of the buttons randomly each night.
He pushed m distinct buttons b1, b2, ..., bm (the buttons were pushed consecutively in the given order) this night.
Now he wants to know for each light the index of the button that turned this light off.
Please note that the index of button bi is actually b(i), not i.

Please, help Mashmokh, print these indices.

Input
The first line of the input contains two space-separated integers n and m (1 ≤ n, m ≤ 100),
the number of the factory lights and the pushed buttons respectively.
The next line contains m distinct space-separated integers b1, b2, ..., bm (1 ≤ b(i) ≤ n).

It is guaranteed that all lights will be turned off after pushing all buttons.

Output
Output n space-separated integers where the i-th number is index of the button that turns the i-th light off.

"""
n, m = map(int, input().split())
btns = list(map(int, input().split()))
arr = [0] * n
for i in range(m):
    temp = btns[i]
    for j in range(temp - 1, n):
        temp2 = arr[j]
        if(temp2 == 0):
            arr[j] = temp
        else:
            break
print(*arr)