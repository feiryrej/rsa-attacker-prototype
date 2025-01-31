import math
import random
from sympy import isprime

class RSA:
    """RSA implementation with configurable key length and message chunking"""
    
    def __init__(self, key_length: int = 1024):
            self.key_length = key_length
            self.e = 65537  # Standard RSA public exponent
            self.generate_keys()

    def generate_prime(self, bits: int) -> int:
        """Generate a prime number of specified bit length"""
        while True:
            num = random.getrandbits(bits)
            num |= (1 << bits - 1) | 1  
            if isprime(num):
                return num

    def generate_keys(self):
        """Generate RSA key pairs"""
        half_length = self.key_length // 2
        self.p = self.generate_prime(half_length)
        self.q = self.generate_prime(half_length)
        
        while self.p == self.q:
            self.q = self.generate_prime(half_length)
        
        self.n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        self.d = pow(self.e, -1, phi)