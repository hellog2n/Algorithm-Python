# MARK:- 구현 왕실의 나이트    (page. 115)

# 나이트가 현재 위치로부터 나아갈 수 있는 8가지의 경우의 수 (x, y)
steps = [(1, 2), (-1, 2), (2, -1), (2, 1), (-1, -2), (1, -2), (-2, 1), (-2, -1)]

def solution():
    pos = input()
    # 아스키코드를 이용하여 문자와 숫자를 받는다.
    pos = (ord(pos[0]) - 96, int(pos[1]))
    res = 0
    for step in steps:
        posNum = tuple(sum(elem) for elem in zip(step, pos))
        # 위치 범위를 넘어가면 무시한다.
        if posNum[1] < 1 or posNum[0] < 1 or posNum[1] > 8 or posNum[0] > 8:
            continue
        else:
        # 위치 범위를 넘어가지 않을 경우, 경우의 수를 더한다.
            res += 1
    print(res)

solution()

