from tkinter import Tk,Frame,Label,Entry,Button,messagebox
from PIL import Image,ImageTk

fonts = ('Courier New', 13, 'bold')
fonts1 = ('Courier New', 17, 'bold')
admin = 'user'
password = '123'
student = 'leo'
password1 = '2022'


root = Tk()

class Home:
    def __init__(self,root):
        self.root=root
        self.root.title("HOME")
        self.page = Frame(self.root,width=600,height=400)
        self.page.place(x=0,y=0)

        self.image = Image.open('../assets/pic3.png')
        self.image = self.image.resize((600,400))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page,image=self.image)
        self.image_label.place(x=0,y=0)

        self.main_label = Label(self.page , text = 'WELCOME', font = fonts1)
        self.main_label.place(x=250,y=50)
        self.main_label2 = Label(self.page , text = "APPROVAL OF PERMISSION FOR STUDENT ATTENDANCE" , font = fonts)
        self.main_label2.place(x=70,y=150)
        self.main_label_btn = Button(self.page,text='ENTER',font=fonts1,command=self.home_login)
        self.main_label_btn.place(x=200,y=290)


    def home_login(self):    
        self.page.destroy()
        home_obj = Main(root)



class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE")
        self.right =Frame(self.root,width = 600, height = 400,bg='teal')
        self.right.place(x = 0, y = 0 )

        
        self.admin_logo = Image.open('../assets/ai.png')
        self.admin_logo = self.admin_logo.resize((100, 100))

        self.admin_logo = ImageTk.PhotoImage(self.admin_logo)

        self.admin_logo_lbl = Label(self.right, image = self.admin_logo)
        self.admin_logo_lbl.place(x = 100, y= 30)



       
        self.admin__login = Label(self.right,text="Admin login")
        self.admin__login.place(x=100,y=125) 
        self.admin_name = Label(self.right, text = 'USER ID', bg = 'olive', fg ='white', font = fonts,width = 9)
        self.admin_name.place(x = 50, y = 170)
        self.admin_name_entry = Entry(self.right, width = 10, font = fonts)
        self.admin_name_entry.place(x = 150, y = 170)
        self.admin_pass = Label(self.right, text = 'PASSWORD', bg = 'olive', fg ='white', font = fonts, width = 9)
        self.admin_pass.place(x = 50, y = 200)
        self.admin_pass_entry = Entry(self.right, width = 10, font = fonts)
        self.admin_pass_entry.place(x = 150, y = 200)

        self.admin_login_btn = Button(self.right, text = 'LOGIN', font = fonts, command = self.admin_login)
        self.admin_login_btn.place(x = 100, y = 250)


        self.left =Frame(self.root, width = 600, height = 400,bg='teal')
        self.left.place(x = 250, y = 0 )
        
        
      
        self.student_logo = Image.open('../assets/si.png')
        self.student_logo = self.student_logo.resize((100, 100))

        self.student_logo = ImageTk.PhotoImage(self.student_logo)

        self.student_logo_lbl = Label(self.left, image = self.student_logo)
        self.student_logo_lbl.place(x = 100, y= 30)



        self.student__login = Label(self.left,text="Student login")
        self.student__login.place(x=100,y=125) 


        self.student_name = Label(self.left, text = 'USER ID', bg = 'olive', fg ='white', font = fonts,width=9)
        self.student_name.place(x = 50, y = 170)
        self.student_name_entry = Entry(self.left, width = 10, font = fonts)
        self.student_name_entry.place(x = 150, y = 170)

        self.student_pass = Label(self.left, text = 'PASSWORD', bg = 'olive', fg ='white', font = fonts, width = 9)
        self.student_pass.place(x = 50, y = 200)
        self.student_pass_entry = Entry(self.left, width = 10, font = fonts)
        self.student_pass_entry.place(x = 150, y = 200)

        self.student_login_btn = Button(self.left, text = 'LOGIN', font = fonts,command = self.student_login)
        self.student_login_btn.place(x = 100, y = 250)
    

    def admin_login(self):
        global admin, password
        self.a_name = self.admin_name_entry.get()
        self.a_pass = self.admin_pass_entry.get()
        if self.a_name == admin:
            if self.a_pass == password:
                self.right.destroy()
                self.left.destroy()
                admin_obj = Admin(root)
            else:
                messagebox.showerror('INVALID','INCORRECT PASSWORD')
        else:
                messagebox.showerror('INVALID','USER ID INVALID')



    def student_login(self):
        global student, password1
        self.b_name = self.student_name_entry.get()
        self.b_pass = self.student_pass_entry.get()
        if self.b_name == student:
            if self.b_pass == password1:
                self.right.destroy()
                self.left.destroy()
                student_obj = Student(root)
            else:
                messagebox.showerror('INVALID','INCORRECT PASSWORD')
        else:
                messagebox.showerror('INVALID','USER ID INVALID')
      

class Admin:
    def __init__(self, root):
        self.root = root
        self.root.title("ADMIN DASHBOARD")
        self.right = Frame(self.root, width = 600, height = 400,bg='lavender')
        self.right.place(x = 0, y = 0)

        self.admin__approval = Label(self.right,text="Student Attendance Approval",bg='lavender',fg='black',font = fonts1)
        self.admin__approval.place(x=100,y=30)
        self.student_info__btn = Button(self.right,text = 'STUDENT REQUESTS', font = fonts,command=self.approval)
        self.student_info__btn.place(x = 200, y = 100)

    def approval(self):    
        self.right.destroy()
        Admin_obj = confirm(root)
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
    def __init__(self, root):
        self.root = root
        self.root.title('STUDENT DASHBOARD')
        self.left = Frame(self.root, width = 600, height = 400,bg='gray')
        self.left.place(x = 0, y = 0)

        self.student__login = Label(self.left,text="ATTENDANCE APPROVAL PORTAL",fg='blueviolet',bg='gray',font=fonts1)
        self.student__login.place(x=130,y=40)

        self.image_upload = Label(self.left, text = 'Upload Image',fg ='black', font = fonts)
        self.image_upload.place(x = 100, y = 140)
        self.image_upload_entry = Entry(self.left,width=20, font = fonts)
        self.image_upload_entry.place(x = 300, y = 140)
        

root.geometry('600x400+550+200')
home = Home(root)
root.mainloop()