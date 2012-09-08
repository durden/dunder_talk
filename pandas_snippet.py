# from pandas/core/series.py:100:
# Ignore fancy wrapping function, etc. boils down to this:
# Comparision between object s and integer, turns into lib.scalar_compare()

#1. __ge__(self, other_instance)
def _comp_method(op, name):
    """
    Wrapper function for Series arithmetic operations, to avoid
    code duplication.
    """
    def na_op(x, y):
        if x.dtype == np.object_:
            if isinstance(y, list):
                y = lib.list_to_object_array(y)

            if isinstance(y, np.ndarray):
                result = lib.vec_compare(x, y, op)
            else:
                result = lib.scalar_compare(x, y, op)
        else:
            result = op(x, y)

        return result

    def wrapper(self, other):
        from pandas.core.frame import DataFrame

        if isinstance(other, Series):
            name = _maybe_match_name(self, other)
            return Series(na_op(self.values, other.values),
                        index=self.index, name=name)
        elif isinstance(other, DataFrame): # pragma: no cover
            return NotImplemented
        elif isinstance(other, np.ndarray):
            return Series(na_op(self.values, np.asarray(other)),
                        index=self.index, name=self.name)
        else:
            values = self.values
            other = lib.convert_scalar(values, other)

            if issubclass(values.dtype.type, np.datetime64):
                values = values.view('i8')

            # scalars
            res = na_op(values, other)
            if np.isscalar(res):
                raise TypeError('Could not compare %s type with Series'
                                % type(other))
            return Series(na_op(values, other),
                        index=self.index, name=self.name)
    return wrapper

# from pandas/core/series.py:430
# 2. __getitem__(self, key)

# key is subtype of np.ndarray (numpy)
# key is a 'boolean indexer' type
# Create new series with given boolean indexer

def __getitem__(self, key):
    try:
        return self.index.get_value(self, key)
    except InvalidIndexError:
        pass
    except KeyError:
        if isinstance(key, tuple) and isinstance(self.index, MultiIndex):
            # kludge
            pass
        else:
            raise
    except Exception:
        raise

    if com.is_iterator(key):
        key = list(key)

    # boolean
    # special handling of boolean data with NAs stored in object
    # arrays. Since we can't represent NA with dtype=bool
    if _is_bool_indexer(key):
        key = self._check_bool_indexer(key)
        key = np.asarray(key, dtype=bool)

    return self._get_with(key)
