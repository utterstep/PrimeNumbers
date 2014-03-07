# coding=utf-8


def _eratosthenes_sieve_np(limit):
    """
    Возвращает все простые числа из промежутка [1; limit].

    Реализация решета Эратосфена, использующая модуль numpy.
    Быстрее "чистой" Python-реализации приблизительно в 5 раз.
    """
    from math import sqrt
    from numpy import arange, ones

    if limit < 1:
        raise ValueError("Правая граница промежутка, в котором осуществляется поиск, должна быть не меньше 1.")

    sqrt_limit = int(sqrt(limit)) + 1

    is_prime = ones(limit + 1, dtype='bool')

    is_prime[0:2] = False
    is_prime[arange(2 * 2, limit + 1, 2)] = False

    for i in xrange(3, sqrt_limit, 2):
        if is_prime[i]:
            is_prime[arange(i * i, limit + 1, i)] = False

    primes = arange(0, limit + 1)[is_prime]
    primes.setflags(write=False)
    return primes


def _eratosthenes_sieve(limit):
    """
    Возвращает все простые числа из промежутка [1; limit].

    Реализация решета Эратосфена, использующая только стандартную библиотеку Python.
    """
    from math import sqrt

    if limit < 1:
        raise ValueError("Правая граница промежутка, в котором осуществляется поиск, должна быть не меньше 1.")

    sqrt_limit = int(sqrt(limit)) + 1
    sqrt_limit = sqrt_limit + 1 if sqrt_limit % 2 == 0 else sqrt_limit

    is_prime = [True] * (limit + 1)
    primes = []

    if limit > 2:
        primes.append(2)

    for i in xrange(3, sqrt_limit, 2):
        if is_prime[i]:
            primes.append(i)

            for j in xrange(i * 2, limit, i):
                is_prime[j] = False

    for i in xrange(sqrt_limit, limit + 1, 2):
        if is_prime[i]:
            primes.append(i)

    return tuple(primes)


def prime_sieve(limit):
    """
    Возвращает все простые числа из промежутка [1; limit].

    При первом запуске проверяет, установлен ли модуль numpy, если да - использует более быстрый метод.
    """
    try:
        import numpy
        prime_sieve = _eratosthenes_sieve_np

    except ImportError:
        prime_sieve = _eratosthenes_sieve

    return prime_sieve(limit)


def get_first_primes(count):
    """
    Возвращает первые count простых чисел.

    Использует неравенство p_n < n * (ln n + ln ln n) (при n > 5).
    """
    from math import log
    lim = lambda x: int(x * (log(x) + log(log(x))))

    if count < 0:
        raise ValueError("count < 0")

    if count <= 5:
        return prime_sieve(11)[:count]

    return prime_sieve(lim(count))[:count]
