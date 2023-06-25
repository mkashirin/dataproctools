from itertools import chain

import pandas as pd

from ._core import DataProcBase


class RenamingTool(DataProcBase):
    """
    Renamer class works with `pandas.DataFrame` only.
    Rename columns by default, indices if you provide in a specified order.
    """

    def __init__(self):
        super().__init__()
        self.mark = None

    def preprocess(self, data: pd.DataFrame, mark: str = None,
                   cols: str = None, rows: str = None, copy: bool = False):
        """
        Preprocess the dataset.

            :param data: `pandas.DataFrame` to be preprocessed
            :param mark: pass an `str` name of the marker variable
            :param cols: pass an `str` name of columns
            :param rows: pass an `str` name of indices
            :param copy: pass `True` if you want to create a copy of the `data`
            :return: `pandas.DataFrame` with columns renamed and indices if provided
        """
        super().__copy__(data, copy)
        if mark:
            self.mark = list(self._cols).index(mark)
        self._cols = len(self._cols)
        self._rows = len(self._rows)

        if cols:
            self._processor = list(chain.from_iterable(
                [[cols + str(i + 1)] if i != self.mark else
                 ['y', cols + str(i + 1)] for i in range(self._cols)]))
            try:
                self.data.columns = self._processor
            except ValueError:
                self.data.columns = self._processor[:-1]

        if rows:
            self._processor = list(chain.from_iterable(
                [[rows + str(i + 1)] for i in range(self._rows)]))
            self.data.index = self._processor
        return self.data

