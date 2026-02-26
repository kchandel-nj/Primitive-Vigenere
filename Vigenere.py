# Libraries
from CharToNum import ctn

class vigenere:

    def __init__(self) -> None:
        self.num = ctn()
        pass

    def encode(self, plaintext: str, key: str) -> str:
        """
        Encodes the plaintext using the given key.

        :param plaintext: The phrase to encode.
        :type plaintext: str
        :param key: The key to encode the phrase.
        :type key: str

        :return: The ciphertext.
        :rtype: str
        """

        ciphertext = ""
        if len(key) < len(plaintext):
            while len(key) < len(plaintext):
                key += key
            return self.encode(plaintext, key)
        else:
            for i in range(0, len(plaintext)):
                ciphertext += self.num.numToChar((self.num.charToNum(plaintext[i]) 
                                                  + self.num.charToNum(key[i])) % 26)

        return ciphertext
    
    def decode(self, ciphertext: str, key: str) -> str:
        """
        Decodes the ciphertext using the given key.

        :param ciphertext: The phrase to decode.
        :type ciphertext: str
        :param key: The key to decode the phrase.
        :type key: str

        :return: The plaintext.
        :rtype: str
        """
        
        plaintext = ""
        if len(key) < len(ciphertext):
            while len(key) < len(ciphertext):
                key += key
            return self.decode(ciphertext, key)
        else:
            for i in range(0, len(ciphertext)):
                plaintext += self.num.numToChar((self.num.charToNum(ciphertext[i]) 
                                                 - self.num.charToNum(key[i])) % 26)
        
        return plaintext