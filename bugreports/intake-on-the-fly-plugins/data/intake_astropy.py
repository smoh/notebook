'''
Astropy Table driver for Intake
'''
from astropy.table import Table
import pandas as pd
import intake


__all__ = ['AstropyTableSource']


class AstropyTableSource(intake.source.base.DataSource):
    container = 'dataframe'
    name = 'astropy_table'
    version = '0.0.1'
    partition_access = False

    def __init__(self, path, metadata=None, **kwargs):
        super(AstropyTableSource, self).__init__(metadata=metadata)
        self.path = path
        self.kwargs = kwargs

    def _get_schema(self):
        t = Table.read(self.path, **self.kwargs)
        return intake.source.base.Schema(
            datashape=None
        )

    def read(self):
        t = Table.read(self.path, **self.kwargs)
        return t.to_pandas()

    def _close(self):
        pass