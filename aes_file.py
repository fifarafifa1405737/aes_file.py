from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

# Password
password = "kriptografi123"

# Membuat key AES 128-bit dari password
key = hashlib.md5(password.encode()).digest()

# =====================
# ENKRIPSI FILE
# =====================
def encrypt_file():
    with open("data.txt", "rb") as f:
        data = f.read()

    print("\n=== ISI FILE ASLI ===")
    print(data.decode())

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    with open("encrypted.bin", "wb") as f:
        f.write(encrypted_data)

    print("\n=== HASIL ENKRIPSI (HEX) ===")
    print(encrypted_data.hex())

    print("\nFile berhasil dienkripsi.")

# =====================
# DEKRIPSI FILE
# =====================
def decrypt_file():
    with open("encrypted.bin", "rb") as f:
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(
        cipher.decrypt(encrypted_data),
        AES.block_size
    )

    with open("hasil_dekripsi.txt", "wb") as f:
        f.write(decrypted_data)

    print("\n=== HASIL DEKRIPSI ===")
    print(decrypted_data.decode())

    print("\nFile berhasil didekripsi.")

# =====================
# MENU
# =====================
while True:
    print("\n=== MENU AES ===")
    print("1. Enkripsi File")
    print("2. Dekripsi File")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        encrypt_file()

    elif pilihan == "2":
        decrypt_file()

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")