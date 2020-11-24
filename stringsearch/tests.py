# stringsearching.py
# Author: Lee Taylor
from stringsearching import *


"""
AGTCATATG -> CATA -> 7

TGTAATAAG -> TAAC -> 13
"""
def test():
    """ Tests function bruteforce(...) """
    rv, ans = bruteforce("AGTCATATG", "CATA")
    print(ans)

    rv2, ans2 = bruteforce("TGTAATAAG", "TAAC")
    print(ans2)

    rv3, ans3 = bruteforce("AGTAAGTACTAC", "AGTAC")
    print(ans3)

# noinspection SpellCheckingInspection
def test_table():
    # Strings
    print("ABC: " + str(find_next("ABC")))
    print("ABAB: " + str(find_next("ABAB")))
    print("ABCABB: " + str(find_next("ABCABB")))
    # Table for str "ABABC"
    print()
    print("A: " + str(find_next("A")))
    print("AB: " + str(find_next("AB")))
    print("ABA: " + str(find_next("ABA")))
    print("ABAB: " + str(find_next("ABAC")))
    print("ABABC: " + str(find_next("ABACB")))

# noinspection SpellCheckingInspection
def test_kmp():
    table("ABCABB", True)
    table("ABACB", True)
    table("CABABB", True)
    table("ABAA", True)
    table("ACACB", True)
    table("11000", True)
    table("00001", True)
    print()  # newline
    # kmp_search("AACBACACACBCA", "ACACB", debug=True)
    # kmp_search("00000000", "00001", debug=True)
    # kmp_search("ABABCDABCABCABBACC", "ABCABB", debug=True)
    # kmp_search("DDCDADDDDAC", "DDDA", debug=True)

    kmp_search_traced("DDCDADDDDAC", "DDDA")
    kmp_search_traced("ABABCDABCABCABBACC", "ABCABB", True)
    kmp_search_traced("ACBCCAACBA", "ACBA")
    kmp_search_traced("ACACABACAB", "ACACB")
    kmp_search_traced("AACBACACACBCA", "ACACB")
    kmp_search_traced("1110101100010", "11000", True)
    kmp_search_traced("00000000", "00001", True)
    kmp_search_traced("BBBBA", "AB")

if __name__ == '__main__':
    test()
    print()  # newline
    test_table()
    print()  # newline
    test_kmp()