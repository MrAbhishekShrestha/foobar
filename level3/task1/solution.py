"""
Google Foobar 
Challenge 3 
Task 1 

date: 26th June 2021
"""

from math import inf 

def solution(map):
    # your code here 
    height = len(map) # height  
    width = len(map[0]) # width
    memo = [None] * height
    for i in range(height):
        memo[i] = [None] * width
    
    # base 
    for i in range(height-1, -1, -1):
        for j in range(width-1, -1, -1):
            # exit 
            if i == height-1 and j == width-1:
                memo[i][j] = 1
            # wall 
            elif map[i][j] == 1:
                memo[i][j] = inf 
            # bottom row 
            elif i == height-1:
                if memo[i][j+1] != inf and memo[i][j+1] is not None:
                    memo[i][j] = memo[i][j+1] + 1
            # rightmost column
            elif j == width - 1:
                if memo[i+1][j] != inf and memo[i+1][j] is not None:
                    memo[i][j] = memo[i+1][j] + 1

    # for row in memo:
    #     print(row)
    # return 

    # fill up memo
    for i in range(height-1, -1, -1):
        for j in range(width-1, -1, -1):
            # if already numbered, skip 
            if memo[i][j] is not None:
                continue 
            up = down = left = right = inf
            # up 
            if i != 0:
                if memo[i-1][j] is not None:
                    up = memo[i-1][j]
            # down 
            if i != height - 1:
                if memo[i+1][j] is not None:
                    down = memo[i+1][j]
            # left 
            if j != 0:
                if memo[i][j-1] is not None:
                    left = memo[i][j-1]
            # right 
            if j != width - 1:
                if memo[i][j+1] is not None:
                    right = memo[i][j+1]
            if left == inf and right == inf and up == inf and down == inf:
                continue 
            else: 
                memo[i][j] = 1 + min(left, right, up, down)
    
    for row in memo:
        print(row)
    return 
                
    

def main():
    map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    # print(solution(map))

    map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    print(solution(map))

if __name__ == "__main__":
    main()
