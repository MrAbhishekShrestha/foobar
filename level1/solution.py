# level 1 
def solution(s):
    # your code here
    n = len(s)
    cuts = 0 
    isEven = (n % 2 == 0)
    while isEven:
        isValid = True
        count = 1
        m = n // 2**count
        testString = s[:m]
        index = m  
        for _ in range(2**count-1):
            checkString = s[index:index + m]
            if testString != checkString:
                isValid = False
                break
            index = index + m
        isEven = isValid
        if isEven:
            count += 1
            cuts += 1
            isEven = len(testString) % 2 == 0
    return 2**cuts

def main():
    word = "abab"
    print((word + word).find(word, 1))

if __name__ == "__main__":
    main()