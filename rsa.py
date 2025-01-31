class RSA:
    """RSA implementation with configurable key length and message chunking"""
    
    def __init__(self, key_length: int = 1024):
        self.key_length = key_length
        self.e = 65537  # Standard RSA public exponent
        self.generate_keys()