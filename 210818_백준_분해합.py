import sys

input = sys.stdin.readline


def get_generate_number(num):
    ret = num
    num = f"{num}"
    for char in num:
        ret += int(char)
    return ret


def main():
    n = int(input())
    result = []
    for i in range(1, n + 1):
        if get_generate_number(i) == n:
            result.append(i)
    print(min(result) if result else 0)


if __name__ == "__main__":
    main()