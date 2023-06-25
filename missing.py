import pandas as pd

from ._core import DataProcBase
from . import statistics as stats


class HandlingTool(DataProcBase):
    """
    HandlingTool class works with `pandas.DataFrame` only.
    Handle any missing values (such as `NaN`), replacing it with the statistic passed.
    """
    def __init__(self):
        super().__init__()
        self.stat = None

    def pre(self, data: pd.DataFrame, stat: str = 'mean', copy: bool = True):
        """
        Absorb metadata about the dataset passed and choose statistic to replace missing values.

            :param data: `pandas.DataFrame` to be prepared
            :param stat: pass `'mean'`, `'median'` or `'mode'`
                to replace missing values with the corresponding statistic.
                Missing values would be ignored during the calculation
            :param copy: pass `False` if you do not want to create a copy of the `data`
            :return: `self`
        """
        super().__copy__(data, copy)
        self.stat = stat
        return self

    def process(self, data: pd.DataFrame):
        """
        Process the dataset.

            :return: `pandas.DataFrame` with missing data handling parameters applied
        """
        for col in self._cols:
            data[col] = data[col].fillna(eval(f'stats.{self.stat}(self.data[col])'))
        return data

