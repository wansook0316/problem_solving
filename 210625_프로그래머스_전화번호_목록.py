def solution(phone_book):
    hash_map = {num: 1 for num in phone_book}

    for phone_num in phone_book:
        word = ""
        for num in phone_num:
            word += num
            if word in hash_map and word != phone_num:
                return False
    return True