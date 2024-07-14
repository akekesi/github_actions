import numpy as np # only to test pip install

from typing import Optional


def func_00(arg: Optional[float] = None):
    if arg is not None:
        return arg
    return 0.123


if __name__ == "__main__":
    res = func_00()
    print(f"{res = }")

    arg = -0.123456789
    res = func_00(arg=arg)
    print(f"{res = }")
