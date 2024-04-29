
def Decrypt():
    import Hide_Folder
    import os
    from cryptography.fernet import Fernet

    # Function to load an encryption key from a file
    def load_key(key_file_path):
        with open(key_file_path, 'rb') as key_file:
            key = key_file.read()
        return key

    # Function to decrypt data
    def decrypt_data(encrypted_data, key):
        cipher_suite = Fernet(key)
        return cipher_suite.decrypt(encrypted_data)

    # Function to decrypt all .enc files in a folder and its subfolders
    def decrypt_folder(folder_path, key):
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                if file_name.endswith('.enc'):
                    encrypted_file_path = os.path.join(root, file_name)
                    with open(encrypted_file_path, 'rb') as encrypted_file:
                        encrypted_data = encrypted_file.read()
                    decrypted_data = decrypt_data(encrypted_data, key)
                    original_file_path = encrypted_file_path[:-4]  # Remove ".enc" from the file name
                    with open(original_file_path, 'wb') as original_file:
                        original_file.write(decrypted_data)
                    os.remove(encrypted_file_path)  # Remove the encrypted file

    # Specify the folder path where you want to decrypt files
    folder_path = 'E:\Codeing\Python Language\Projects\Project_12_Folder_Encryption_(LOCK)\.Lock.encrypted'

    # Specify the path for the encryption key file
    key_file_path = 'E:\Codeing\Python Language\key_file.key'


    # Load the encryption key
    key = load_key(key_file_path)

    # Decrypt all .enc files in the folder and its subfolders
    decrypt_folder(folder_path, key)

    print("Decryption completed.")
    Hide_Folder.Hide_Files_Folders(folder_path,'U')

