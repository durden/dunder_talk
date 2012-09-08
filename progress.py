class ProgressBar(object):
    """Progress bar that normalizes progress to [0 - 100] scale"""

    def __init__(self, max_value):
        """Create progress bar with max_value"""

        self._current_value = 0.0
        self._completed_value = 100.0
        self._max_value = float(max_value)

    def __enter__(self):
        """Start of context manager, 'with' statement"""

        self._current_value = 0.0

        # Important!
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Start of context manager, 'with' statement"""

        self.update(self._max_value)

        # Not handling any exceptions, so they'll be raised automatically
        # To ignore exceptions return True or inspect arguments to handle

        return False

    def update(self, value):
        """Update progress value"""

        if value >= self._max_value:
            self._current_value = self._completed_value
        else:
            self._current_value = (value / self._max_value) * self._completed_value

        print '\r%s' % (self._current_value),
