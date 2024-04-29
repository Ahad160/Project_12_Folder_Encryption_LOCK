
def Hide_Files_Folders(folder_path,user):
    import os
    if user == 'H':
        A='+h'
        B="Hide"
    elif user == 'U':
        A='-h' 
        B="Unhide"   

    # Use the attrib command to hide all files and subfolders in the folder
    os.system(f'attrib {A} "{folder_path}\\*" /s /d')
    
    # Hide the folder itself
    os.system(f'attrib {A} "{folder_path}"')
    
    print(f"Folders {B} completed.")
    exit()


# folder_path = r'E:\Codeing\Python Language\Projects\Project-12_Folder_Encryption_(LOCK)\.Lock.encrypted'
# Hide_Files_Folders(folder_path)
