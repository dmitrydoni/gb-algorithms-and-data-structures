import hashlib


# This function compares two strings using SHA-1 hash function.
def is_eq_str(a: str, b: str, verbose=False) -> bool:
    assert len(a) > 0 and len(b) > 0, "Strings must not be empty"

    print("Comparing strings...")

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f'String 1 hash: {ha}\nString 2 hash: {hb}')

    return ha == hb


print("Please input two strings to compare.")

s_1 = input("String 1: ")
s_2 = input("String 2: ")

print("The strings are equal." if is_eq_str(s_1, s_2, True) else "The strings are different.")


# Based on Rabin-Karp algorithm
def find_subs_in_s(s: str, subs: str, verbose=False) -> int:
    assert len(s) > 0 and len(subs) > 0, "Strings must not be empty"
    assert len(s) > len(subs), "A string must be longer than a substring"

    print("Calculating hash...")

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

            if s[i:i + len_sub] == subs:
                return i

    if verbose:
        print(f'Substring hash: {h_subs}')

    return -1


print("Please input strings.")

s_1 = input("String: ")
s_2 = input("Substring: ")

pos = find_subs_in_s(s_1, s_2)

print(f'The substring is found in position {pos}.' if pos != -1 else 'The substring was not found.')
