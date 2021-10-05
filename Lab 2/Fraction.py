# SYSC 2100 Winter 2021 Lab 2

def gcd(m: int, n: int) -> int:
    """Return the greatest common divisor of m and n.

    Precondition: m > 0, n > 0.

    >>> gcd(4, 1)
    1
    >>> gcd(30, 5)
    5
    >>> gcd(9, 17)
    1
    """
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, top: int, bottom: int) -> None:
        """Initialize self with numerator top and denominator bottom.

        Raise a ValueError exception if bottom is 0.

        When __init__ returns, this fraction will be in reduced form.
        This means that:
        (1) if the numerator is equal to 0, the denominator is always 1.
        (2) if the numerator is not equal to 0, the denominator is always
        positive. This means that negative fractions always have a negative
        numerator and a positive denominator.
        (3) the numerator and denominator have no common divisors
        other than 1.

        >>> Fraction(3, 4)
        Fraction(3, 4)
        >>> Fraction(6, 8)
        Fraction(3, 4)
        >>> Fraction(-3, 4)
        Fraction(-3, 4)
        >>> Fraction(3, -4)
        Fraction(-3, 4)
        >>> Fraction(-3, -4)
        Fraction(3, 4)
        >>> Fraction(0, 5)
        Fraction(0, 1)
        """

        # This method must be modified to match the specification
        # in the docstring.
        
        if (bottom == 0):
            raise ValueError("Denominator cannot be 0") 
        
        divisor = gcd(top, bottom)
        
        if (top == 0):
            self._num = top
            self._den = 1
            
        elif (bottom < 0):
            self._num = (-top)
            self._den = (-bottom)
            
            if (divisor != 1):
                self._num = top // divisor
                self._den = bottom // divisor            
        
        elif (divisor != 1):
            self._num = top // divisor
            self._den = bottom // divisor
            
        else:
            self._num = top
            self._den = bottom            
            
    def __str__(self) -> str:
        """Return a string representation of self in the format:
        top/bottom.

        >>> f = Fraction(3, 4)
        >>> str(f)
        '3/4'
        """
        return "{0}/{1}".format(self._num, self._den)

    def __repr__(self) -> str:
        """Return a string representation of self in the format:
        Fraction(top, bottom).

        >>> f = Fraction(3, 4)
        >>> f
        Fraction(3, 4)
        >>> f = Fraction(3, -4)
        >>> f
        Fraction(-3, 4)
        """
        return "Fraction({0}, {1})".format(self._num, self._den)

    def numerator(self) -> int:
        """Return the numerator of self.

        >>> f = Fraction(3, 4)
        >>> f.numerator()
        3
        """
        return self._num

    def denominator(self) -> int:
        """Return the denominator of self.

        >>> f = Fraction(3, 4)
        >>> f.denominator()
        4
        """
        return self._den

    def __eq__(self, other_fraction) -> bool:
        """Return True if self equals other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(6, 8)
        >>> f1 == f2
        True
        >>> f2 = Fraction(1, 2)
        >>> f1 == f2
        False
        """
        first_num = self._num * other_fraction._den
        second_num = other_fraction._num * self._den

        return first_num == second_num

    def __lt__(self, other_fraction) -> bool:
        """Return True if self is less than other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(6, 8)
        >>> f1 < f2
        False
        >>> f2 = Fraction(7, 8)
        >>> f1 < f2
        True
        """
        first_num = self._num * other_fraction._den
        second_num = other_fraction._num * self._den

        return first_num < second_num

    def __le__(self, other_fraction) -> bool:
        """Return True if self is less than or equal to other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(6, 8)
        >>> f1 <= f2
        True
        >>> f2 = Fraction(7, 8)
        >>> f1 <= f2
        True
        >>> f2 <= f1
        False
        """
        first_num = self._num * other_fraction._den
        second_num = other_fraction._num * self._den

        return first_num <= second_num
    
    def __ne__(self, other_fraction) -> bool:
        """Return True if self is not equal to other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(6, 8)
        >>> f1 != f2
        False
        >>> f2 = Fraction(7, 8)
        >>> f1 != f2
        True
        >>> f2 != f1
        True
        """
        first_num = self._num * other_fraction._den
        second_num = other_fraction._num * self._den

        return first_num != second_num  
    
    def __gt__(self, other_fraction) -> bool:
        """Return True if self is greater than other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(6, 8)
        >>> f1 > f2
        False
        >>> f2 = Fraction(7, 8)
        >>> f1 > f2
        False
        >>> f2 > f1
        True
        """
        first_num = self._num * other_fraction._den
        second_num = other_fraction._num * self._den

        return first_num > second_num
    
    def __ge__(self, other_fraction) -> bool:
        """Return True if self is greater than or equal to other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(6, 8)
        >>> f1 >= f2
        True
        >>> f2 = Fraction(7, 8)
        >>> f1 >= f2
        False
        >>> f2 >= f1
        True
        """
        first_num = self._num * other_fraction._den
        second_num = other_fraction._num * self._den

        return first_num >= second_num    

    def __add__(self, other_fraction):
        """Return the sum of self and other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(1, 8)
        >>> f1 + f2
        Fraction(7, 8)
        >>> f1 = Fraction(1, 4)
        >>> f2 = Fraction(1, 2)
        >>> f1 + f2
        Fraction(3, 4)
        """
        new_num = (self._num * other_fraction._den
                   + self._den * other_fraction._num)
        new_den = self._den * other_fraction._den
        return Fraction(new_num, new_den)

    def __sub__(self, other_fraction):
        """Return the difference of self and other_fraction; that is,
        the Fraction that is obtained by subtracting other_fraction from sub.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(1, 8)
        >>> f1 - f2
        Fraction(5, 8)
        >>> f1 = Fraction(1, 4)
        >>> f2 = Fraction(1, 2)
        >>> f1 - f2
        Fraction(-1, 4)
        """
        new_num = (self._num * other_fraction._den
                   - self._den * other_fraction._num)
        new_den = self._den * other_fraction._den
        return Fraction(new_num, new_den)

    def __mul__(self, other_fraction):
        """Return the product of self and other_fraction; that is,
        self - other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(1, 8)
        >>> f1 * f2
        Fraction(3, 32)
        >>> f2 = Fraction(6, 8)
        >>> f1 * f2
        Fraction(9, 16)
        """
        new_num = self._num * other_fraction._num
        new_den = self._den * other_fraction._den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        """Return the result of dividing self by other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(1, 8)
        >>> f1 / f2
        Fraction(6, 1)
        >>> f2 = Fraction(2, 1)
        >>> f1 * f2
        Fraction(3, 8)
        """
        new_num = self._num * other_fraction._den
        new_den = other_fraction._num * self._den
        return Fraction(new_num, new_den)
    
# if __name__ == "__main__":
#     x = Fraction(1, 2)
#     print('x = {0}'.format(x))
#     y = Fraction(2, 3)
#     print('y = {0}'.format(y))
#     print('x + y = {0}'.format(x + y))
#     print('x == y is {0}'.format(x == y))
