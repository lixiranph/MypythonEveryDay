"""
自定义模块
    实现数学的四则运算
    两个数的加减乘除
"""
__all__ = ['add', 'sub', 'mul', 'div']  # 全局变量all（python3中不提倡使用）


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


if __name__ == '__main__':
    a = 10
    b = 2
    print(f'加{add(a, b)}')
    print(f'减{sub(a, b)}')
    print(f'乘{mul(a, b)}')
    print(f'除{div(a, b)}')
    print(__name__)
