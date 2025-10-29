import pytest
from src.rwmath.math import add, sub, mul, div

class TestMath:
    def testAdd(self):
        assert add(3, 4) == 7
    
    def testSub(self):
        assert sub(4, 3) == 1

    def testMul(sefl):
        assert mul(3, 2) == 6

    def testDiv(self):
        assert div(8, 4) == 2

