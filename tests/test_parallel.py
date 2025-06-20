import unittest

from parallel import parallel


class TestParallel(unittest.TestCase):
    def test_positive_parallel_execution(self):
        with parallel(max_workers=None) as pl:
            pl(lambda: print('Hello'))
            pl(lambda: print('World'))

    def test_negative_parallel_execution(self):
        try:
            with parallel(max_workers=None) as pl:
                pl(print('TypeError'))  # noqa
        except TypeError:
            pass
        else:
            raise AssertionError('TypeError not raised as expected')

    def test_parallel_max_workers(self):
        with parallel(max_workers=5) as pl:
            pl(lambda: print('Hello World'))
