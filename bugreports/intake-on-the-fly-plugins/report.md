1. I am trying to add a module containing my custom "Driver" on-the-fly following the documentation.

I have the following in my current directory
```
└── data
    ├── catalog.yaml
    ├── example.csv
    └── intake_astropy.py
```

```yaml
# ==> data/catalog.yaml <==
metadata:
  version: 1

plugins:
  source:
    - module: intake_astropy
    - dir: "{{ CATALOG_DIR }}"

sources:

  example:
    driver: astropy_table
    args:
      path: "{{ CATALOG_DIR }}/example.csv"
      args:
        format: ascii.csv
```

==> data/example.csv <==
```csv
col1, col2, col3
1, 2, 3
```


==> data/intake_astropy.py <==
```python
'''
Astropy Table driver for Intake
'''
from intake.source.base import DataSource
from astropy.table import Table
import pandas as pd
import intake


__all__ = ['AstropyTableSource']


class AstropyTableSource(DataSource):
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
```

Now I try to read:
```python
In [1]: import intake

In [2]: cat = intake.open_catalog('data/catalog.yaml')

In [3]: cat.example.get()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-3-b8364f147845> in <module>
----> 1 cat.example.get()

~/miniconda3/envs/research/lib/python3.7/site-packages/intake/catalog/local.py in get(self, **user_parameters)
    235         if len(self._plugin) == 0:
    236             raise ValueError('No plugins loaded for this entry: %s'
--> 237                              % self._driver)
    238         elif isinstance(self._plugin, list):
    239             plugin = self._plugin[0]

ValueError: No plugins loaded for this entry: astropy_table
```

I tried with `driver: intake_astropy.AstropyTableSource` or `driver: AstropyTableSource` and got the same error.

What am I doing wrong here?

2. Is there a way to express "parent dir of CATALOG_DIR" using jinja?

```
plugins:
    dir: "{{CATALOG_DIR}}/.."
````
Does this work?

3. Finally, if a user is inside the directory where the driver module is (`intake_astropy.pyz), this import statement
```
from intake.source.base import DataSource
```
gives
```
In [1]: import intake
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-924f1ec0a922> in <module>
----> 1 import intake

~/miniconda3/envs/research/lib/python3.7/site-packages/intake/__init__.py in <module>
     69
     70
---> 71 make_open_functions()
     72 cat = load_combo_catalog()
     73

~/miniconda3/envs/research/lib/python3.7/site-packages/intake/__init__.py in make_open_functions()
     36         isidentifier = IDENTIFIER_REGEX.match
     37     for plugin_name, plugin in registry.items():
---> 38         func_name = 'open_' + plugin_name
     39         if not isidentifier(func_name):
     40             # primitive name normalization

TypeError: can only concatenate str (not "NoneType") to str
```

I'm guessing this is becuase it's recognizing the base class as a plugin driver?

If I remove that import statement and instead subclass like
```python
class AstropyTableSource(intake.source.base.DataSource):
```
everything works out:
```python
In [1]: import intake

In [2]: intake.open_astropy_table
Out[2]: intake_astropy.AstropyTableSource
```
