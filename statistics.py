from .essential import flush

from numpy import ndarray


def mean(arr: ndarray):
    """
    Calculates empirical mean of an array.

        :param arr: `list`  sequence to be parsed
        :return: `float` value of empirical mean of the array passed
    """
    arr_flushed = flush(arr)
    arr_mean = sum(arr_flushed) / len(arr_flushed)
    return arr_mean


def median(arr: ndarray):
    """
    Calculates empirical median of an array.

        :param arr: `list` sequence to be parsed
        :return: `float` value of empirical median of the array passed
    """
    arr_flushed = flush(arr)

    arr_median_index = len(arr_flushed) // 2
    arr_median = sorted(arr_flushed)[arr_median_index]
    return arr_median


def mode(arr: ndarray):
    """
    Calculate empirical mode of an array.

        :param arr: `list` sequence to be parsed
        :return: float` value of empirical mode of the array passed
    """
    arr_flushed = flush(arr)
    arr_mode = max(arr_flushed, key=arr_flushed.count)
    return arr_mode

