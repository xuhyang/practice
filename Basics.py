class Basics :

    def factorialIterative(self, n: int) -> int :
        result = 1
        for i in range(2, n+1):
            result = result * i

        return result

    def factorialRecursive(self, n: int) -> int :
        if n == 1 :
            return 1

        return n * self.factorialRecursive(n - 1)

    def fibonacciIterative(self, n: int) -> int :
        a, b = 0, 1

        for i in range(n) :
            a, b = b, a+b

        return a

    def fibonacciRecursive(self, n: int) -> int :
        if n == 0 or n == 1 :
            return n

        return self.factorialIterative(n - 1) + self.factorialIterative(n - 2)

