import os
import shutil

folder_path = '/folder'  

file_types = {
    'Images': ['jpg', 'jpeg', 'png', 'gif'],
    'Documents': ['pdf', 'doc', 'docx', 'txt'],
    'Audio': ['mp3', 'wav'],
    'Videos': ['mp4', 'avi', 'mov'],
    'Scripts': ['py', 'sh', 'bat'],
}


def organize_files():
    for filename in os.listdir(folder_path):
        file_extension = filename.split('.')[-1].lower()
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue
        moved = False
        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                target_folder = os.path.join(folder_path, folder_name)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                shutil.move(os.path.join(folder_path, filename), os.path.join(target_folder, filename))
                moved = True
                break
        if not moved:
            other_folder = os.path.join(folder_path, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(os.path.join(folder_path, filename), os.path.join(other_folder, filename))

    print("Files ka achi tarah se intezaam ho gaya hai!")
if __name__ == "__main__":
    organize_files()
