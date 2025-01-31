import decryption_algorithms as da
import performance_testing as pt
import os
from rsa import RSA
from tabulate import tabulate
from fpdf import FPDF


def generate_pdf_report(results, oaep_results, rsa, message, ciphertext_chunks, key_length):
    """Generate a PDF report with the results of the RSA analysis."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(200, 10, txt="RSA Encryption Analysis Report", ln=True, align='C')
    pdf.ln(10)

    # Section 1: RSA Encryption Details
    pdf.set_font("Arial", size=14, style='B')
    pdf.cell(200, 10, txt="1. RSA Encryption Details", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Message: {message}", ln=True)
    pdf.cell(200, 10, txt=f"Key Length: {key_length} bits", ln=True)
    pdf.cell(200, 10, txt=f"Maximum bytes per chunk: {rsa.get_max_chunk_size()}", ln=True)
    pdf.cell(200, 10, txt=f"Encrypted chunks: {ciphertext_chunks}", ln=True)
    pdf.cell(200, 10, txt=f"RSA Values: n = {rsa.n}, e = {rsa.e}, d = {rsa.d}", ln=True)
    pdf.ln(10)

    # Section 2: Decryption Algorithm Results
    pdf.set_font("Arial", size=14, style='B')
    pdf.cell(200, 10, txt="2. Decryption Algorithm Results", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Results of various decryption algorithms:", ln=True)

    # Convert results to a table
    table = tabulate(results, headers=['Algorithm', 'Time', 'Success', 'Decrypted Message'], tablefmt='grid')
    pdf.multi_cell(0, 10, txt=table)
    pdf.ln(10)

    # Section 3: RSA-OAEP Performance
    pdf.set_font("Arial", size=14, style='B')
    pdf.cell(200, 10, txt="3. RSA-OAEP Performance", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"RSA-OAEP Encryption Time: {oaep_results['encryption_time']:.4f}s", ln=True)
    pdf.cell(200, 10, txt=f"RSA-OAEP Decryption Time: {oaep_results['decryption_time']:.4f}s", ln=True)
    pdf.cell(200, 10, txt=f"Decrypted Message: {oaep_results['plaintext']}", ln=True)

    # Check if the output directory exists
    if not os.path.exists("output"):
        os.makedirs("output")

    # Save the PDF to output/result.pdf
    pdf.output("output/rsa-analysis-report.pdf")
    print("\nPDF report generated: output/rsa-analysis-report.pdf")


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
        "Brute Force": da.BruteForce.decrypt,
        "Euler's Factorization": da.EulersFactorization.decrypt,
        "Quadratic Sieve": da.QuadraticSieve.decrypt,
        "General Number Field Sieve": da.GNFS.decrypt,
        "Shor's Algorithm": da.ShorsAlgorithm.decrypt
    }

    results = []
    print("\nTesting decryption algorithms...")
    print("=" * 50)
    
    for name, algo in algorithms.items():
        print(f"\nTesting {name}...")
        result = pt.test_algorithm(algo, rsa.n, message, ciphertext_chunks, timeout=60)
        results.append([
            name,
            f"{result['time']:.4f}s",
            "[Success]" if result['success'] else "[Failed]",
            result['decrypted'] if result['success'] else "Failed"
        ])

    print("\nResults:")
    print("=" * 50)
    print(tabulate(results, 
                  headers=['Algorithm', 'Time', 'Success', 'Decrypted Message'],
                  tablefmt='grid'))

    print("\nMeasuring RSA-OAEP performance...")
    oaep_results = pt.measure_rsa_oaep(key_length, message)

    if oaep_results['encryption_time'] is not None:
        print(f"RSA-OAEP Encryption Time: {oaep_results['encryption_time']:.4f}s")
    if oaep_results['decryption_time'] is not None:
        print(f"RSA-OAEP Decryption Time: {oaep_results['decryption_time']:.4f}s")
    if oaep_results['plaintext'] is not None:
        print(f"Decrypted Message: {oaep_results['plaintext']}")

    # Generate PDF report
    generate_pdf_report(results, oaep_results, rsa, message, ciphertext_chunks, key_length)


if __name__ == "__main__":
    main()
