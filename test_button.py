import tkinter as tk

def do_something():
    print("Button 1 pressed!")
    # ทำสิ่งที่ต้องการเมื่อผู้ใช้กดปุ่ม 1 ที่นี่

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Button Example")

# สร้างปุ่ม
button = tk.Button(root, text="Press Button 1", command=do_something)
button.pack(pady=10)

# เริ่มการทำงานของ GUI
root.mainloop()
