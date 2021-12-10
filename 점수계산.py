n = int(input())
ans = list(map(int,input().split()))
score = 0 
cnt = 0 

for i in ans :
    if i == 1:
        cnt += 1
        score += cnt 
    else:
        cnt = 0
print(score)