# 1부터 100사이의 자연수가 적힌 N장의 카드 
# 같은 숫자의 카드 여러장 
# 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록 
# 3장을 뽑을 수 있는 모든 경우 기록 
# 기록한 값 중 k 번째로 큰 수를 출력 

n, k = map(int, input().split())
number = list(map(int,input().split()))

res = set()

for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            res.add(number[i]+number[j]+number[l])

res = list(res)
res.sort(reverse=True)
print(res[k-1])


