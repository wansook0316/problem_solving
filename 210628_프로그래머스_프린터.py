from collections import deque


def solution(priorities, location):
    p = [[index, value] for index, value in enumerate(priorities)]
    count = 0
    while p:
        loc, doc = p.pop(0)
        flag = False
        for i in range(len(p)):
            if p[i][1] > doc:
                p.append([loc, doc])
                flag = True
                break
        if flag:
            continue
        else:
            count += 1
            if loc == location:
                return count
