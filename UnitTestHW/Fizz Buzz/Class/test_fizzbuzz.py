import pytest
from horrible_fizzbuzz import Solution

@pytest.fixture
def solution():
    return Solution()

class TestSolution:
    def test_3(self, solution):
        assert solution.singleFizzBuzz(3) == "Fizz"
    
    def test_5(self, solution):
        assert solution.singleFizzBuzz(5) == "Buzz"
    
    def test_15(self, solution):
        assert solution.singleFizzBuzz(15) == "FizzBuzz"
    
    def test_2(self, solution):
        assert solution.singleFizzBuzz(2) == "2"

    def test_main_14(self, solution):
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14"]
        assert solution.fizzBuzz(14) == expected

    def test_main_15(self, solution):
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
        assert solution.fizzBuzz(15) == expected

    def test_invalid_input(self, solution):
        with pytest.raises(TypeError):
            solution.singleFizzBuzz("a string")