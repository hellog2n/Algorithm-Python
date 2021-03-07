def solution(money):
    summary = 0
    change = [500, 100, 50, 10]
    for i in change:
        summary += (money // i)
        money = (money % i)
    return summary, money



print(solution(1260))