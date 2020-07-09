"""
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.
"""
from typing import List, Dict


def twoSum(nums: List[int], target: int) -> List[int]:

    residue2idx: Dict[int, int] = dict()
    for i, e in enumerate(nums):
        residue = target - e
        if residue in residue2idx:
            return [i, residue2idx[residue]]
        else:
            # save down the residue
            residue2idx[e] = i


if __name__ == "__main__":
    res = twoSum(nums=[2, 7, 11, 15], target=9)
    print(res)
