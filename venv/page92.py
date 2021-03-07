def solution():
    n, m, k = map(int, input().split())
    array = list(map(int, input().split()))
    sum = 0
    array.sort()
    maxNum = array[-1] # 최대값
    max2Num = array[-2]
    while m > 0:
        for i in range(k):
            sum += maxNum
            m -= 1
        sum += max2Num
        m -= 1
    return sum

def solution2():
    n, m, k = map(int, input().split())
    array = list(map(int, input().split()))
    sum = 0
    array.sort()
    maxNum = array[-1]  # 최대값
    max2Num = array[-2]
    sum = (m // (k + 1)) * (maxNum * k + max2Num) + (m % ( k + 1 )) * maxNum
    return sum

print(solution2())
