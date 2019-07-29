""""
https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
""""
"""
James found a love letter that his friend Harry has written to his girlfriend. 
James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

1. He can only reduce the value of a letter by 1 , i.e. he can change d to c, but he cannot change c to d or d to b.
2. The letter a may not be reduced any further.

Each reduction in the value of any letter is counted as a single operation. 
Find the minimum number of operations required to convert a given string into a palindrome.

For example, given the string [ s = cde ] , the following two operations are performed: cde → cdd → cdc.

Write a functionthat should return the integer representing the minimum number of operations needed to make the string a palindrome.

theLoveLetterMystery() function should have the following parameter(s):

s: a string
t= a intezer denoting no. of test cases.
"""
# python 3 Time Complexity O(m*n)

for i in range (int(input())): 
    string=input() 
    reverse_string=string[::-1] 
    changes=0 
    for i in range (len(string)):
        changes+=abs(ord(reverse_string[i])-ord(string[i])) 
    print(changes//2)
