from homework.debugging_if.debugging_if import check_sign


class TestCheckSign:

    def test_check_sign(self):
        assert check_sign(0) == "Zero"
        assert check_sign(5) == "Positive"
        assert check_sign(-3) == "Negative"
