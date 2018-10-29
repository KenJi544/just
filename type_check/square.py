from typing import Sequence

def square(x: int) -> int:
    """
    calculates power(x,2)
    """
    return x**2

if __name__ == "__main__":
    print(square(2))
    print(square('foo'))
