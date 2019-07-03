https://www.hackerrank.com/challenges/the-minion-game/problem

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S .
Both players have to make substrings using the letters of the string S .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string S.


def minion_game(string):
    l=len(string)
    vowels='AEIOU'
    kevin=0
    stuart=0
    for i in range(l):
        if string[i] in vowels:
            kevin+=l-i
        else:
            stuart+=l-i
    if kevin>stuart:
        print('Kevin',+' '+str(kevin))
    elif stuart>kevin:
        print('Stuart'+' '+str(stuart))
    else:
        print('Draw')
    return 0


s = input()
minion_game(s)
