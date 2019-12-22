import dis
from bytecode import Bytecode


def f(x):
    return x


dis.dis(f)

for each in Bytecode.from_code(f.__code__):
    print(each)
