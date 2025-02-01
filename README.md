<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center"> 
  <a href="https://github.com/feiryrej/rsa-attacker-prototype">
    <img src="https://github.com/user-attachments/assets/2ded5581-28e7-4900-a529-74a2dcc352f9" alt="Logo" width="140" height="140">
  </a>

  <h1 align="center">RSA-Attacker-Prototype</h1> 
  <p align="center">
    Mapping Attack Resistance and Vulnerabilities
    <br />
    <a href="https://drive.google.com/drive/folders/13OPHTafFAbe67403Vr7lv9-Q2bJgp9s2?usp=sharing"><strong>Explore the paper »</strong></a>
    <br />
    <br />
    <a href="#demo">View Demo</a>
    ·
    <a href="https://github.com/feiryrej/rsa-attacker-prototype/issues">Report Bug</a>
    ·
    <a href="https://github.com/feiryrej/rsa-attacker-prototype/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
This project showcases the implementation of an RSA encryption and decryption system while also exploring various factorization methods used to break RSA security. The **RSA class** is responsible for generating cryptographic keys, ensuring secure message encryption using the **public exponent 65537**, and efficiently handling **message chunking** to fit within the RSA modulus size. By utilizing modular exponentiation, it guarantees a **secure encryption and decryption** process.

<!-- TABLE OF CONTENTS -->
## Table Of Contents
<ol>
  <li>
    <a href="#about-the-project">About The Code</a>
    <ul>
      <li><a href="#table-of-contents">Table Of Contents</a></li>
      <li><a href="#features">Features</a></li>
      <li><a href="#technologies">Technologies Used</a></li>
    </ul>
  </li>
  <li>
    <a href="#output-snapshots">Output Snapshots</a>
  </li>
  <li>
    <a href="#installation">Installation</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
    </ul>
  </li>
  <li>
    <a href="#run">Run</a>
  </li>
  <li>
    <a href="#contributors">Contributors</a>
  </li>
  <li>
    <a href="#license">License</a>
  </li>
</ol> 

<!-- FEATURES -->
## Features

This project implements an **RSA encryption and decryption system** with multiple functionalities, including secure key generation, message chunking, encryption, and decryption. It also evaluates various **factorization-based attack methods** to analyze RSA security.

### 🔐 RSA Encryption & Decryption  
- **Key Generation**: Dynamically generates RSA keys based on a configurable key length.  
- **Message Chunking**: Splits messages into manageable chunks that fit within the RSA key size.  
- **Secure Encryption**: Encrypts messages using modular exponentiation with **public exponent 65537**.  
- **Decryption Handling**: Recovers original plaintext from encrypted message chunks using the private key.  

### 🛠️ Factorization & Cryptanalysis  
Includes multiple factorization techniques to test RSA vulnerabilities:  
- **Brute-Force Factorization**: Attempts to find RSA prime factors through direct division.  
- **Euler’s Factorization Method**: Uses Euler’s method to find prime factors efficiently.  
- **Quadratic Sieve (QS)**: A sieve-based method for breaking RSA encryption.  
- **General Number Field Sieve (GNFS)**: A powerful method for factoring large numbers.  
- **Shor’s Algorithm (Simulated Classically)**: Uses quantum-inspired number theory principles.  

### ⏱️ Performance Testing & Benchmarking  
- **Algorithm Efficiency Analysis**: Evaluates execution time and success rate of different decryption techniques.  
- **RSA-OAEP Performance Test**: Measures encryption and decryption time using **Optimal Asymmetric Encryption Padding (OAEP) with SHA-256** for enhanced security.  
- **Automated Report Generation**: Displays test results in an easy-to-read tabulated format.  

### 🏗️ Modular & Expandable Design  
- **Pythonic Class Structure**: RSA and decryption algorithms are implemented as modular classes.  
- **Custom Key Length**: Users can define the RSA key size for flexible security testing.  
- **Exception Handling**: Handles encryption/decryption failures gracefully.  

This code serves both as a **demonstration of RSA encryption** and an **analysis of factorization-based attacks**, making it a valuable resource for cryptography enthusiasts, security researchers, and students. 🚀  

<!-- TECHNOLOGIES USED -->
## Technologies

This code utilizes various technologies and libraries to implement and analyze RSA encryption and decryption.  

- **[Python](https://www.python.org/)** – The primary programming language used for implementing RSA encryption, decryption, and factorization techniques.  
- **[SymPy](https://www.sympy.org/)** – Used for **prime number generation** and **greatest common divisor (GCD) calculations**.  
- **[Cryptography](https://cryptography.io/)** – Provides **RSA key generation, encryption, and decryption** with **Optimal Asymmetric Encryption Padding (OAEP) and SHA-256**.  
- **[Math & Random Modules](https://docs.python.org/3/library/math.html)** – Used for mathematical calculations, modular exponentiation, and secure random number generation.  
- **[Time Module](https://docs.python.org/3/library/time.html)** – Measures execution times for encryption, decryption, and factorization tests.  
- **[Typing Module](https://docs.python.org/3/library/typing.html)** – Provides type hints for better code clarity and maintainability.  
- **[Tabulate](https://pypi.org/project/tabulate/)** – Formats test results into a structured table for easy readability.  

These technologies enable **efficient RSA cryptography** while ensuring **modular, secure, and optimized performance** for testing encryption and decryption algorithms. 🚀

<!-- OUTPUT SNAPSHOTS -->
## Output Snapshots
