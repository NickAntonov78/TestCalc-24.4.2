import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_multiply(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_adding_division(self):
        assert self.calc.division(self, 98754, 2) == 49377

    def test_adding_subtraction(self):
        assert self.calc.subtraction(self, 5875464, 668744) == 5206720

    def test_adding_adding(self):
        assert self.calc.adding(self, 104587, 668744) == 773331