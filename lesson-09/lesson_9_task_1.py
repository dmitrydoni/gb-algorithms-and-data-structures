"""
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача
считается не решённой.
"""

import hashlib


def count_subs_in_s(s: str, verbose=False) -> int:
    assert len(s) > 0, "String must not be empty"

    print("Counting substrings...")

    s_len = len(s)
    subs_hash_set = set()

    for i in range(s_len + 1):

        for j in range(i + 1, s_len + 1):
            subs_hash = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()

            subs_hash_set.add(subs_hash)

    if verbose:
        print(f'Hash set: {subs_hash_set}')

    return len(subs_hash_set)


my_string = input("String: ")

subs_cnt = count_subs_in_s(my_string, False)

print(f'The string contains {subs_cnt} substrings.')
