import pandas as pd


class DataProcBase:
    """
    DataSet superclass contains metadata for subclasses.
    This metadata is required to perform essential functionality.
    """
    def __init__(self):
        self.data = None
        self.copy = None
        self._processor = None

    def __copy__(self, data: pd.DataFrame, copy: bool = True):
        """
        Copy magic method provides successive decomposition of the `pandas.DataFrame` passed.

            :param data: `pandas.DataFrame` to be copied
            :param copy: `bool` responsible for creating a copy of the `data` or modifying the original
            :return: essentially `None` whilst overwriting the copy of the `data` passed into `self.data` and
                absorbing metadata about the `data`
        """
        self.copy = copy
        if self.copy:
            self.data = data.copy()
        else:
            self.data = data
        self._cols = self.data.columns
        self._rows = self.data.index
        self._vals = self.data.values.base

