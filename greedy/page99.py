# MARK:- Greedy 알고리즘 1이 될 때까지 (page. 99)

import math
def solution():
    n, k = map(int, input().split())
    result = 0
    # N이 K로 나누어 떨어질때 까지를 보는 것은 지수 관계를 보는 것과도 같다.
    # N = K ** result 식 관계에서 result를 구하기 위해서는 양변에 log를 취해주면 된다.
    result = int(math.log(n, k))
    result = result + (n % k)
    return result

# 책 풀이
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

