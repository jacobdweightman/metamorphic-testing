import random
import unittest

from binary_search import binary_search

class MR1(unittest.TestCase):
    '''
    Represents the metamorphic relation:
    if x = A[k], then binary_search(x, A) = k

    This MR will catch some simple implementation errors.
    '''
    def __init__(self, name, A=None, k=None):
        super().__init__(name)
        self.A = A
        self.k = k

    def test_mr(self):
        x = self.A[self.k]
        self.assertEqual(binary_search(x, self.A), self.k)


class MR2(unittest.TestCase):
    '''
    Represents the metamorphic relation:
    if A[k-1] < x < A[k+1] and x != A[k], then binary_search(x, A) = -1

    This MR will catch an error where the value being searched for is
    accidentally being inserted into the array.
    '''
    def __init__(self, name, A=None, k=None):
        super().__init__(name)
        self.A = A
        self.k = k

    def test_mr(self):
        if self.k <= 0 or self.k + 1 >= len(self.A):
            self.skipTest("This MR does not apply at the ends of an array")

        x = self.A[self.k - 1] + 1

        if x == self.A[self.k]:
            x += 1

        if x >= self.A[self.k+1]:
            self.skipTest("There is no x such that A[k-1] < x != A[k] < A[k+1]")

        assert self.A[self.k - 1] < x < self.A[self.k + 1]
        assert x != self.k

        self.assertEqual(binary_search(x, self.A), -1)


class MR3(unittest.TestCase):
    '''
    Represents the metamorphic relation:
    if x = A[k], then binary_search(A[k-1], A) = k-1 and
    binary_search(A[k+1], A) = k+1

    This MR will catch errors with the splitting of the array.
    '''
    def __init__(self, name, A=None, k=None):
        super().__init__(name)
        self.A = A
        self.k = k

    def test_mr(self):
        x = self.A[self.k]
        self.assertEqual(binary_search(x, self.A), self.k)


def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()

    A = [4, 6, 10, 15, 18, 25, 40]
    k = 5

    suite.addTest(MR1('test_mr', A=A, k=k))
    suite.addTest(MR2('test_mr', A=A, k=k))
    suite.addTest(MR3('test_mr', A=A, k=k))

    return suite
