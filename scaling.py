from typing import Union

from numpy import ndarray
from pandas import DataFrame

from ._core import DataProcBase
from .essential import not_na


def _scale(val: Union[int, float], arr: ndarray):
    """
    Scales a value with respect to an array.

        :param val: `int` or `float` value to be scaled
        :param arr: `ndarray` with respect to which scaling is done
        :return: `float` value scaled with respect to arr
    """
    scaled = (val - min(arr)) / (max(arr) - min(arr))
    return scaled


class ScalingTool(DataProcBase):
    def __init__(self):
        super().__init__()

    def pre(self, data: DataFrame, copy: bool = True):
        """
        Absorb metadata about the dataset passed.

            :param data: `pandas.DataFrame` to be prepared
            :param copy: pass `False` if you do not want to create a copy of the `data`
            :return: `self`
        """
        super().__copy__(data, copy)
        return self

    def process(self, data: DataFrame):
        """
        Process the dataset passed.

            :return: `pandas.DataFrame` with values scaled due to MinMax scaling order
        """
        for col in self._cols:
            for row in data.index:
                if not_na(data.loc[row, col]):
                    data.loc[row, col] = _scale(data.loc[row, col], self.data[col])
        return data

