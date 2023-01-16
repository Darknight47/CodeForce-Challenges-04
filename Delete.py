"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/1005/B -----------

You are given two strings s and t. In a single move, you can choose any of two strings and delete the first
(that is, the leftmost) character. After a move, the length of the string decreases by 1. You can't choose a string if it is empty.

For example:
    * by applying a move to the string "where", the result is the string "here",
    * by applying a move to the string "a", the result is an empty string "".
You are required to make two given strings equal using the fewest number of moves.
It is possible that, in the end, both strings will be equal to the empty string, and so, are equal to each other.
In this case, the answer is obviously the sum of the lengths of the initial strings.

Write a program that finds the minimum number of moves to make two given strings s and t equal.

Input:
The first line of the input contains s. In the second line of the input contains t. Both strings consist only of lowercase Latin letters. The number of letters in each string is between 1 and 2⋅105, inclusive.

Output:
Output the fewest number of moves required. It is possible that, in the end, both strings will be equal to the empty string, and so, are equal to each other. In this case, the answer is obviously the sum of the lengths of the given strings.

Input:
test
west

Output:
2

"""
first = input()
second = input()
if(len(first) <= 0):
    print(len(second))
elif(len(second) <= 0):
    print(len(second))
elif(first == second):
    print(0)
else:
    arr1 = list(first)
    arr2 = list(second)
    if(arr1[len(arr1) - 1] != arr2[len(arr2) - 1]):
        print(len(first) + len(second))
    else:
        indFirst = len(first) - 1
        indSecond = len(second) - 1
        equals = 0
        while True:
            tempFirst = arr1[indFirst]
            tempSecond = arr2[indSecond]
            indFirst -= 1
            indSecond -= 1
            if(tempFirst == tempSecond):
                equals += 1
            else:
                break
            if(indFirst < 0 or indSecond < 0):
                break
        sameFirst = len(first) - equals
        sameSecond = len(second) - equals
        print(sameFirst + sameSecond)
        