import math
import random
import time
from typing import Tuple, Optional
from sympy import isprime, gcd

class BruteForce:
    @staticmethod
    def decrypt(n: int, timeout: int = 60) -> Optional[Tuple[int, int]]:
        """Brute-force factorization"""
        start_time = time.time()
        i = 2
        while i * i <= n and time.time() - start_time < timeout:
            if n % i == 0:
                return (i, n // i)
            i += 1
        return None

class EulersFactorization:
    @staticmethod
    def decrypt(n: int, timeout: int = 60) -> Optional[Tuple[int, int]]:
        """Euler's factorization method"""
        start_time = time.time()
        a = math.isqrt(n)
        
        while time.time() - start_time < timeout:
            b2 = a * a - n
            if b2 < 0:
                a += 1
                continue
            b = math.isqrt(b2)
            if b * b == b2:
                return (a - b, a + b)
            a += 1
        return None
    
class QuadraticSieve:
    @staticmethod
    def decrypt(n: int, timeout: int = 60) -> Optional[Tuple[int, int]]:
        """Quadratic Sieve algorithm"""
        def is_smooth(x: int, factor_base: list) -> bool:
            temp = abs(x)
            for p in factor_base:
                while temp % p == 0:
                    temp //= p
            return temp == 1

        start_time = time.time()
        limit = int(math.exp(math.sqrt(math.log(n) * math.log(math.log(n)))))
        factor_base = [p for p in range(2, min(limit, 100)) if isprime(p)]
        
        x = math.isqrt(n)
        while time.time() - start_time < timeout:
            x_squared = x * x - n
            if is_smooth(x_squared, factor_base):
                factor = gcd(x, n)
                if 1 < factor < n:
                    return (factor, n // factor)
            x += 1
        return None

