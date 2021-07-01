class Node:
    def __init__(self, data):
        self.data = data[0]
        self.x = data[1][0]
        self.y = data[1][1]
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class SearchTree:
    def __init__(self):
        self.root = None

    def insertElement(self, data):  # 핵심은 다음노드, 이전 노드를 잡고 가는 것
        new_node = Node(data)  # 새로운 노드 만들기
        if self.root is None:
            self.root = new_node

        current_node = self.root  # root 위치부터 시작
        while True:
            pre_node = current_node  # 일단 지금 작업중인 노드위치 저장
            if current_node.x > new_node.x:
                current_node = current_node.left
                if current_node is None:
                    current_node = new_node  # 현재 작업 노드 위치 변경 -> 종료조건을 만들기 위함
                    pre_node.left = new_node
            elif current_node.x < new_node.x:
                current_node = current_node.right

                if current_node is None:
                    current_node = new_node
                    pre_node.right = new_node
            else:
                return  # 같은 키가 있다는 것임 -> 항상 같은 키가 존재할 수 밖에 없음

    def preorderTravelsal(self, node, bucket):
        # print(node, end=" ")
        bucket.append(node.data)
        if node.left is not None:
            self.preorderTravelsal(node.left, bucket)
        if node.right is not None:
            self.preorderTravelsal(node.right, bucket)

    def postorderTravelsal(self, node, bucket):
        if node.left is not None:
            self.postorderTravelsal(node.left, bucket)
        if node.right is not None:
            self.postorderTravelsal(node.right, bucket)
        # print(node, end=" ")
        bucket.append(node.data)


def solution(nodeinfo):

    nodeinfo_with_data = [[i + 1, node] for i, node in enumerate(nodeinfo)]
    print(nodeinfo_with_data)

    nodeinfo_with_data.sort(key=lambda x: (-x[1][1], x[1][0]))
    print(nodeinfo_with_data)
    tree = SearchTree()

    for node in nodeinfo_with_data:
        tree.insertElement(node)
    answer = []
    temp = []
    tree.preorderTravelsal(tree.root, temp)
    answer.append(temp)

    temp = []
    tree.postorderTravelsal(tree.root, temp)
    answer.append(temp)

    print(answer)
    return answer


if __name__ == "__main__":
    nodeinfo = [
        [5, 3],
        [11, 5],
        [13, 3],
        [3, 5],
        [6, 1],
        [1, 3],
        [8, 6],
        [7, 2],
        [2, 2],
    ]
    solution(nodeinfo)