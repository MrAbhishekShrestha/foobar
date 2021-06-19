"""
Level 1
"""
def solution1(s):
    """
    Algorithm: 
    1. generate suffixes from len(s)//2
    2. start from the smallest suffix
    3. check if repeating the suffix == s 
    4. First suffix to match is the solution
    5. return its length
    """
    print("input word: " + s)
    # if odd length, then only viable pattern is a single repeated character
    if len(s) % 2 == 1:
        if s[0] * len(s) == s:
            return s[0], len(s)
            # return len(s)
        return s, 1

    # generate suffixes from len(s)//2
    sids = []
    for i in range(len(s)-1, len(s)//2 - 1, -1):
        sids.append(i)
        
    # for each suffix, check if repeating it forms input string 
    match = False
    for sufId in sids:
        suf_len = len(s) - sufId
        repeat = (len(s) - suf_len) // suf_len + 1
        checkString = s[sufId:] * repeat
        if checkString == s:
            match = True
            break 
    if not match: 
        sufId, repeat = 0, 1
    return s[sufId:], repeat
    # return repeat
    
def main():
    # given test cases 
    word = "abcabcabcabc"
    print(solution1(word))
    word = "abccbaabccba"
    print(solution1(word))

    # single repeated character of odd length 
    word = "aaaaa"
    print(solution1(word))

    # single repeated character of even length 
    word = "aaaa"
    print(solution1(word))

    # odd length with no repeating pattern 
    word = "abcdabc"
    print(solution1(word))
    
    # even length with no repeating pattern 
    word = "jklimhni"
    print(solution1(word))

if __name__ == "__main__":
    main()