import os
from termcolor import colored

def encrypt_caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = ord(char) + shift - ord('a')
            shifted %= 26
            shifted += ord('a')
            if is_upper:
                shifted = chr(shifted).upper()
            else:
                shifted = chr(shifted)
            encrypted_text += shifted
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt_caesar_cipher(text, shift):
    return encrypt_caesar_cipher(text, -shift)

os.system('cls')

def main():
    while True:
        print("Menu:")
        print("1. Enkripsi Data")
        print("2. Dekripsi Data")
        print("3. Keluar")
        
        choice = input("Pilih opsi (1/2/3): ")
        
        if choice == '1':
            text = input("Masukkan teks yang ingin dienkripsi: ")
            shift = int(input("Masukkan jumlah pergeseran: "))
            # Menghapus spasi sebelum enkripsi
            text = text.replace(" ", "")
            encrypted_text = encrypt_caesar_cipher(text, shift)
            print(colored(f'Result : {str(encrypted_text)}', 'green'))
            print()
        elif choice == '2':
            text = input("Masukkan teks yang ingin didekripsi: ")
            shift = int(input("Masukkan jumlah pergeseran: "))
            decrypted_text = decrypt_caesar_cipher(text, shift)
            print(colored(f'Result : {str(decrypted_text)}', 'green'))
            print()
        elif choice == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()
