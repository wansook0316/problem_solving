from collections import deque


def diff(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count


def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    q = deque()
    q.append([begin, 0, []])

    while q:
        word, count, path = q.pop()

        if word == target:
            answer = count
            break

        for w in words:
            if diff(w, word) == 1 and w not in path:
                q.append([w, count + 1, path + [w]])

    return answer