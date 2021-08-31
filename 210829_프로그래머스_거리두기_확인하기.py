sitted = "P"
empty = "O"
partition = "X"
possible = 1
impossible = 0


class Person:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def distance(self, person):
        return abs(self.y - person.y) + abs(self.x - person.x)

    def __str__(self):
        return f"{self.y} {self.x}"


def isBlocked(place: list, p1: Person, p2: Person) -> bool:
    print(place)
    dy, dx = abs(p1.y - p2.y), abs(p1.x - p2.x)
    flag = False
    if dy == 1 and dx == 1:
        # 4개 조사해서 X가 2개 있어야 함
        sy, sx = min(p1.y, p2.y), min(p1.x, p2.x)
        ey, ex = max(p1.y, p2.y), max(p1.x, p2.x)
        numOfPartitions = 0
        for i in range(sy, ey + 1):
            for j in range(sx, ex + 1):
                if place[i][j] == partition:
                    numOfPartitions += 1
        if numOfPartitions == 2:
            flag = True
    elif dy == 2 and dx == 0:
        # 작은 것 index로 부터 다음 것에 X 있어야 함
        y, x = min(p1.y, p2.y), p1.x
        if place[y + 1][x] == partition:
            flag = True
    elif dy == 0 and dx == 2:
        y, x = p1.y, min(p1.x, p2.x)
        if place[y][x + 1] == partition:
            flag = True
    return flag


def isPossible(place):
    people = list()
    # p의 위치를 모두 가져와서 객체로 만들고 리스트에 저장
    for i in range(len(place)):
        for j in range(len(place[0])):
            if place[i][j] == sitted:
                people.append(Person(i, j))

    for p1 in people:
        for p2 in people:
            if p1 == p2:
                continue
            dist = p1.distance(p2)
            if dist <= 1:
                return impossible
            elif dist == 2:
                if isBlocked(place, p1, p2) is False:
                    return impossible

    return possible


# 각각의 참가자가 앉아 있는 곳을 기반으로 맨해튼 거리가 2인 지점을 모두 조사
# 총 12번


def solution(places):
    ret = []
    for place in places:
        ret.append(isPossible(place))
    return ret


def main():
    places = [
        # ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        # ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        # ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        # ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        # ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"],
    ]
    print(solution(places))


if __name__ == "__main__":
    main()
