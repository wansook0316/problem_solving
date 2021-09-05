from pprint import pprint


def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for (winner, loser) in results:
        graph[winner][loser] = 1

    pprint(graph)

    # k를 중간 노드로 생각....
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    print("------")
                    print(i, k)
                    print(k, j)
                    print(i, j)
                    graph[i][j] = 1

    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if graph[i][j] or graph[j][i]:
                count += 1
        if count == n - 1:
            answer += 1
    return answer


def main():
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))


if __name__ == "__main__":
    main()