# OrderedDict

    !python

    __setitem__(self, key, value)
    __getitem__(self, key)
    __len__(self)
    __delitem__(self, key)
    __iter__(self)
    __reversed__(self)
    __contains__(self)
    __concat__(self)

- Sequence protocol, implement what you need
- [Pure Python OrderedDict](http://code.activestate.com/recipes/576693/)

# Presenter Notes

- Immutable only needs getitem, len
- Mutable needs setitem
- Implementing __contains__ usually not needed, default behavior is to loop
  over your items and return if it was found.

--------------------------------------------------

# OrderedDict usage

    !python
    >>> import collections
    >>> ordered_dict = collections.OrderedDict()
    >>>
    >>> ordered_dict['a'] = 1
    >>> ordered_dict['b'] = 2
    >>> ordered_dict['c'] = 3
    >>> for k, v in ordered_dict.iteritems(): print k,v
    ...
    a 1
    b 2
    c 3

    >>> unordered_dict = {}
    >>> unordered_dict['a'] = 1
    >>> unordered_dict['b'] = 2
    >>> unordered_dict['c'] = 3
    >>> for k, v in unordered_dict.iteritems(): print k,v
    ...
    a 1
    c 3
    b 2
