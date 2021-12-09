'''
n명의 학생의 수학 점수가 주어진다. 
n명의 학생들의 평균(소수 첫째자리 반올림)을 구하고 
n명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하기.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고,
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 한다. 
'''

n = int(input())
scores = list(map(int,input().split()))

avg = round((sum(scores)/n)+0.5)
print(avg)
min = 2147000000
for idx, value in enumerate(scores):
    tmp = abs(value - avg)
    if tmp < min :
        min = tmp
        score = value
        res = idx + 1 
    elif tmp == min : 
        if value > score :
            score = value 
            res = idx + 1 
