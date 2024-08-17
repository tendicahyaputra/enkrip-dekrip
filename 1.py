import random   # digunakan untuk menghasilkan angka acak
import string   # untuk menyediakan konstanta string

chars = " " + string.punctuation + string.digits + string.ascii_letters # punctuation utk menampilkan kumpulan karakter tanda baca.
chars = list(chars)                                                     # digits utk menampilkan karakter digit 0-9
key = chars.copy()                                                      # ascii_letters utk menampilkan huruf besar dan kecil

random.shuffle(key)     # digunakan untuk mengacakan daftar kunci

print(f"chars: {chars}")
print(f"key: {key}")


#encriptions
plain_text = input("Enter a message to encrypt:")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)                 # Proses enkripsi
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypt message: {cipher_text}")

#Decryptions
cipher_text = input("Enter a message to encrypt:")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]                      # Proses Deskripsi

print(f"encrypt message: {cipher_text}")
print(f"original message: {plain_text}")

