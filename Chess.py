"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/519/A -------------

A and B are preparing themselves for programming contests.

To train their logical thinking and solve problems better, A and B decided to play chess. During the game A wondered whose position is now stronger.

For each chess piece we know its weight:

    the queen's weight is 9,
    the rook's weight is 5,
    the bishop's weight is 3,
    the knight's weight is 3,
    the pawn's weight is 1,
    the king's weight isn't considered in evaluating position.
    The player's weight equals to the sum of weights of all his pieces on the board.

As A doesn't like counting, he asked you to help him determine which player has the larger position weight.

Input
The input contains eight lines, eight characters each — the board's description.

The white pieces on the board are marked with uppercase letters, the black pieces are marked with lowercase letters.

The white pieces are denoted as follows: the queen is represented is 'Q', the rook — as 'R', the bishop — as'B', the knight — as 'N', the pawn — as 'P', the king — as 'K'.

The black pieces are denoted as 'q', 'r', 'b', 'n', 'p', 'k', respectively.

An empty square of the board is marked as '.' (a dot).

It is not guaranteed that the given chess position can be achieved in a real game. Specifically, there can be an arbitrary (possibly zero) number pieces of each type, the king may be under attack and so on.

Output
Print "White" (without quotes) if the weight of the position of the white pieces is more than the weight of the position
of the black pieces, print "Black" if the weight of the black pieces is more than the weight of the white pieces and print "Draw"
if the weights of the white and black pieces are equal.

Input:
...QK...
........
........
........
........
........
........
...rk...
Output:
White

"""
white = 0
black = 0
for i in range(8):
    temp = list(input())
    for ch in temp:
        if(ch != '.'):
            if(ch.islower()):
                if(ch == 'q'):
                    black += 9
                elif(ch == 'r'):
                    black += 5
                elif(ch == 'b'):
                    black += 3
                elif(ch == 'n'):
                    black += 3
                elif(ch == 'p'):
                    black += 1
            else:
                if(ch == 'Q'):
                    white += 9
                elif(ch == 'R'):
                    white += 5
                elif(ch == 'B'):
                    white += 3
                elif(ch == 'N'):
                    white += 3
                elif(ch == 'P'):
                    white += 1 
       
if(white == black):
    print("Draw")
else:
    print("White" if white > black else "Black")                
