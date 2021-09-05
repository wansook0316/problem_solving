from pprint import pprint
from functools import reduce

# 정렬된 것을 기반으로 생각한다.


def solution(lines):
    # 핵심.. : 끝나는 시간은 정렬되어 있다.
    # 그렇다면 끝나는 시간기준으로 하나씩 볼때, 끝나는 시간 +1초 사이에 들어오는 요청을 구하자.
    # i번째 끝나는 시간 이전의 요청은 i번째 끝나는 시간 + 1 초 사이에 들어오는 구간에 절대 들어올 수 없다.
    # 그렇다면 i번째 끝나는 시간보다 더 늦게 끝나는 요청의 경우가 몇개 들어오는지 알아야 한다.
    # 다음 요청의 시작시간이 지금 끝나는 시간보다 작기만 하면 무조건 처리된다.
    # 이게 당연한거네.. 왜냐면 처리되는 중간이 무조건 걸리기 때문..

    # e - s + 1 = 시간
    # s = e - 시간  + 1

    start_time = []
    end_time = []

    for line in lines:
        splited = line.split()
        end_t = time_to_sec(splited[1])
        start_time.append(end_t - float(splited[2][:-1]) * 1000 + 1)
        end_time.append(end_t)

    answer = 0
    for i in range(len(lines)):
        end_t = end_time[i] + 1000

        count = 0
        for j in range(i, len(lines)):
            if start_time[j] < end_t:
                count += 1

        answer = max(answer, count)

    return answer


def time_to_sec(line):
    splited = list(map(float, line.split(":")))
    h = splited[0] * 3600 * 1000
    m = splited[1] * 60 * 1000
    s = splited[2] * 1000
    return h + m + s


def main():
    lines = [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s",
    ]

    print(solution(lines))


if __name__ == "__main__":
    main()