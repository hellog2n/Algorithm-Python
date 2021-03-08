# 1이 될 때까지

import math
def solution():
    n, k = map(int, input().split())
    result = 0
    result = int(math.log(n, k))
    result = result + (n % k)
    return result

def solution2():
    n, k = map(int, input().split())
    result = 0
    while n >= k:
        # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
        while n % k != 0:
            n -= 1
            result += 1
        n %= k
        result +=1

    while n > 1:
        n -= 1
        result += 1
    return result


def solution3():
    n, k = map(int, input().split())
    result = 0
    while True:
        # 정수로 만들어줌.
        target = (n // k) * k
        result += (n - target)
        n = target

        if n < k:
            break
        n //= k
        result += 1
    result += (n - 1)
    return result


print(solution3())

