"""
Solution for Level 2
Google Foobar

20/06/2021
"""
import random 

def solution(l, t):
    # print()
    # print(f"list: {l}")
    # print(f"target: {s}")
    # your code here 
    i, j = 0, 1
    total = l[i]
    found = False

    # if list only has single element 
    if len(l) == 1: 
        if total == t:
            found = True

    while j < len(l) and i < len(l):
        if total == t:
            found = True 
            break
        elif total < t:
            total += l[j]
            j += 1
        else: 
            total -= l[i]
            i += 1
    if not found: 
        i, j = -1, 0
    return [i, j - 1]


def main():
    # given test cases 
    lst = [4, 3, 5, 7, 8]
    target = 12
    print(solution(lst, target))

    lst = [1,2,3,4]
    target = 15
    print(solution(lst, target))

    lst = [4, 3, 10, 2, 8]
    target = 12
    print(solution(lst, target))

    # single element list that does not match 
    lst = [4]
    target = 5
    print(solution(lst, target))

    # single element list that does match 
    lst = [4]
    target = 4
    print(solution(lst, target))

    # random list that matches
    lst = random.sample(range(1, 100), 25)
    target = sum(lst[5:9])
    print(solution(lst, target))

    lst = random.sample(range(1, 100), 25)
    target = sum(lst[5:9])
    print(solution(lst, target))

    # list that does not match 
    lst = [79,87,99,23,56,53,30,40,1]
    target = 13
    print(solution(lst, target))



if __name__ == "__main__":
    main()