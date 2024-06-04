from random import randint


def CodeGenerator(length : int = 6) -> str:
    code = [str(randint(0, 9)) for i in range(length)]
    return "".join(code)
