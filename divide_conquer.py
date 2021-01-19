# Divide and Conquer

def consecutive_sum(start, end):
    #  base_case
    if start == end:
        return start
    # 부분 문제를 반으로 나누기 위한 문제의 중앙 정의
    mid = (start + end) // 2
    # 각 부분 문제를 재귀적으로 풀고 난 후 답을 더함
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)


# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 293))
print(consecutive_sum(1, 304))
