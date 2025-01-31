This code implements an RSA encryption and decryption system, along with several methods for factorizing RSA keys. The RSA class handles key generation, message chunking, encryption, and decryption. 
It generates prime numbers to form public and private keys, ensuring secure encryption using the standard RSA public exponent (65537). 
Messages are split into chunks to fit within the key length, encrypted using modular exponentiation, and later decrypted using the private key. 
The Decryption class provides multiple factorization techniques to break RSA encryption, including Euler’s factorization, the quadratic sieve, the General Number Field Sieve (GNFS), Shor’s quantum algorithm (simulated classically), and brute-force factorization. Each method attempts to retrieve the original prime factors of a given RSA modulus. 
The test_algorithm function evaluates the efficiency of these decryption techniques by timing their execution and verifying successful decryption.
Additionally, the measure_rsa_oaep function tests RSA encryption and decryption using Optimal Asymmetric Encryption Padding (OAEP) with SHA-256, ensuring robust security measures. 
The code as a whole is designed to demonstrate both RSA encryption's strength and the feasibility of factorization-based attacks under different conditions.
