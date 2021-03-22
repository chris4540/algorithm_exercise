"""
https://leetcode.com/problems/reorder-data-in-log-files
"""
from typing import List


# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         digit_logs = []
#         msg_to_log = {}
#         for log in logs:
#             if log.startswith("dig"):
#                 digit_logs.append(log)
#                 continue
#             # ------------------------------
#             # split the log into [identifier, message]
#             msg = log.split(" ", 1)[1]
#             msg_to_log[msg] = log

#         sorted_letter_logs = [
#             msg_to_log[m]
#             for m in sorted(msg_to_log.keys())
#         ]
#         ret = [
#             *sorted_letter_logs,
#             *digit_logs
#         ]

#         return ret



if __name__ == '__main__':
    fun = Solution().reorderLogFiles

    inputs = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero"
    ]
    res = fun(inputs)
    print(res)