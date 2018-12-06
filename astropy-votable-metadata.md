When reading a VOTable with `astropy.table.Table.read` or (probably equivalently) doing `VOTable.to_table`,
meta data such as `INFO` is not transferred at all.

This is not because they are not parsed and one way to get them is to use `astropy.io.votable.parse` directly. An example to extract QUERY INFO usually returned in votables from TAP service:

```python
def find_query(vot_filename):
    """Find QUERY INFO from VOTable
    """
    from astropy.io import votable
    vot = votable.parse(vot_filename)
    t = vot.resources[0]
    query = list(filter(lambda info: info.name == 'QUERY', t.iter_info()))
    assert len(query) == 1
    return query[0].content
```

`parse` parses the entire file so it does not seem possible to read in just the metadata.

