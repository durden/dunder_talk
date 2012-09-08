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

- Immutuable only needs getitem, len
- Mutuable needs setitem
- Implementing __contains__ usually not needed, default behavior is to loop
  over your items and return if it was found.
