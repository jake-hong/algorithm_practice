import collections
import re
# 유효한 팰린드롬, 데크 사용을 통해 최적화


def isPalindrome(string):
    # 자료형을 데크로 선언
    strs = collections.deque()

    for char in string:
        if char.isalnum():             # isalnum(): 문자, 숫자 판별 함수
            strs.append(char.lower())  # strs 리스트에 소문자로 변환하여 추가

    while(len(strs)) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))


# 슬라이싱을 사용한 palindrome

def isPalindrome_slicing(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


print(isPalindrome_slicing("A man, a plan, a canal: Panama"))
print(isPalindrome_slicing("race a car"))
