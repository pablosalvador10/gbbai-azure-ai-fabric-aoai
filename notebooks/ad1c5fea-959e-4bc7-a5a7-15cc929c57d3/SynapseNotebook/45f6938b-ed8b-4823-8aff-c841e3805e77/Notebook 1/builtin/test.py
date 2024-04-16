class MathOperations:
    def add(self, a: int, b: int) -> int:
        """
        Add two numbers.

        :param a: The first number.
        :param b: The second number.
        :return: The sum of the two numbers.
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        Subtract one number from another.

        :param a: The first number.
        :param b: The second number.
        :return: The result of subtracting the second number from the first.
        """
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """
        Multiply two numbers.

        :param a: The first number.
        :param b: The second number.
        :return: The product of the two numbers.
        """
        return a * b

    def divide(self, a: int, b: int) -> float:
        """
        Divide one number by another.

        :param a: The numerator.
        :param b: The denominator.
        :return: The result of dividing the first number by the second.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b