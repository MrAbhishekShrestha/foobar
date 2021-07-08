"""
Google Foobar 
Level 3 task 2 
Bomb Baby
"""
def solution(x, y):
    """
    find number of turns it takes (generations) to find the gcd of x and y 
    as if x or y is a factor of the other, then the solution is impossible
    integer divide larger with smaller number to find number of generations 
    instead of repeatedly subtracting (optimized solution)
    need this optimization as integers x and y can be as large as 10^50
    """
    m, f = int(x), int(y)
    generation = 0 

    while (m != 1 and f != 1):
        if m < 1 or f < 1: 
            return "impossible"
        if max(m, f) % min(m, f) == 0:
            return "impossible"
        else: 
            generation += max(m, f)//min(m, f)
            m, f =  max(m, f)%min(m, f), min(m, f)
    return str(generation + max(m, f) - 1)

def main():
    # sample test cases 
    print(f"expected:1 |   got:{solution('2', '1')}")
    print(f"expected:4 |   got:{solution('4', '7')}")
    print(f"expected:impossible |   got:{solution('2', '4')}")

if __name__ == "__main__":
    main()