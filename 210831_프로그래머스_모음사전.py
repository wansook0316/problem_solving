from itertools import product, chain


def solution(word):
    dictionary_string_list = list()
    for i in range(1, 6):
        temp = list(map("".join, product(*(["AEIOU"] * i))))
        dictionary_string_list.extend(temp)

    dictionary_string_list.sort()
    return dictionary_string_list.index(word) + 1


def main():
    words = ["AAAAE", "AAAE", "I", "EIO"]
    for word in words:
        print(solution(word))


if __name__ == "__main__":
    main()
