from itertools import chain
from functools import reduce


def time2sec(time):
    h, m, s = map(int, time.split(":"))
    return 3600 * h + 60 * m + s


def sec2time(sec):
    h = str(sec // 3600) if len(str(sec // 3600)) % 2 == 0 else "0" + str(sec // 3600)
    m = (
        str((sec % 3600) // 60)
        if len(str((sec % 3600) // 60)) % 2 == 0
        else "0" + str((sec % 3600) // 60)
    )
    s = (
        str((sec % 3600) % 60)
        if len(str((sec % 3600) % 60)) % 2 == 0
        else "0" + str((sec % 3600) % 60)
    )
    return f"{h}:{m}:{s}"


def solution(play_time, adv_time, logs):
    start_time_sec = 0
    play_time_sec = time2sec(play_time)
    adv_time_sec = time2sec(adv_time)
    logs = [list(map(time2sec, l.split("-"))) for l in logs]
    participants = [0 for _ in range(play_time_sec + 1)]

    for s, e in logs:
        participants[s] += 1
        participants[e] += -1

    for i in range(1, len(participants)):
        participants[i] += participants[i - 1]

    i, j = 0, adv_time_sec
    time = reduce(lambda x, y: x + y, participants[:adv_time_sec])
    max_time, start_time = 0, 0
    for start in range(play_time_sec - adv_time_sec):
        if time > max_time:
            max_time = time
            start_time = i
        time -= participants[i]
        time += participants[j]
        i += 1
        j += 1
    if time > max_time:
        max_time = time
        start_time = i
    return sec2time(start_time)