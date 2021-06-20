"""
Solution for Level 2
Google Foobar

20/06/2021
"""
import random 

def solution3(l, t):
    print()
    print(f"list: {l}")
    print(f"target: {t}")

    # your code here 
    i, j = 0, 1
    total = l[i]
    found = False 
    within_bounds = True
    while within_bounds:
        if total == t:
            found = True 
            break 
        elif total < t: 
            if j == len(l):
                within_bounds = False 
            else: 
                total += l[j]
                j += 1
        else: 
            if i == len(l) or i > j:
                within_bounds = False 
            else: 
                total -= l[i]
                i += 1
    if not found:
        i, j = -1, 0
    return [i, j-1]
            

def main():
    # given test cases 
    lst = [4, 3, 5, 7, 8]
    target = 12
    print(solution3(lst, target))

    lst = [1,2,3,4]
    target = 15
    print(solution3(lst, target))

    lst = [4, 3, 10, 2, 8]
    target = 12
    print(solution3(lst, target))

    # single element list that does not match 
    lst = [4]
    target = 5
    print(solution3(lst, target))

    # single element list that does match 
    lst = [4]
    target = 4
    print(solution3(lst, target))

    # random list that matches
    lst = random.sample(range(1, 100), 25)
    target = sum(lst[5:9])
    print(solution3(lst, target))

    lst = random.sample(range(1, 100), 25)
    target = sum(lst[21:22])
    print("lst: " + str(lst))
    print("target: " + str(target))
    print(solution3(lst, target))

    # list that does not match 
    lst = [79,87,99,23,56,53,30,40,1]
    target = 13
    print(solution3(lst, target))



    print("extra test cases")
    print(solution3([250,0,0], 250))
    print("required: "+ str([0,0]))
    print(solution3([1,2,3,4], 15))
    print("required: " + str([-1,-1]))
    print(solution3([4, 3, 10, 2, 8], 12))
    print("required: " + str([2,3]))
    print(solution3([4, 3, 5, 7, 8], 12))
    print("required: " + str([0,2]))
    print(solution3([260], 260))
    print("required: " + str([0,0]))

if __name__ == "__main__":
    main()