"""
Author    : Nikhil Arora
Date      : February 36, 2023

Implement the class of prefix sum with useful functions based on it.

"""


class PrefixSum:
    def __init__(self, array: list[int]) -> None:
        len_array = len(array)
        self.prefix_sum = [0] * len_array

        if len_array > 0:
            self.prefix_sum[0] = array[0]

        for i in range(1, len_array):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + array[i]
