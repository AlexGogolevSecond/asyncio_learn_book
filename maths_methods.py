

def print_fib(number: int) -> None:
    
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    
    print(f'fib({number}) равно {fib(number)}')