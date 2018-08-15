from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox
class Signup:
    def signup(self):

            self.bal = StringVar()
            self.uname = StringVar()
            self.creds = StringVar()

            self.f.grid_forget()
            self.sp = Frame(self.master,bg='#777777')

            self.sl1 = Label(self.sp,text='UserName : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
            self.sl1.grid(row=0,column=0,ipadx=40,pady=28)

            self.se1 = Entry(self.sp,textvariable=self.uname,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
            self.se1.grid(row=0,column=1)

            self.sl2 = Label(self.sp,text='Password : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
            self.sl2.grid(row=1,column=0)

            self.se2 = Entry(self.sp,textvariable=self.creds,show='*',bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
            self.se2.grid(row=1,column=1,padx=20)

            self.sl3 = Label(self.sp,text='Balance : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
            self.sl3.grid(row=2,column=0,ipadx=42,pady=27)

            self.se3 = Entry(self.sp,textvariable=self.bal,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
            self.se3.grid(row=2,column=1)


            self.sb2 = Button(self.sp,bg='#777777',text='SIGNUP',font=('Times','20','bold'),command=self.mksignup,fg='#123456')
            self.sb2.grid(row=3,column=1,columnspan=4)

            self.sb3 = tk.Button(self.sp,text='<<Back',width=10,bg="#777777",font=('Times','18','bold'),command=self.show_sf,fg="#000000")
            self.sb3.grid(row=3,column=0,padx=66,pady=17)
            self.sp.grid(padx=self.ws*.3,pady=self.hs*.2)

    def mksignup(self):

        uname = self.uname.get().lower()
        password  = self.creds.get()
        balance = self.bal.get()
        if uname and password and balance :
            try :
                balance = float(balance)
                db = sql.connect('localhost','bank','bank','bank')
                c = db.cursor()
                c.execute('select * from user where name="{}"'.format(uname))
                d = c.fetchone()
                if d :
                    messagebox.showerror("UserExist","User with this name is already exists.\n Please Login if you are already a user \nelse choose another name")
                else :
                    cmd = "insert into user(name,password,balance) values('{}','{}',{})".format(uname,password,balance)
                    c.execute(cmd)
                    db.commit()
                    messagebox.showinfo("Account Created","Congratulations!! Your Account is Successfully Created\nPlease LOGIN to Enjoy your services")
                    self.sp.grid_forget()
                self.f.grid(padx=self.ws*.3,pady=self.hs*.2)
            except ValueError as e :
                messagebox.showerror("ERROR","Please Enter a Valid Amount to Deposit Initial")


            except Exception as e :
                messagebox.showerror("ERROR","SOMETHING WENT WRONG\nError!!{}".format(e))

        else :
            messagebox.showerror("INPUT","Please fill-in all the Details")
