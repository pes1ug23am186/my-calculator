"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract, multiply, multiplication, division

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(8,-1) == 7
        assert add(-9,6) == -3
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(9,-1) == 10
        assert subtract(-9,6) == -15
    
class TestMultiplyDiv:
    def test_multiply_positive_numbers(self):
        """Test multiplying negative numbers"""
        assert multiplication(6,2) == 12
        assert multiplication(8,4) == 32

    def test_multiply_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert multiplication(-5,2) == -10
        assert multiplication(-4,-5) == 20

    def test_division_positive_numbers(self):
        """Test multiplying negative numbers"""
        assert division(4,2) == 2
        assert division(12,3) == 4
    
    def test_division_negative_numbers(self):
        """Test Dividing negative numbers"""
        assert division(-4,-2) == 2
        assert division(-8,2) == -4
    

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# TODO: Students will add TestMultiplyDivide class