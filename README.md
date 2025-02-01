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

This code serves both as a **demonstration of RSA encryption** and an **analysis of factorization-based attacks**, making it a valuable resource for cryptography enthusiasts, security researchers, and students.

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

These technologies enable **efficient RSA cryptography** while ensuring **modular, secure, and optimized performance** for testing encryption and decryption algorithms.

<!-- OUTPUT SNAPSHOTS -->
## Output Snapshots
<p align="center">
  <img src="https://github.com/user-attachments/assets/ff61ddc8-4a91-4952-8750-1b7ea860f8a1" alt="Output Screenshot 1" width="50%">
</p>

<!-- INSTALLATION -->
## Installation  
To run this RSA encryption and decryption project, you need **Python 3.8+** and several dependencies. Follow these steps to install and run the program:  

### Prerequisites
Ensure you have **Python 3.8 or later** installed. You can check your Python version with:
```
python --version
```
### Install Dependencies
Clone this repository and navigate to the project directory:
```
git clone https://github.com/your-username/rsa-encryption.git  
cd rsa-encryption  
```
Then, install the required Python packages:
```
pip install -r requirements.txt  
```
If requirements.txt is not available, manually install dependencies:
```
pip install sympy cryptography tabulate  
```

<!-- HOW TO RUN THE PROGRAM -->
##  Run
To start the RSA encryption analysis, run:
```
python main.py  
```
The program will prompt you to:

Enter a message for encryption.
Specify an RSA key length (e.g., 1024 or 2048 bits).
View the encrypted message, decryption process, and decryption algorithm results.

<!-- TABLE -->
## Contributors
  <table style="width: 100%; text-align: center;">
    <thead>
      <tr>
        <th>Name</th>
        <th>Avatar</th>
        <th>GitHub</th>
        <th>Contributions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Regina Bonifacio</td>
        <td><img src="https://avatars.githubusercontent.com/u/116869096?s=400&u=43146b191775802d9ab2f0f721b452ffc52c9efa&v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/feiryrej">feiryrej</a></td>
        <td>
          Regina set up the development environment and established the project codebase, laying the foundation for the system's implementation. 
          She was primarily responsible for designing and   implementing the decryption algorithms, which include brute-force factorization, Euler’s factorization method, 
          the quadratic sieve, the General Number Field Sieve (GNFS), and a classical simulation of Shor’s algorithm. In addition to her work on cryptanalysis, she facilitated 
          the overall development process, ensuring the code was efficient, structured, and maintainable. 
          Regina also collaborated closely with Acelle in refining and editing `main.py`, focusing on optimizing the encryption and decryption flow to enhance performance and accuracy.  
        </td>
      </tr>
      <tr>
        <td>Syruz Ken Domingo</td>
        <td><img src="https://avatars.githubusercontent.com/u/141235021?v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/sykeruzn">sykeruzn</a></td>
        <td>
          Syruz played a key role in the development of rsa, implementing the core RSA encryption and decryption system. He designed the key generation process, 
          ensuring the secure creation of RSA key pairs using random prime generation and modular exponentiation. To enhance encryption efficiency, he implemented message chunking, 
          allowing larger plaintexts to be processed while maintaining RSA’s security constraints.
        </td>
      </tr>
      <tr>
        <td>Hans Christian Queja</td>
        <td><img src="https://avatars.githubusercontent.com/u/65350664?v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/HansQueja">HansQueja</a></td>
        <td>
          Hans developed performance testing, which is responsible for evaluating the efficiency of encryption and decryption algorithms. He implemented test_algorithm, 
          a function that benchmarks decryption techniques by measuring execution time, verifying decryption success, and handling errors gracefully. Additionally, 
          he designed measure_rsa_oaep, which assesses the encryption and decryption performance of RSA using Optimal Asymmetric Encryption Padding (OAEP) with SHA-256. 
        </td>
      </tr>
      <tr>
        <td>Acelle Krislette Rosales</td>
        <td><img src="https://avatars.githubusercontent.com/u/143507354?v=4" alt="" style="border-radius: 50%; width: 50px;"></td>
        <td><a href="https://github.com/krislette">krislette</a></td>
        <td>
          Acelle developed and integrated the main execution script, ensuring the seamless coordination of RSA encryption, decryption, and performance analysis. She implemented the core 
          logic for handling user input, RSA key generation, and message encryption, making the system interactive and user-friendly. Acelle also structured the execution flow for testing 
          various decryption algorithms, integrating brute-force, Euler's factorization, the quadratic sieve, GNFS, and Shor's algorithm. Additionally, she developed the PDF report generation 
          feature using FPDF, allowing the results of RSA encryption, decryption, and performance analysis to be documented in a structured format. 
        </td>
      </tr>
    </tbody>
  </table>
</section>

<!-- LICENSE -->
## License

Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See [LICENSE](LICENSE) for more information.

<p align="right">[<a href="#readme-top">Back to top</a>]</p>
