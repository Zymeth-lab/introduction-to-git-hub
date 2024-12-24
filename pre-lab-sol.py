# stats.py

def mean(numbers):
    """
    Compute the average of a set of numbers.

    :param numbers: A list of numbers.
    :return: The average of the numbers.
    """
    if len(numbers) == 0:
        raise ValueError("The list is empty")

    return sum(numbers) / len(numbers)

def median(numbers):
    """
    Compute the median of a list of numbers.

    :param numbers: A list of numbers.
    :return: The median of the numbers.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (sorted_numbers[mid1] + sorted_numbers[mid2]) / 2

def mode(numbers):
    """
    Compute the mode(s) of a list of numbers.

    :param numbers: A list of numbers.
    :return: The mode(s) of the numbers. If there is more than one mode, a ValueError is raised.
    """
    from collections import Counter
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_count]

    if len(modes) == 1:
        return modes[0]
    else:
        raise ValueError("The list has multiple modes: " + ", ".join(map(str, modes)))


# main.py
import stats

data = [4, 7, 2, 8, 1, 5]

try:
    print("Mean:", stats.mean(data))
    print("Median:", stats.median(data))
    print("Mode:", stats.mode(data))
except Exception as e:
    print(e)
