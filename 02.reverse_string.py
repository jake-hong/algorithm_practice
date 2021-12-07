# reverse_string (리스트로 입력된 문자열 뒤집기)

def reverseString(string):
    string.reverse()
    return string


hello = ["h", "e", "l", "l", "o"]
print(reverseString(hello))


# 투포인터를 이용한 뒤집기

def reverseString_twoPointer(string):
    left, right = 0, len(string) - 1
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    return string


hannah = ["h", "a", "n", "n", "a", "h"]
print(reverseString_twoPointer(hannah))
