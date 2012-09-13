# Context Managers

    !python

    __enter__(self)
    __exit__(self, exc_type, exc_value, traceback)

- Useful for 'book ended' actions
- Simple exception handling
- Built-in for File objects, etc. in 2.7

--------------------------------------------------

# Context Manager usage

    !python
    >>> with ProgressBar(5) as p:
    ...   for ii in xrange(5):
    ...     p.update(ii)
    ...
    0.0 20.0 40.0 60.0 80.0 100.0

    >>> with ProgressBar(5) as p:
    ...   for ii in xrange(2):
    ...     p.update(ii)
    ...
    0.0 20.0 100.0

--------------------------------------------------

# Context Manager example

    !python
    class ProgressBar(object):
        """Progress bar that normalizes progress to [0 - 100] scale"""
        def __init__(self, max_val):
            self._curr_val = 0.0
            self._done_val = 100.0
            self._max_val = float(max_val)
        def __enter__(self):
            """Start of context manager, 'with' statement"""
            self._curr_val = 0.0

            # Important!
            return self
        def __exit__(self, exc_type, exc_value, traceback):
            """End of context manager, leaving 'with' statement"""
            self.update(self._max_val)

            # Not handling any exceptions, so they'll be raised automatically
            # To ignore exceptions return True or inspect arguments to handle
            return False

        def update(self, value):
            if value >= self._max_val:
                self._curr_val = self._done_val
            else:
                self._curr_val = (value / self._max_val) * self._done_val

            print '%s' % (self._curr_val),
