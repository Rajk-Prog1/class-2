from homework.arithmetic_operators.arithmetic_operators import arithmetic_operators


class TestArithmeticOperators:

    def test_basic_operations(self):
        assert arithmetic_operators(3, 5) == (8, -2, 15)
        assert arithmetic_operators(10, 2) == (12, 8, 20)

    def test_large_numbers(self):
        assert arithmetic_operators(10**10, 10**10) == (2 * 10**10, 0, 10**20)

    def test_same_values(self):
        assert arithmetic_operators(7, 7) == (14, 0, 49)

    def test_smallest_values(self):
        assert arithmetic_operators(1, 1) == (2, 0, 1)
        assert arithmetic_operators(1, 10**10) == (1 + 10**10, 1 - 10**10, 1 * 10**10)
