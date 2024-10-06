from homework.debugging_while.debugging_while import countdown


class TestCountdown:

    def test_countdown(self):
        # Test cases for Task 3 (Debugging while loop)
        assert countdown(5) == [5, 4, 3, 2, 1]
        assert countdown(1) == [1]
        assert countdown(0) == []
