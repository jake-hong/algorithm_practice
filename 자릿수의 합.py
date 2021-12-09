def digit_sum(x):
    res = 0
    while x != 0:
        res += x % 10
        x = x // 10
    return res

'''
def digit_sum(x):
    res = [int(i) for i in srt(x)]
    return sum(res) 
'''

n = int(input())
a = list(map(int,input().split()))

max = 0 

for x in a :
    tot = digit_sum(x)
    if max < tot:
        max = tot
        res = x 
print(x)