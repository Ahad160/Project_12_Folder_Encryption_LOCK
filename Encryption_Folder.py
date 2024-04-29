
def Encrypt():
    import Hide_Folder
    import os
    from cryptography.fernet import Fernet
    import Hide_Folder

    # Function to generate and save an encryption key to a file
    def Generate_Key(key_Path):
        if not os.path.exists(key_Path):
            key = Fernet.generate_key()
            with open(key_Path, 'wb') as key_file:
                key_file.write(key)
        else:
            with open(key_Path, 'rb') as key_file:
                key = key_file.read()
        return key

    # Function to encrypt data
    def encrypt_data(data, key):
        cipher_suite = Fernet(key)
        return cipher_suite.encrypt(data)

    # Function to encrypt all files in a folder and its subfolders
    def encrypt_folder(folder_path, key):
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                with open(file_path, 'rb') as file:
                    data = file.read()
                encrypted_data = encrypt_data(data, key)
                encrypted_file_path = file_path + '.enc'  # Appending ".enc" to the original file name
                with open(encrypted_file_path, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted_data)
                os.remove(file_path)  # Remove the original file if you want to replace it

    # Specify the folder path where you want to encrypt files
    folder_path = 'E:\Codeing\Python Language\Projects\Project_12_Folder_Encryption_(LOCK)\.Lock.encrypted'

    # Specify the path for the encryption key file
    key_file_path = 'E:\Codeing\Python Language\Projects\Project_12_Folder_Encryption_(LOCK)\key_file.key'

    # Generate or load the encryption key
    key = Generate_Key(key_file_path)

    # Encrypt all files in the folder and its subfolders
    encrypt_folder(folder_path, key)

    print("Encryption completed.")
    Hide_Folder.Hide_Files_Folders(folder_path,'H')


