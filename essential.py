from pandas import DataFrame
from numpy import ndarray


def not_na(val):
    """
    Indicate whether the value passed is missing or not.

        :param val: value to be checked
        :return: `False` if value is missing, `True` otherwise
    """
    return not (val != val)


def flush(arr: ndarray):
    """
    Drop `NaN` values from a two-dimensional array.

        :param arr: two-dimensional array to be flushed
        :return: two-dimensional list with `NaN` values dropped
    """
    flushed = [x for x in list(arr) if not_na(x)]
    return flushed


def dict_drop(df: DataFrame):
    """
    Convert any `pandas.DataFrame` to dictionary (dropping lower indices).

        :param df: `pandas.DataFrame` to be converted
        :return: `dict` with lower indices dropped
    """
    converted = {key: val for key, val in zip(df.columns, map(tuple, df.values.base))}
    return converted

