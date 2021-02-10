#  소수 구하기.
import sys


def is_prime(a):
    for i in range(2, a, 1):
        if a % i == 0:
            return False
    return True


a = int(sys.stdin.readline())

print(is_prime(7))
print(is_prime(11))
print(is_prime(8))
print(is_prime(9))
