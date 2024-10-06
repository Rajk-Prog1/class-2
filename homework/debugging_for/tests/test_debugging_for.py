from homework.debugging_for.debugging_for import generate_numbers


class TestGenerateNumbers:

    def test_generate_numbers(self):
        assert generate_numbers(5) == [1, 2, 3, 4, 5]
        assert generate_numbers(1) == [1]
        assert generate_numbers(0) == []
