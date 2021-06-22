"""
Level 2 - Task 2 
Elevator Maintenance
Google Foobar 

date: 20/06/2021
"""
def solution(l):
    # your code here 

    # pre processing each string -> list[int]
    for i in range(len(l)):
        l[i] = l[i].split(".")
        for x in range(len(l[i])):
            l[i][x] = int(l[i][x])

    # radix sort 
    for index in range(2, -1, -1):
        counting_sort_column(l, index)

    # # post processing each list[int] -> string 
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j] = str(l[i][j])
        l[i] = ".".join((l[i]))
    return l

def counting_sort_column(lst, index):
    # find max for this column 
    if len(lst[0]) >= index+1:
        max_item = lst[0][index]
    else: 
        max_item = 0 
    for elem in lst:
        if len(elem) >= index+1 and max_item < elem[index]:
            max_item = elem[index]
    
    # initialize count array 
    count_array = [None] * (max_item + 1)
    for i in range(len(count_array)):
        count_array[i] = []
    
    # update count array 
    for item in lst:
        if len(item) >= index+1:
            count_array[item[index]].append(item)
        else:
            count_array[0].append(item)
    
    # update input list 
    pos = 0 
    for i in range(len(count_array)):
        for j in range(len(count_array[i])):
            item = count_array[i][j]
            lst[pos] = item 
            pos += 1
    return lst 


def main():
    lst = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
    print(solution(lst))
    
    lst = [[1, 1, 2], [1, 0], [1, 3, 3], [1, 0, 12], [1, 0, 2]]
    # for k in range(2, -1, -1):
    #     print(counting_sort_column(lst, k))
    # print(counting_sort_column(lst, 1))



if __name__ == "__main__":
    main()