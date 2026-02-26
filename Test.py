# Libraries
from CharToNum import ctn
from Vigenere import vigenere as v

cvt = ctn()

alphabet = list(map(chr, range(97, 123)))

for a in alphabet:
    print(cvt.charToNum(a))

for a in alphabet:
    print(cvt.numToChar(cvt.charToNum(a)))

coder = v()
ciphertext1 = coder.encode("hello", "fires")
print(ciphertext1)
print(coder.decode(ciphertext1, "fires"))

ciphertext2 = coder.encode("blanks", "bobbob")
print(ciphertext2)
print(coder.decode(ciphertext2, "bobbob"))

ciphertext3 = coder.encode("blanks", "bob")
print(ciphertext3)
print(coder.decode(ciphertext3, "bob"))