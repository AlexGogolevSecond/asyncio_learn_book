from random import randint


def lalala(a: int):
    l = randint(1, 10)
    print(f'{l=}')
    return l

def some():
    a = 0
    b = 1
    d = lalala(a)
    c = a + b + d
    print(c)
    return c
    
if __name__ == "__main__":
    res = some()
    print(f'{res=}')