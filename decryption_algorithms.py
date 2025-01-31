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
