def solution(phone_book):
    from collections import deque


def diff(word1, word2):
    ret = 0
    for a, b in zip(word1, word2):
        if a != b:
            ret += 1
    return ret


def DFS(begin, visited, words, target, count):
    # print(begin, visited, words, target, count)
    global answer
    if begin == target:
        answer = min(answer, count)

    for w in words:
        if visited[w] == False and diff(begin, w) == 1:
            visited[w] = True
            DFS(w, visited, words, target, count + 1)
            visited[w] = False


def solution(begin, target, words):
    global answer
    answer = 1e6
    if target not in words:
        return 0

    visited = {w: False for w in words}
    visited[begin] = True
    DFS(begin, visited, words, target, 0)
    return answer