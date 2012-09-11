# Context Managers

    !python

    __enter__(self)
    __exit__(self, exc_type, exc_value, traceback)

- Useful for 'book ended' actions
- Simple exception handling
- Built-in for File objects, etc. in 2.7

--------------------------------------------------
# Context Manager example

    !python
    class ProgressBar(object):
        """Progress bar that normalizes progress to [0 - 100] scale"""
        def __init__(self, max_val):
            """Create progress bar with max_val"""
            self._curr_val = 0.0
            self._done_val = 100.0
            self._max_val = float(max_val)
        def __enter__(self):
            """Start of context manager, 'with' statement"""
            self._curr_val = 0.0
            # Important!
            return self
        def __exit__(self, exc_type, exc_value, traceback):
            """Start of context manager, 'with' statement"""
            self.update(self._max_val)

            # Not handling any exceptions, so they'll be raised automatically
            # To ignore exceptions return True or inspect arguments to handle
            return False
        def update(self, value):
            """Update progress value"""
            if value >= self._max_val:
                self._curr_val = self._done_val
            else:
                self._curr_val = (value / self._max_val) * self._done_val
            print '\r%s' % (self._curr_val),
