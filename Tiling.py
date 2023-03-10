"""
----------- Link for the challenge: https://codeforces.com/contest/1150/problem/B ------

One day Alice was cleaning up her basement when she noticed something very curious:
an infinite set of wooden pieces! Each piece was made of five square tiles, with four
tiles adjacent to the fifth center tile:

By the pieces lay a large square wooden board. The board is divided into n2 cells arranged into n rows and n columns.
Some of the cells are already occupied by single tiles stuck to it. The remaining cells are free.
Alice started wondering whether she could fill the board completely using the pieces she had found.
Of course, each piece has to cover exactly five distinct cells of the board, no two pieces can overlap
and every piece should fit in the board entirely, without some parts laying outside the board borders.
The board however was too large for Alice to do the tiling by hand. Can you help determine if it's possible
to fully tile the board?

Input:
The first line of the input contains a single integer n(3 ≤ n ≤ 50) — the size of the board.

The following n lines describe the board. The i-th line (1 ≤ i ≤ n) contains a single string of length n.
Its j-th character (1 ≤ j ≤ n) is equal to "." if the cell in the i-th row and the j-th column is free;
it is equal to "#" if it's occupied.

You can assume that the board contains at least one free cell.

Output:
Output YES if the board can be tiled by Alice's pieces, or NO otherwise.
You can print each letter in any case (upper or lower).

Input:
3
#.#
...
#.#

Output:
YES
"""
sze = int(input())
lst = []
for i in range(sze):
    tempLst = list(input())
    lst.append(tempLst)
ok = True
for j in range(sze - 2):
    firstRow = lst[j]
    secondRow = lst[j + 1]
    thirdRow = lst[j + 2]
    ind = -1
    for z in range(sze):
        ch = firstRow[z]
        if(ch == '.' and z > 0 and z <= (sze - 2)):
            firstRow[z] = 'X'
            ind = z
            if(ind >= 1 and ind < (sze - 1)):
                chleft = secondRow[ind - 1]
                chmiddle = secondRow[ind]
                chright = secondRow[ind + 1]
                if(chleft == '.' and chmiddle == '.' and chright == '.'):
                    secondRow[ind - 1] = 'X'
                    secondRow[ind] = 'X'
                    secondRow[ind + 1] = 'X'
                else:
                    ok = False
                    break
            chthird = thirdRow[ind]
            if(chthird == '.'):
                thirdRow[ind] = 'X'
            else:
                ok = False
                break
for line in lst:
    if(line.count('.') > 0):
        ok = False
        break
print("YES" if ok else "NO")
        

   