# 입력 : 1."babad" 2."cbbd"
# 출력 : 1."bab"   2."bb"

# 투포인터가 중앙을 중심으로 확장하는 형태로 풀이

def longestPalinfrome(string):
    # palindrome 판별 , 투 포인터 확장
    def expand(left, right):
        while left >= 0 and right <= len(string) and string[left] == string[right - 1]:
            left -= 1
            right += 1
        return string[left + 1:right - 1]

    # 해당 사항이 없을 때 빠르게 리턴
    if len(string) < 2 or string == string[::-1]:
        return string

    result = ''

    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(string)-1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)
    return result


print(longestPalinfrome("babad"))
print(longestPalinfrome("cbbd"))
