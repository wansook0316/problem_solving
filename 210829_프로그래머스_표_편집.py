class Node:
    def __init__(self, value):
        self.value = value
        self.flag = True
        self.prev = None
        self.next = None
        self.dict = dict()

        self.printPrev = None
        self.printNext = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node("head")
        self.tail = Node("tail")

        self.head.next = self.tail
        self.head.printNext = self.tail
        self.tail.prev = self.head
        self.tail.printPrev = self.head

        self.stack = list()
        self.cursor = None

    def setCursor(self, position):
        cur_node = self.head
        while not (cur_node.next.value == "tail" or cur_node.value == position):
            cur_node = cur_node.next
        self.cursor = cur_node

    def undo(self):
        if not self.stack:
            return

        node = self.stack.pop()
        node.flag = True

        node.prev.next = node
        node.next.prev = node

    def append(self, value):
        temp_node = self.tail.prev

        self.tail.prev = Node(value)
        self.tail.prev.next = self.tail
        # 출력 위한 링크
        self.tail.printPrev = self.tail.prev
        self.tail.prev.printNext = self.tail

        temp_node.next = self.tail.prev
        self.tail.prev.prev = temp_node

        # 출력 위한 링크
        temp_node.printNext = self.tail.prev
        self.tail.prev.PrintPrev = temp_node

    def down(self, num):
        count = 0
        cur_node = self.cursor

        while not (cur_node.next.value == "tail" or count >= num):
            count += 1
            cur_node = cur_node.next

        self.cursor = cur_node

    def up(self, num):
        count = 0
        cur_node = self.cursor

        while not (cur_node.prev.value == "head" or count >= num):
            count += 1
            cur_node = cur_node.prev

        self.cursor = cur_node

    def delete(self):
        self.cursor.flag = False
        self.stack.append(self.cursor)

        self.cursor.prev.next = self.cursor.next
        self.cursor.next.prev = self.cursor.prev

        self.cursor = self.cursor.next

        if self.cursor.value == "tail":
            self.cursor = self.cursor.prev

    def description(self):
        ret = ""
        cur_node = self.head.printNext
        while cur_node.value != "tail":
            ret += "O" if cur_node.flag else "X"
            cur_node = cur_node.printNext
        return ret


def solution(n, k, cmd):
    # 처음에 n개에 맞는 요소를 링크드 리스트에 삽입한다.
    # 커서 위치를 변경한다.
    # command 를 해석해서 하나씩 적용한다.

    table = DoubleLinkedList()

    for i in range(n):
        table.append(i)  # 테이블에 하나씩 넣는다.
    table.setCursor(k)
    # print(table.cursor.value)
    for command in cmd:
        if command.startswith("U"):
            num = int(command.split()[1])
            table.up(num)
            # print(table.cursor.value)
        elif command.startswith("D"):
            num = int(command.split()[1])
            table.down(num)
            # print(table.cursor.value)
        elif command.startswith("C"):
            table.delete()
            # print(table.cursor.value)
        elif command.startswith("Z"):
            table.undo()
            # print(table.cursor.value)

    return table.description()


def main():
    n = 8
    k = 2
    cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
    # cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
    print(solution(n, k, cmd))


if __name__ == "__main__":
    main()
