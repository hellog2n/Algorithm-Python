import csv
import numpy as np

# 최빈값 구하기
def mode(arr):
    max_count=0
    mod_num=0
    arr = arr.tolist()
    counter = np.unique(arr)
    for c in counter:
        if max_count < arr.count(c):
            max_count = arr.count(c)
            mod_num = c
    return mod_num

# 표본 분산값 구하기
def variance(arr):
    return (1/(len(arr) -1) * (sum(np.power(arr, 2)) - (1/len(arr)) * sum(arr) ** 2))


def solution():
    data = []
    with open('ch2_data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        for line in reader:
            data.append(line[:])

        file.close()

    data = np.array(data[1:])
    data = data.astype(int)
    data = np.squeeze(data, axis=1)
    data = np.sort(data)
    print("="*100)
    print()
    print('*' * 20, " 통계학 과목 수강생의 학기말 성적을 크기순으로 정렬 ", '*' * 20)
    print(data)
    print("=" * 100)
    print()
    median = (len(data) + 1) / 2.0



    print("평균은 ", data.mean(), " 입니다.")
    print("중위수의 위치는 ", median, " 입니다.")
    print("중위수는 ", data[int(median-1)], " 입니다.")

    print("최빈값은 ", mode(data), " 입니다.")
    print("분산값은 ", round(variance(data), 4), " 입니다.")
    print("범위는 ", data.max() - data.min(), " 입니다.")
    print("최소값은 ", data.min(), " 입니다.")
    print("최대값은 ", data.max(), " 입니다.")



    print("아래사분위수의 위치는 ", int((median + 1) / 2.0), " 입니다.")
    print("아래사분위수는 ", data[int((median + 1) / 2.0) - 1], " 입니다.")
    print("위사분위수의 위치는 ", int(median + (median + 1) / 2.0), " 입니다.")
    print("위사분위수는 ",  data[int(median + (median + 1) / 2.0) - 1], " 입니다.")


if __name__ == "__main__":
    solution()

