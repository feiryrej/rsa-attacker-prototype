# performance_testing.py
import time
from typing import Dict, List
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def test_algorithm(algo, n: int, original_message: str, ciphertext_chunks: List[int], timeout: int = 60) -> Dict:
    """Test a single decryption algorithm and return performance metrics"""
    start_time = time.time()
    result = algo(n, timeout)
    end_time = time.time()
    time_taken = end_time - start_time
    
    success = result is not None
    decrypted = None
    if success:
        try:
            p, q = result
            phi = (int(p) - 1) * (int(q) - 1)
            d = pow(65537, -1, phi)
            decrypted_chunks = []
            for chunk in ciphertext_chunks:
                msg_int = pow(int(chunk), int(d), int(n))
                decrypted_chunks.append(msg_int)
            
            decrypted_bytes = bytearray()
            for chunk in decrypted_chunks:
                chunk_size = (chunk.bit_length() + 7) // 8
                chunk_bytes = chunk.to_bytes(chunk_size, 'big')
                decrypted_bytes.extend(chunk_bytes)
            
            decrypted = decrypted_bytes.decode()
            success = decrypted == original_message
        except Exception as e:
            print(f"Decryption error: {e}")
            success = False
    
    return {
        'time': time_taken,
        'success': success,
        'decrypted': decrypted if success else None
    }

def measure_rsa_oaep(key_length: int, message: str) -> Dict:
    """Measure RSA-OAEP encryption and decryption times"""
    try:
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_length)
        public_key = private_key.public_key()
    except ValueError as e:
        print(f"Key generation error: {e}")
        return {
            'encryption_time': None,
            'decryption_time': None,
            'plaintext': None
        }
    
    # Encrypt
    start_time = time.time()
    try:
        ciphertext = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        encryption_time = time.time() - start_time
    except Exception as e:
        print(f"Encryption error: {e}")
        return {
            'encryption_time': None,
            'decryption_time': None,
            'plaintext': None
        }
    
    # Decrypt
    start_time = time.time()
    try:
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()
        decryption_time = time.time() - start_time
    except Exception as e:
        print(f"Decryption error: {e}")
        return {
            'encryption_time': encryption_time,
            'decryption_time': None,
            'plaintext': None
        }
    
    return {
        'encryption_time': encryption_time,
        'decryption_time': decryption_time,
        'plaintext': plaintext
    }