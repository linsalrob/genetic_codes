"""
Some basic statistics functions
"""


def mean(arr):
    """
    Calculate the mean of all the values in a list

    :param arr: The list of values
    :type arr: list
    :return: The mean of all the numbers
    :rtype: float
    """
    n = len(arr)
    sm = sum(arr)
    return float(sm) / float(n)


def median(arr):
    """
    Calculate the median of all the values in a list

    :param arr: The list of values
    :type arr: list
    :return: The median of all the numbers
    :rtype: float
    """
    arr.sort()
    n = len(arr)
    mid = int(n / 2)
    return arr[mid]
