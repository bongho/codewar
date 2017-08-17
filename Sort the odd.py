# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example

# sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


odd_numbers = [n for n in [5, 3, 2, 8, 1, 4] if n % 2 != 0]
    print(odd_numbers)
    odd_numbers = sorted(odd_numbers)
    print(odd_numbers)

    data = [5, 3, 2, 8, 1, 4]
    print(data)
    odds = iter(sorted(el for el in data if el % 2))
    print([next(odds) if el % 2 else el for el in data])

    import numpy as np
    a = np.array([5, 3, 2, 8, 1, 4])
    ind = np.where(a % 2)  # get indices of odd items
    a[ind] = np.sort(a[ind])  # update items at indices using sorted array
    print(a)
