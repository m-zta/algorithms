import numpy as np

dictionary = {}


def combinations(num, array):
    if num == 0:
        return 1

    if num in dictionary:
        return dictionary.get(num)

    result = 0

    for x in array:
        if num - x >= 0:
            combs = combinations(num - x, array)
            result += combs

    dictionary[num] = result

    return result


def min_comb(num, array):
    min_indices = []



def main():
    arr = np.array([1, 2, 3])
    nums = np.array([3, 11, 15, 41])

    for num in nums:
        print(combinations(num, arr))


if __name__ == "__main__":
    main()
