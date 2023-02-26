def permute(nums: list[int]) -> list[list[int]]:
    """
    Return all premutations.

    From intertools import permutations
    :param nums: numbers = [1, 2, 3]
    :return: all(list(nums) in permute(numbers) for nums in permutations(numbers))
    True
    """

    result = []
    if len(nums) == 1:
        return [nums.copy()]
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutations = permute(nums)
        for perm in permutations:
            perm.append(n)
        result.extend(permutations)
        nums.append(n)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
