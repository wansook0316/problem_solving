from collections import deque


def solution(tickets):
    answers = []
    q = deque()
    used = [False for _ in tickets]
    answer = ["ICN"]
    q.append(["ICN", used, answer])

    while q:
        start, used, answer = q.pop()

        if all(used):
            answers.append(answer)

        for i, (s, e) in enumerate(tickets):
            if s == start and used[i] == False:
                _used = used[:]
                _answer = answer[:]
                _used[i] = True
                _answer.append(e)
                q.append([e, _used, _answer])
    # print(answers.sort())
    answers.sort()
    return answers[0]


# ICN JFK [False, False, False] ['ICN']
# ICN JFK [True, False, False] ['ICN', 'JFK']
# JFK HND [False, False, False] ['ICN']
# JFK HND [False, False, True] ['ICN', 'HND']
# HND IAD [False, False, False] ['ICN']
# HND IAD [False, True, False] ['ICN', 'IAD']

# [["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]
# return : ["ICN", "A", "D", "B", "A", "C"]