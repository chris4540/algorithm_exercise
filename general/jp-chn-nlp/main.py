"""
https://stackoverflow.com/questions/30069846/how-to-find-out-chinese-or-japanese-character-in-a-string-in-python
"""
import regex as re
import pandas as pd


def is_full_hiragana(x):
    pattern = re.compile(r'^\p{IsHira}+$', re.UNICODE)
    ret = bool(pattern.fullmatch(x))
    return ret


def is_japanese(x):
    """
    if contains any hiragana / katakana, then japanese, else chinese
    """
    pattern = re.compile(r'[\p{IsHira}\p{IsKatakana}]', re.UNICODE)
    ret = bool(pattern.search(x))
    return ret


if __name__ == '__main__':
    with open("jp_basic_grammar.txt", encoding="utf-8", mode='r', newline='\n') as f:
        lines = f.readlines()

    rows = []
    row = None

    for l in lines:
        l = l.rstrip("\n")

        if is_full_hiragana(l):
            if row:
                rows.append(row)
            row = []

        if l:
            row.append(l)

    # build row_dict
    row_dicts = []
    for row in rows:
        row_dict = dict()
        row_dict['助詞'] = row[0]
        explain = ""
        for i in range(1, len(row)):
            e = row[i]
            if not is_japanese(e):
                explain += e
                explain += ";"
            else:
                break
        row_dict['解釋'] = explain[:-1]
        # -------------------------------
        row_dict['例句'] = ";".join(row[i:])
        row_dicts.append(row_dict)


    df = pd.DataFrame(row_dicts)
    df.to_csv("table.csv", index=None)
