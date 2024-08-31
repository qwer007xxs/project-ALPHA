** นี่คือ source code ที่ยังไม่ run เป็นแบบ .exe เท่านั้นจึงต้องอาศัย (click me).bat ในการทดสอบ **

** หากต้องการ run แบบ exe จะต้อง compile file ที่ชื่อว่า onefile.py ใน
https://github.com/qwer007xxs/project-ALPHA/releases/tag/project-ALPHA เท่านั้น **

**หมายเหตุสำคัญ**
โปรเจคนี้ถูกสร้างขึ้นเพื่อการศึกษาเท่านั้น และไม่อนุญาตให้ใช้เพื่อเจตนาร้ายอื่นๆ การนำไวรัสที่พัฒนาไปใช้ในทางที่ผิดอาจมีผลกระทบทางกฎหมายและจริยธรรมอย่างร้ายแรง

**ผลงาน**
   การพัฒนาไวรัสเพื่อการศึกษาการทำงานของ Antivirus และ Windows Defender
   เพื่อศึกษาอันตรายจากการกดไฟล์ที่ไม่รู้จัก
   และการ login โดยไม่ต้องใช้ Password หรือและ การ Bypass การยืนยันตัวตน 2 ชั้น

**รายละเอียดโครงการ**
- วัตถุประสงค์ :เพื่อศึกษาว่า Windows defender นั้นทำงานอย่างไรและสามารถป้องกันภัยอันตรายได้จริงหรือไม่
   และถ้าหากการเกิดการกดไฟล์ที่เราไม่รู้จักจะสามารถเข้าถึง Social Media ต่างๆของเราได้หรือไม่
- การใช้งาน: เพื่อการศึกษาและวิจัยเท่านั้น

**ขอบเขตงาน**
 
 1.การออกแบบและพัฒนาไวรัส
- ออกแบบไวรัสที่มีความซับซ้อนและสามารถทำงานได้ในระบบปฏิบัติการ Windows
- ใช้ภาษาโปรแกรมมิ่งที่ใช้ในการพัฒนา คือ Python DOS/Windows shell scrip

2.การทดสอบไวรัสในสภาพแวดล้อมที่ควบคุม
- ทดสอบไวรัสในสภาพแวดล้อมทั้ง Windows 10 และ Windows 11
- database SQL ที่จะใช้ test คือ phpmyadmin 

3.การวิเคราะห์การตอบสนองของโปรแกรมป้องกันไวรัส
- วิเคราะห์การตอบสนองของโปรแกรม Antivirus และ Windows Defender ต่อไวรัสที่สร้างขึ้น
- บันทึกและวิเคราะห์ข้อมูลที่ได้จากการตรวจจับ การกักกัน และการกำจัดไวรัส

/!\ข้อจำกัด/!\
ต้อง run โปรแกรม ตอนปิด google chrome เท่านั้นไม่ว่าจะเป็น source code หรือ .exe
ไม่งั้น error permission
  
**วิธี run program**
1. แก้ไขโปรแกรมในโฟลเดอร์ source code
2. ต้อง set ค่า database ก่อน ตัวอย่างเช่น
```
	CREATE DATABASE IF NOT EXISTS user;
	USE user;
	CREATE TABLE IF NOT EXISTS user_log (
	id INT AUTO_INCREMENT PRIMARY KEY,
	user VARCHAR(255) NOT NULL,
	data TEXT NOT NULL,
	log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);
```
3. ตั้งค่า connect database ที่บรรทัด 102
```
 conn = mysql.connector.connect(host="host", user="host", password=password", database="database")
 ```
4.0 (source code)หากตองการ run program ต้องปลี่ยนนามสกุล file เป็น tab.py เป็น tab.pdf และ hidden.bat เป็น hidden.pdf
4.1 (exe)หากตองการ run program จะต้อง compile file ที่ชื่อว่า onefile.py ใน 
https://github.com/qwer007xxs/project-ALPHA/releases/tag/project-ALPHA

**หลักการทำงานของโปรแกรม**
1. อันดับแรกโปรแกรมจะทำการล็อคหน้าจอของผู้ใช้ 
2. โปรแกรมจะเปลี่ยนนามสกุลไฟล์ hidden.pdf และ tab.pdf เปลี่ยนเป็น hidden.bat และ tab.py ตามลำดับ
3. ถ้าหากว่าในเครื่องนั้นไม่ได้ติดตั้ง python เอาไว้โปรแกรมก็จะทำการลง python จากไฟล์ python installer .bat
4. จากนั้นก็จะ run ไฟล์ tab.py
5. โดย tab.py จะทำการดึงคุกกี้จาก google chrome ออกมาและทำการอัพโหลดไปที่ Database server ที่ตั้งค่าเอาไว้
6. หลังจากนั้นโปรแกรมตัวนี้จะทำการซ่อนตัวอยู่ในเครื่องของผู้ใช้โดยที่ hidden.pdf จะทำการฝังตัวเองไว้ใน Start Up และ tab.pdf จะถูก copy ไปที่ userprofile folder

**ผลลัพธ์**
- จากกันที่นำไฟล์ของโปรแกรมเราทั้งหมดมาสแกนด้วย Third party anti-virus และของ Windows defender นั้นพบว่าไม่สามารถตรวจพบไวรัสหรือความผิดปกติใดๆ
  แต่ถ้าหากว่าเราทำการ Export เป็นไฟล์ .exe แล้ว Windows 11 จะตรวจพบ Trojan ทันที
  แต่ Windows 10 นั้นยังไม่พบความผิดปกติใดๆ
  
- พบว่าคุกกี้ที่ตกอยู่ในความเสี่ยงนั้นคือคุกกี้ของ Facebook เนื่องจากสามารถทำการ login โดยผ่านการป้องกัน 2 ชั้นไปได้และไม่มีการแจ้งเตือนใดๆอาจรวมทั้ง Messenger 
  Instagram หรืออาจจะมีคุกกี้อื่นๆอีกที่ตกอยู่ในความเสี่ยง ขณะนี้ผมกำลังวิจัยว่าคุกกี้นั้นสามารถใช้เพื่อ login เข้าอีเมลได้หรือไม่
