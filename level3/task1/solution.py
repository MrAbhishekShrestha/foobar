"""
Google Foobar 
Challenge 3 
Task 1 

date: 26th June 2021
"""

from math import inf 

def solution(map):
    # your code here 
    n = len(map) # height  
    m = len(map[0]) # width
    memo = [None] * n
    for i in range(n):
        memo[i] = [None] * m
    
    # base 
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            # exit 
            if i == n-1 and j == m-1:
                memo[i][j] = 1
            # wall 
            elif map[i][j] == 1:
                memo[i][j] = inf 
            # bottom row 
            elif i == n-1:
                if memo[i][j+1] == 0:
                    memo[i][j] = 0 
                else:
                    memo[i][j] = memo[i][j+1] + 1
            # top row 
            elif j == m - 1:
                if memo[i+1][j] == 0:
                    memo[i][j] = 0 
                else:
                    memo[i][j] = memo[i+1][j] + 1
    
    # fill up memo
    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            # if wall, skip 
            if memo[i][j] == 0:
                continue 
            up = down = left = right = inf
            # up 
            if i!= 0:
                if memo[i-1][j] is not None:
                    up = memo[i-1][j]
            # down 
            
            # left 

            # right 
            

    return memo[0][0]
                
    

def main():
    map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    print(solution(map))

if __name__ == "__main__":
    main()
