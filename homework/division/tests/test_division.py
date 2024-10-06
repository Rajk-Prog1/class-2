from homework.division.division import division


class TestDivision:
    def test_basic_operations(self):
        assert division(3, 5) == (0, 0.6)
        assert division(4, 3) == (1, 4 / 3)
        assert division(10, 2) == (5, 5.0)

    def test_division_by_1(self):
        assert division(10, 1) == (10, 10.0)

    def test_large_numbers(self):
        assert division(10**10, 2) == (10**10 // 2, 10**10 / 2)

    def test_small_divisors(self):
        assert division(1, 1000000) == (0, 1 / 1000000)

    def test_float_precision(self):
        result = division(7, 3)
        assert result == (2, 7 / 3)
        assert abs(result[1] - 2.33333333333) < 1e-10
