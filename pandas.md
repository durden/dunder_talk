## Pandas

    !python
    >>> import pandas
    >>> # Series is 1-d numpy array with labels
    >>> s = pandas.Series({'a' : 0., 'b' : 1., 'c' : 2.})
    >>> s
    a    0
    b    1
    c    2
    >>> s[0]
    0.0
    >>> s[[2,1]]
    c    2
    b    1
    >>> s[[2,1]][0]
    2.0

    >>> s[s >= 1]
    b    1
    c    2

    >>> s * 3
    a    0
    b    3
    c    6

- Supports tons of fancy indexing
- See pandas/core/series.py

# Presenter Notes

- Show pandas_snippet.py if time

--------------------------------------------------

# Pandas secrets

    !python

    __ge__(self, other_instance)
    __getitem__(self, key)

    >>> class Test(object):
            def __getitem__(self, key):
                print '%-15s  %s' % (type(key), key)

    >>> t = Test()
    >>> t[1]
    <type 'int'>     1

    >>> t['hello world']
    <type 'str'>     hello world

    >>> t[1, 'b', 3.0]
    <type 'tuple'>   (1, 'b', 3.0)

    >>> t[5:200:10]
    <type 'slice'>   slice(5, 200, 10)

    >>> t['a':'z':3]
    <type 'slice'>   slice('a', 'z', 3)

    >>> t[object()]
    <type 'object'>  <object object at 0x10aaf40d0>

- 'key' argument is fancy
