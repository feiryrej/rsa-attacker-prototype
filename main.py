from tabulate import tabulate
from rsa import RSA
import decryption_algorithms
from performance_testing import test_algorithm, measure_rsa_oaep


def main():
    """Main function to run RSA analysis"""
    print("\nRSA Encryption Analysis Tool")
    print("=" * 50)
    
    message = input("\nEnter a message to encrypt: ")
    key_length = int(input("Enter RSA key length: "))

    if key_length <= 0:
        print("\nError: Key length must be a positive integer.")
        return

    print("\nGenerating RSA keys and encrypting message...\n")
    try:
        rsa = RSA(key_length)
        max_chunk_size = rsa.get_max_chunk_size()
        print(f"Maximum bytes per chunk: {max_chunk_size}")
        
        ciphertext_chunks = rsa.encrypt(message)
        print(f"\nEncrypted chunks: {ciphertext_chunks}")
        print(f"\nRSA Values: \nn = {rsa.n}, \ne = {rsa.e}, \nd = {rsa.d}")
        
        # Test decryption
        decrypted = rsa.decrypt(ciphertext_chunks)
        print(f"\nDecryption test: {decrypted}")
        
    except Exception as e:
        print(f"Error during RSA key generation or encryption: {e}")
        return
    
    # Test all algorithms
    algorithms = {
        "Brute Force": decryption_algorithms.BruteForce.decrypt,
        "Euler's Factorization": decryption_algorithms.EulersFactorization.decrypt,
        "Quadratic Sieve": decryption_algorithms.QuadraticSieve.decrypt,
        "General Number Field Sieve": decryption_algorithms.GNFS.decrypt,
        "Shor's Algorithm": decryption_algorithms.ShorsAlgorithm.decrypt
    }
    
    results = []
    print("\nTesting decryption algorithms...")
    print("=" * 50)
    
    for name, algo in algorithms.items():
        print(f"\nTesting {name}...")
        result = test_algorithm(algo, rsa.n, message, ciphertext_chunks, timeout=60)
        results.append([
            name,
            f"{result['time']:.4f}s",
            "✓" if result['success'] else "✗",
            result['decrypted'] if result['success'] else "Failed"
        ])
    
    print("\nResults:")
    print("=" * 50)
    print(tabulate(results, 
                  headers=['Algorithm', 'Time', 'Success', 'Decrypted Message'],
                  tablefmt='grid'))
    
    print("\nMeasuring RSA-OAEP performance...")
    oaep_results = measure_rsa_oaep(key_length, message)

    if oaep_results['encryption_time'] is not None:
        print(f"RSA-OAEP Encryption Time: {oaep_results['encryption_time']:.4f}s")
    if oaep_results['decryption_time'] is not None:
        print(f"RSA-OAEP Decryption Time: {oaep_results['decryption_time']:.4f}s")
    if oaep_results['plaintext'] is not None:
        print(f"Decrypted Message: {oaep_results['plaintext']}")


if __name__ == "__main__":
    main()
