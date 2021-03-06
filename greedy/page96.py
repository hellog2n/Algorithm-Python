# MARK:- Greedy 알고리즘 카드 숫자 놀이 (page. 96)
import time

def solution():
    n, m = map(int, input().split())
    # 배열을 한 줄씩 이어 받는다.
    array = [map(int, input().split()) for _ in range(n)]

    # 가장 작은 숫자들 중 큰 수를 찾는다.
    number = max([ min(i) for i in array])
    return number

# 책 풀이
def solution2():
    n, m = map(int, input().split())
    result = 0
    # 한 줄씩 이어받아 확인한다.
    for i in range(n):
        array = map(int, input().split())
        minValue = min(array)
        result = max(minValue, result)
    return result

# 시간 재보기
start = time.time()
print(solution2())
print(time.time() - start)
