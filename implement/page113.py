# MARK:- 구현 시각    (page. 113)



# 24시간의 초수는 최대값이 86400가지이므로 3중 for문이 가능하다...? 다른 방법이 있을지도 모른다.
def solution2():
    res = 0
    n = int(input())
    for hour in range(n+1):
        for minute in range(60):
            for seconds in range(60):
                if '3' in str(hour) + str(minute) + str(seconds):
                    res += 1

    print(res)
solution2()