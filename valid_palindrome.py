# 유효한 팰린드롬
def isPalindrome(string):

    strs = []
    for char in string:
        if char.isalnum():             # isalnum(): 문자, 숫자 판별 함수
            strs.append(char.lower())  # strs 리스트에 소문자로 변환하여 추가

    while len(strs) > 1:               # 리스트에 들어간 값 palindrome 여부 판별
        if strs.pop(0) != strs.pop():
            return False

    return True


# 테스트
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
