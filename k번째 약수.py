# 자연수  p , k 
# p 를 k 로 나눌 때 나머지가 0이면 q 는 p의 약수이다. 

# n,k가 주어졌을 때 n의 약수 중 k 번째로 작은 수를 출력하는 프로그램을 작성 
# 만약 약수의 개수가 k보다 적어서 존재하지 않을 경우는 -1

# 1) my answer 
n, k = map(int,input().split())

num = [] 
for i in range (1, n+1):
    if n % i == 0 :
        num.append(i) 

if len(num) < k :
    print(-1)        
else:
    print(num[k-1])

# 2) 모범 답안

n, k = map(int, input().split())

cnt = 0 
for i in range(1,n+1):
    if n % i == 0 :
        cnt +=1 
    if cnt == k :
        print(i)
        break
else:
    print(-1)
