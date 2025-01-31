import random
from typing import List
from sympy import isprime
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

class RSA:
    """RSA implementation with configurable key length and message chunking"""
    
    def __init__(self, key_length: int = 1024):
        self.key_length = key_length
        self.e = 65537  # Standard RSA public exponent
        self.generate_keys()
        
    def get_max_chunk_size(self) -> int:
        """Calculate maximum number of bytes that can be encrypted with current key"""
        return (self.key_length // 8) - 1
        
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
    
    def chunk_message(self, message: str) -> List[int]:
        """Split message into chunks that fit within key length"""
        message_bytes = message.encode()
        chunk_size = self.get_max_chunk_size()
        chunks = []
        
        for i in range(0, len(message_bytes), chunk_size):
            chunk = message_bytes[i:i + chunk_size]
            chunk_int = int.from_bytes(chunk, 'big')
            chunks.append(chunk_int)
            
        return chunks
    
    def encrypt(self, message: str) -> List[int]:
        """Encrypt a string message using RSA with chunking"""
        chunks = self.chunk_message(message)
        encrypted_chunks = []
        
        for chunk in chunks:
            encrypted_chunk = pow(chunk, self.e, self.n)
            encrypted_chunks.append(encrypted_chunk)
            
        return encrypted_chunks
    
    def decrypt(self, ciphertext_chunks: List[int]) -> str:
        """Decrypt ciphertext chunks back to string using RSA"""
        decrypted_bytes = bytearray()
        
        for chunk in ciphertext_chunks:
            if chunk >= self.n:
                raise ValueError("Ciphertext chunk is too large for the chosen key length.")
            
            msg_int = pow(chunk, self.d, self.n)
            chunk_size = (msg_int.bit_length() + 7) // 8
            chunk_bytes = msg_int.to_bytes(chunk_size, 'big')
            decrypted_bytes.extend(chunk_bytes)
        
        try:
            return decrypted_bytes.decode()
        except UnicodeDecodeError:
            return "Decryption failed: Invalid message encoding."