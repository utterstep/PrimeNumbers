import unittest
from primes.computing import prime_sieve


class PrimeSieveTest(unittest.TestCase):
    def testGeneral(self):
        self.assertItemsEqual([2, 3, 5, 7, 11], prime_sieve.prime_sieve(11))
        self.assertItemsEqual([2, 3, 5, 7, 11], prime_sieve.prime_sieve(12))
        self.assertItemsEqual([2, 3, 5, 7, 11, 13], prime_sieve.prime_sieve(13))

        self.assertItemsEqual([], prime_sieve.prime_sieve(1))
        self.assertRaises(ValueError, prime_sieve.prime_sieve, 0)
        self.assertRaises(ValueError, prime_sieve.prime_sieve, -1)

    def testNumpySieve(self):
        try:
            self.assertItemsEqual([2, 3, 5, 7, 11], prime_sieve._eratosthenes_sieve_np(11))
            self.assertItemsEqual([2, 3, 5, 7, 11], prime_sieve._eratosthenes_sieve_np(12))
            self.assertItemsEqual([2, 3, 5, 7, 11, 13], prime_sieve._eratosthenes_sieve_np(13))

            self.assertItemsEqual([], prime_sieve._eratosthenes_sieve_np(1))
            self.assertRaises(ValueError, prime_sieve._eratosthenes_sieve_np, 0)
            self.assertRaises(ValueError, prime_sieve._eratosthenes_sieve_np, -1)
        except ImportError:
            pass

    def testSimpleSieve(self):
        self.assertItemsEqual([2, 3, 5, 7, 11], prime_sieve._eratosthenes_sieve(11))
        self.assertItemsEqual([2, 3, 5, 7, 11], prime_sieve._eratosthenes_sieve(12))
        self.assertItemsEqual([2, 3, 5, 7, 11, 13], prime_sieve._eratosthenes_sieve(13))

        self.assertItemsEqual([], prime_sieve._eratosthenes_sieve(1))
        self.assertRaises(ValueError, prime_sieve._eratosthenes_sieve, 0)
        self.assertRaises(ValueError, prime_sieve._eratosthenes_sieve, -1)

    def testIndexed(self):
        self.assertItemsEqual([2, 3], prime_sieve.get_first_primes(2))
        self.assertItemsEqual([2, 3, 5, 7, 11], prime_sieve.get_first_primes(5))
        self.assertItemsEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], prime_sieve.get_first_primes(10))
        self.assertItemsEqual([], prime_sieve.get_first_primes(0))
        self.assertRaises(ValueError, prime_sieve.get_first_primes, -1)

if __name__ == '__main__':
    unittest.main()