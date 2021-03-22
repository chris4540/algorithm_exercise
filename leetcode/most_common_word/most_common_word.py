from typing import List
from collections import Counter
class Solution:
    symbols = set("!?',;.")

    def clean_symbols(self, text: str):
        ret = ""
        for c in text.lower():
            if c in self.symbols:
                ret += " "
            else:
                ret += c
        return ret
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = Counter()
        # handle the symbols in the paragraph
        cleaned_paragraph = self.clean_symbols(paragraph)

        for word in cleaned_paragraph.split():
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1

        for ban in banned:
            if ban in counter:
                counter.pop(ban)

        ret, _ = counter.most_common(1)[0]
        return ret

if __name__ == '__main__':
    text = "a, a, a, a, b,b,b,c, c"
    ban = ["a"]
    print(Solution().mostCommonWord(text, ban))