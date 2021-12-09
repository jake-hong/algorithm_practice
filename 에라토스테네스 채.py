n = int(input())

# 목록 구하기 
'''
ch = [True] * n 

m = int(n ** 0.5)
for i in range(2, m+1):
    print(ch)
    if ch[i] == True:
        for j in range(i+1,n,i):
            ch[j] = False

print([i for i in range(2,n) if ch[i]==True])
'''
# 개수 구하기 
# 
ch = [0] * (n+1)
cnt = 0 

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1 
        for j in range(i, n+1,i):
            ch[j] = 1 
print(cnt)
