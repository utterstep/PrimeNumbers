# coding=utf-8
from django.db import models
import PrimeNumbers.settings as settings


class PrimeNumber(models.Model):
    """
    Модель простого числа.
    """
    index = models.IntegerField()

    @property
    def value(self):
        """
        Возвращает простое число с порядковым номером index.
        """
        return PrimeNumber.__get_value(self.index)

    @staticmethod
    def __get_value(index):
        """
        Возвращает простое число с порядковым номером index.

        При первом обращении вычисляет все MAX_INDEX первых простых и кеширует их.


        >>> prime = PrimeNumber(index=10)
        >>> prime.value
        29
        >>> prime.index = 2
        >>> prime.value
        3
        >>> prime.index = 5
        >>> prime.value
        11
        """
        from django.core.cache import cache
        from primes.computing.prime_sieve import get_first_primes

        CACHE_ID = 'primes'

        primes = cache.get(CACHE_ID)
        if primes is None:
            primes = get_first_primes(settings.MAX_INDEX)
            cache.set(CACHE_ID, primes, None)

        return primes[index - 1]
