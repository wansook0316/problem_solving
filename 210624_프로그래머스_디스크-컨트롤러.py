from collections import deque
import heapq


def solution(jobs):
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
    q = deque(jobs)
    heap = []
    i, time, total = 0, 0, 0
    while i < len(jobs):

        while q:
            job = q.popleft()
            if job[0] <= time:
                heapq.heappush(heap, (job[1], job[0]))
            else:
                q.appendleft([job[0], job[1]])
                break

        if heap:
            current = heapq.heappop(heap)
            time += current[0]
            total += time - current[1]
            i += 1
        else:
            time += 1
    #     print(time, i, total)
    # print(i, time, total)
    return int(total / len(jobs))
