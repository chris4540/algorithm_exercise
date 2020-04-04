"""
Outline:
1. insert parantheses according to digits depth (relaxation)
2. merging anti-paranthese pairs {i.e. ")(" } recusively (constraints)

"""
import re


def insert_parantheses(digit_string):
    ret = ""
    for c in digit_string:
        depth = int(c)

        # add left parantheses
        ret += ''.join(['(']*depth)
        # add the digit
        ret += c
        # add right parantheses
        ret += ''.join([')']*depth)

    return ret

def annihilate_anti_paran(string):
    ret, n_replaced = re.subn(r"\)\(", '', string)

    # do recursion
    if n_replaced > 0:
        ret = annihilate_anti_paran(ret)

    return ret

def add_min_pair_parantheses(digit_string):
    added_para_string = insert_parantheses(digit_string)
    ret = annihilate_anti_paran(added_para_string)
    return ret



def testing():
    strings = [
    '0000',
    '221',
    '312',
    '4',
    ]

    # print(insert_parantheses(s1))
    for s in strings:
        print(s)
        print(add_min_pair_parantheses(s))
        print('-------------')

if __name__ == "__main__":
    num_test = int(input())
    for case in range(1, num_test+1):
        digit_string = input()
        added_paran_string = add_min_pair_parantheses(digit_string)
        print("Case #{}: {}".format(case, added_paran_string))

