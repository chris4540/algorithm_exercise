import sys
import string

def is_password_okay(pwd):
    if len(pwd) < 6:
        return False

    pwd_char_set = set(iter(pwd))
    # check if has at least one symbol
    symbol_intx = pwd_char_set.intersection(set(iter("@$%")))
    if len(symbol_intx) == 0:
        return False

    # check 5 or more unique lowercase alphabetical characters.
    alphabet_intx = pwd_char_set.intersection(set(iter(string.ascii_lowercase)))
    if len(alphabet_intx) < 5:
        return False

    return True

def get_input_string(file):
    with open(file, 'r') as f:
        ret = f.readline()
    return ret

def write_ans(size_pwd):
    with open("answer.txt", 'w') as f:
        f.write(str(size_pwd))

if __name__ == '__main__':
    s = get_input_string(sys.argv[1])

    pwd_len = 6
    while True:
        for i in range(0, len(s)-pwd_len+1):
            if is_password_okay(s[i:i+pwd_len]):
                print("The minimum size of pwd is ", pwd_len)
                write_ans(pwd_len)
                sys.exit(0)

        # cannot find one, add pwd_len
        pwd_len = pwd_len + 1
        if (pwd_len > len(s)):
            print("Unable to find a pwd")
            sys.exit(1)
