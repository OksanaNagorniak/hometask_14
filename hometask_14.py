# Написать декоратор @cache который будет кэшировать входные и выходные данные
# функции. Для хранения входных и выходных данных нужно использовать словарь. Входные данные обязательно
# должны быть immutable типами. Важно что для каждой декорируемой функции должен быть свой словарь.

def cache_decorator(func):
    data = dict()

    def inner(*args):
        if args not in data:
            data[args] = func(*args)
        return data[args]

    return inner


@cache_decorator
def triangle_area(a: float, b: float) -> float:
    print(f' Результат выполнения triangle_area ({a}, {b})')
    return a * b


@cache_decorator
def circle_area(r: float) -> float:
    print(f'Результат выполнения circle_area ({r})')
    return 3.14 * (r * r)


print(triangle_area(5, 10))
print(triangle_area(5, 10))
print(circle_area(20))
print(triangle_area(10, 10))
print(circle_area(20))
