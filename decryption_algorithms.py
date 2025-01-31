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
