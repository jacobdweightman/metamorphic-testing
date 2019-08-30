import unittest

from kth_occurrence import kth_occurrence

class MR1(unittest.TestCase):
    '''
    Represents the metamorphic relation:
    if kth_occurrence(x, k, A) = i, then A[i] = x
    '''
    def __init__(self, A=None, x=None, k=None):
        super().__init__('test_mr')
        self.A = A
        self.x = x
        self.k = k

    def test_mr(self):
        i = kth_occurrence(self.x, self.k, self.A)
        self.assertEqual(self.A[i], self.x)

class MR2(unittest.TestCase):
    '''
    Represents the metamorphic relation:
    kth_occurrence(A[i], 1, A) != -1
    '''
    def __init__(self, A=None, i=None):
        super().__init__('test_mr')
        self.A = A
        self.i = i

    def test_mr(self):
        self.assertNotEqual(kth_occurrence(self.A[self.i], 1, self.A), -1)

def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()

    A = [3, 1, 2, 1, 0, 0, 0, 1, 3, 3, 2, 2]

    suite.addTest(MR1(A=A, x=0, k=2))
    suite.addTest(MR2(A=A, i=3))

    return suite