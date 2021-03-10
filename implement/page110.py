# MARK:- 구현 상하좌  (page. 110)
우
#들어오는 문자의 값에 따라 위치 좌표를 리턴하게 한다.
def switchCase(x):
    global ctr
    return {'L': ctr[0], 'R':ctr[1], 'U': ctr[2], 'D': ctr[3]}.get(x, ctr[0])


# 시작 위치
origin = (1, 1)

# 입력에 따른 위치 좌표를 설정 한다.
ctr = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def solution():
    # N을 입력 받는다.
    n = int(input())
    plan = list(map(str, input().split()))
    global origin
    for planNum in plan:
        ctrNumber = switchCase(plan[planNum])

        # 튜플 값끼리 더한다.
        ctrSum = tuple(sum(elem) for elem in zip(ctrNumber, origin))
        # 기획서를 벗어나는 경우 무시한다.
        if ctrSum[0] == 0 or ctrSum[0] == n+1 or ctrSum[1] == 0 or ctrSum[1] == n+1:
            continue
        # 기획서 지도 안에 위치한 경우, 다음으로 나아간다.
        else:
            origin = ctrSum
    print(origin)



solution()