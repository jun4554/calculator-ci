class Calculator:
    def add(self, a, b):
        return a + b

    def add2(self, a, b, c):
        return a + b + c

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("0で割ることはできません")
        return a / b