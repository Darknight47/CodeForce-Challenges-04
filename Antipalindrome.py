"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/981/A ----------

A string is a palindrome if it reads the same from the left to the right and from the right to the left.
For example, the strings "kek", "abacaba", "r" and "papicipap" are palindromes,
while the strings "abb" and "iq" are not.

A substring s[l…r] (1 ≤ l ≤ r ≤ |s|) of a string s = s1s2…s|s| is the string slsl + 1…sr.

Anna does not like palindromes, so she makes her friends call her Ann.
She also changes all the words she reads in a similar way. Namely, each word s is changed into its longest substring that is not a palindrome.
If all the substrings of sare palindromes, she skips the word at all.

Some time ago Ann read the word s. What is the word she changed it into?

Input
The first line contains a non-empty string s with length at most 50 characters,
containing lowercase English letters only.

Output
If there is such a substring in s that is not a palindrome, print the maximum length of such a substring. Otherwise print 0.

Note that there can be multiple longest substrings that are not palindromes, but their length is unique.

Input:
mew

Output:
3

"""
text = input()
setTemp = set(text)
if(len(setTemp) == 1):
    answer = 0
else:
    if(text != text[::-1]):
        answer = len(text)
    else:
        text = text[:-1]
        reversedTemp = text[::-1]
        while text == reversedTemp:
            text = text[:-1]
            reversedTemp = text[::-1]
        answer = len(text)
print(answer)