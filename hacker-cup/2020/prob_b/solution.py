from collections import Counter


def fuse_stones(stones: str) -> str:
    cnt = {"A": 0, "B": 0}

    for s in stones:
        cnt[s] += 1

    if cnt["A"] == 0 or cnt["B"] == 0:
        return "explosion"
    elif cnt["A"] > cnt["B"]:
        return "A"
    elif cnt["A"] < cnt["B"]:
        return "B"

    raise ValueError("")


def stone_alchemy(stones: str):
    n_stones = len(stones)

    if n_stones == 1:
        return "Y"
    elif len(set(stones)) == 1:
        return "N"

    i = 0
    result_stones = []
    while (i < n_stones - 2):
        result = fuse_stones(stones[i:i+3])
        if result == "explosion":
            result_stones.append(stones[i])
            i += 1
        else:
            result_stones.append(result)
            i += 3

    # add back remainings
    while (i < n_stones):
        result_stones.append(stones[i])
        i += 1

    return stone_alchemy("".join(result_stones))


if __name__ == "__main__":
    n_cases = int(input())
    for i in range(n_cases):
        n_stones = input()
        stones = input()

        print(f"Case #{i+1}: ", stone_alchemy(stones))
        # print(n_stones, stones)
