import sys

n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

#  l은 오름 차순일 경우
#  1 2 3 4 5 6 7 8 9 10

found = False
le = 0
ri = len(l) - 1

while le <= ri:
    mid = (le + ri) // 2
    if l[mid] == k:
        found = True
        break
    elif l[mid] < k:
        le = mid + 1
    elif l[mid] > k:
        ri = mid - 1

if found:
    print(1)
else:
    print(0)
