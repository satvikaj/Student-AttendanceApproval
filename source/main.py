from tkinter import Tk,Frame,Label,Entry,Button,messagebox
from PIL import Image,ImageTk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="krish@444",
    database="attendance"
)
mycursor = mydb.cursor()

fonts = ('Courier New', 13, 'bold')
fonts1 = ('Courier New', 17, 'bold')

root = Tk()
root.resizable(0,0)

class Home:
    def __init__(self,root):
        self.root=root
        self.root.title("HOME")
        self.page = Frame(self.root,width=1000,height=600)
        self.page.place(x=0,y=0)

        self.image = Image.open('../assets/main.png')
        self.image = self.image.resize((1000,600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page,image=self.image)
        self.image_label.place(x=0,y=0)

        
        self.main_label_btn = Button(self.page,text='ENTER',font=fonts1,bg='firebrick3',fg='white',command=self.home_login)
        self.main_label_btn.place(x=250,y=400)


    def home_login(self):    
        self.page.destroy()
        home_obj = Login_page(root)



class Login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE")
        self.right = Frame(self.root, width=1000, height=600)
        self.right.place(x=0, y=0)

        self.image = Image.open('../assets/login1.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.right, image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0, y=0)

        self.admin_logo = Image.open('../assets/ai.png')
        self.admin_logo = self.admin_logo.resize((100, 100))
        self.admin_logo = ImageTk.PhotoImage(self.admin_logo)
        self.admin_logo_lbl = Label(self.right, image=self.admin_logo)
        self.admin_logo_lbl.place(x=150, y=100)



        self.admin__login = Label(self.right, text="Admin login")
        self.admin__login.place(x=150, y=220)
        self.admin_name = Label(self.right, text='USER ID', bg='steel blue', fg='white', font=fonts, width=9)
        self.admin_name.place(x=100, y=280)
        self.admin_name_entry = Entry(self.right, width=10, font=fonts)
        self.admin_name_entry.place(x=230, y=280)
        self.admin_pass = Label(self.right, text='PASSWORD', bg='steel blue', fg='white', font=fonts, width=9)
        self.admin_pass.place(x=100, y=320)
        self.admin_pass_entry = Entry(self.right, width=10, font=fonts)
        self.admin_pass_entry.place(x=230, y=320)

        self.admin_login_btn = Button(self.right, text='LOGIN', font=fonts, command=self.admin_login)
        self.admin_login_btn.place(x=150, y=400)

        self.left = Frame(self.root, width=1000, height=600)
        self.left.place(x=500, y=0)

        self.image = Image.open('../assets/login1.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.left, image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0, y=0)

        self.student_logo = Image.open('../assets/si.png')
        self.student_logo = self.student_logo.resize((100, 100))
        self.student_logo = ImageTk.PhotoImage(self.student_logo)
        self.student_logo_lbl = Label(self.left, image=self.student_logo)
        self.student_logo_lbl.place(x=150, y=100)

        self.student__login = Label(self.left, text="Student login")
        self.student__login.place(x=150, y=220)

        self.student_name = Label(self.left, text='USER ID', bg='steel blue', fg='white', font=fonts, width=9)
        self.student_name.place(x=100, y=280)
        self.student_name_entry = Entry(self.left, width=10, font=fonts)
        self.student_name_entry.place(x=230, y=280)

        self.student_pass = Label(self.left, text='PASSWORD', bg='steel blue', fg='white', font=fonts, width=9)
        self.student_pass.place(x=100, y=320)
        self.student_pass_entry = Entry(self.left, width=10, font=fonts)
        self.student_pass_entry.place(x=230, y=320)

        self.student_login_btn = Button(self.left, text='LOGIN', font=fonts, command=self.student_login)
        self.student_login_btn.place(x=150, y=400)
    

    def admin_login(self):
        self.b_name = self.admin_name_entry.get()
        self.b_pass = self.admin_pass_entry.get()

        mycursor.execute("SELECT * FROM admin WHERE id= %s AND password = %s", (self.b_name, self.b_pass))
        admin_data = mycursor.fetchone()

        if admin_data:
            self.right.destroy()
            self.left.destroy()
            admin_obj = Admin(root, self.b_name)
        else:
            messagebox.showerror('INVALID', 'Invalid UserID or Password')

    def student_login(self):
        self.b_name = self.student_name_entry.get()
        self.b_pass = self.student_pass_entry.get()

        mycursor.execute("SELECT * FROM Student WHERE sid= %s AND password = %s", (self.b_name, self.b_pass))
        student_data = mycursor.fetchone()

        if student_data:
            self.right.destroy()
            self.left.destroy()
            student_obj = Student(root,self.b_name)
        else:
            messagebox.showerror('INVALID', 'Invalid UserID or Password')

class Admin:
    def __init__(self, root,id):
        self.root = root
        self.id=id
        self.root.title("ADMIN DASHBOARD")
        self.right = Frame(self.root, width = 1000, height = 600)
        self.right.place(x = 0, y = 0)

        self.image = Image.open('../assets/hod2.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.right, image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0, y=0)

        self.profile_image = Image.open('../assets/stdprofile.png')
        self.profile_image = self.profile_image.resize((50, 50))
        self.profile_photo = ImageTk.PhotoImage(self.profile_image)
        self.profile_button = Button(self.right, image=self.profile_photo, bg='gray', bd=0,
                                     command=lambda: self.profile(self.id))
        self.profile_button.place(x=948, y=2)

        self.admin__approval = Label(self.right,text="Student Attendance Approval",bg='sky blue',fg='blue4',font = fonts1)
        self.admin__approval.place(x=100,y=30)
        self.student_info__btn = Button(self.right,text = 'STUDENT REQUESTS',fg='blue4',font = fonts,command=self.approval)
        self.student_info__btn.place(x = 250, y = 200)

    def approval(self):    
        self.right.destroy()
        Admin_obj = confirm(root)

    def profile(self, id):
        self.right.destroy()
        profile_obj = admin_profile_page(root, self.id)

class admin_profile_page(Login_page):
    def __init__(self, root,id):
        self.root = root
        self.id=id
        self.root.title("Profile page")
        self.page = Frame(self.root, width=1000, height=600)
        self.page.place(x=0, y=0)

        self.image = Image.open('../assets/stdbg.png')
        self.image = self.image.resize((1000,600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page,image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0,y=0)


    


        mycursor.execute("SELECT * FROM admin WHERE id= %s", (self.id,))
        admin_data = mycursor.fetchone()

        if admin_data:
            admin_user_label = Label(self.page, text=f"Userid: {admin_data[0]}", font=fonts)
            admin_user_label.place(x=400, y=310)

            admin_name_label = Label(self.page, text=f"Name: {admin_data[1]}", font=fonts)
            admin_name_label.place(x=400, y=340)

            admin_email_label = Label(self.page, text=f"Branch: {admin_data[2]}", font=fonts)
            admin_email_label.place(x=400, y=370)

            admin_phone_label = Label(self.page, text=f"Phone number: {admin_data[3]}", font=fonts)
            admin_phone_label.place(x=400, y=400)

    
class confirm:
     def __init__(self, root):
        self.root = root
        self.root.title("CONFIRM")
        self.page = Frame(self.root, width = 600, height = 400,bg='gray')
        self.page.place(x = 0, y = 0)
        self.view_image = Label(self.page,text='Uploaded Image',font=fonts,fg='black')
        self.view_image.place(x=50,y=150)
        self.accept__btn = Button(self.page,text = 'ACCEPT', font = fonts,fg='green',command=self.final)
        self.accept__btn.place(x = 350, y = 250)
        self.accept__btn = Button(self.page,text = 'DECLINE', font = fonts,fg='red',command=self.final)
        self.accept__btn.place(x = 200, y = 250)
     def final(self):    
        self.page.destroy()
        confirm_obj = page1(root)
class page1:
     def __init__(self, root):
        self.root = root
        self.root.title("page")
        self.page = Frame(self.root, width = 600, height = 400,bg='aliceblue')
        self.page.place(x = 0, y = 0)

class Student:
    def __init__(self, root,sid):
        self.root = root
        self.sid=sid
        self.root.title('STUDENT DASHBOARD')
        self.left = Frame(self.root, width = 1000, height = 600)
        self.left.place(x = 0, y = 0)
        self.image = Image.open('../assets/int1.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.left, image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0, y=0)

        self.profile_image = Image.open('../assets/stdprofile.png')
        self.profile_image = self.profile_image.resize((50, 50))
        self.profile_photo = ImageTk.PhotoImage(self.profile_image)
        self.profile_button = Button(self.left, image=self.profile_photo, bg='gray', bd=0,
                                     command=lambda: self.profile(self.sid))
        self.profile_button.place(x=948, y=2)

        self.admin__approval = Label(self.left,text="Welcome to Student Attendance Approval",bg='sky blue',fg='blue4',font = fonts1)
        self.admin__approval.place(x=100,y=30)
        self.student_info__btn = Button(self.left,text = 'MAKE REQUESTS',fg='blue4',font = fonts,command=self.make)
        self.student_info__btn.place(x = 250, y = 200)
        self.student_info__btn = Button(self.left,text = 'VIEW REQUESTS',fg='blue4',font = fonts,command=self.view)
        self.student_info__btn.place(x = 250, y = 300)

    def make(self):    
        self.left.destroy()
        req_obj = page1(root)
    def view(self):    
        self.left.destroy()
        confirm_obj = page1(root)
    def profile(self, sid):
        self.left.destroy()
        student_profile_obj = student_profile_page(root, self.sid)

class student_profile_page(Login_page):
    def __init__(self, root,sid):
        self.root = root
        self.admin_id=sid
        self.root.title("Profile page")
        self.page = Frame(self.root, width=1000, height=600)
        self.page.place(x=0, y=0)

        self.image = Image.open('../assets/stdbg.png')
        self.image = self.image.resize((1000,600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page,image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0,y=0)

        mycursor.execute("SELECT * FROM student WHERE sid= %s", (sid,))
        student_data = mycursor.fetchone()

        if student_data:
            student_user_label = Label(self.page, text=f"Userid: {student_data[0]}", font=fonts)
            student_user_label.place(x=400, y=310)

            student_name_label = Label(self.page, text=f"Name: {student_data[1]}", font=fonts)
            student_name_label.place(x=400, y=340)

            student_phone_label = Label(self.page, text=f"Phone number: {student_data[3]}", font=fonts)
            student_phone_label.place(x=400, y=370)

            student_phone_label = Label(self.page, text=f"Branch: {student_data[2]}", font=fonts)
            student_phone_label.place(x=400, y=400)

        

    


        

    



root.geometry('1000x600+250+100')
home = Home(root)
root.mainloop()