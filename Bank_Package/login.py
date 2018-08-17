from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox
from signup import Signup

class Login():
    def run(self):
        self.main_frame()

    
    def main_frame(self):

        self.f = Frame(self.master,bg='#777777')
        Bank.username = StringVar()
        Bank.password = StringVar()

        self.l0 = Label(self.f,text="Welcome To PYTHON Banking Services",bg='#777777',font=('Times','20','bold'),fg='#abcdef')
        self.l0.grid(row=0,column=0,columnspan=3)

        self.l1 = Label(self.f,text='UserName : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
        self.l1.grid(row=1,column=0,ipadx=40,pady=30)

        self.e1 = Entry(self.f,textvariable=Bank.username,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.e1.grid(row=1,column=1)

        self.l2 = Label(self.f,text='Password : ',bg='#777777',font=('Times','30','bold'),fg='#123456')
        self.l2.grid(row=2,column=0)



        self.e2 = Entry(self.f,textvariable=Bank.password,show='*',bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.e2.grid(row=2,column=1,padx=20)

        self.b3 = Button(self.f,bg='#777777',text='forget password ?',font=('Times','12','bold'),command=self.fpass,fg='red',width=30,bd=0)
        self.b3.grid(row=3,column=1)

        self.b1 = Button(self.f,bg='#777777',text='LOGIN',font=('Times','20','bold'),command=self.login,fg='#123456')
        self.b1.grid(row=4,column=0,columnspan=4,padx=19,pady=31)

        self.b2 = Button(self.f,bg='#777777',text='SIGNUP',font=('Times','20','bold'),command=self.signup,fg='#123456')
        self.b2.grid(row=4,column=1,columnspan=4)
        self.f.grid(padx=self.ws*.3,pady=self.hs*.2)

    def fpass(self):
        messagebox.showinfo("PRIVACY","Due to your privacy reason you have to meet in person to nearest branch with all documents to update your password.")

    def show_sf(self):
            self.sp.grid_forget()
            self.menu_forget = True
            self.f.grid(padx=self.ws*.3,pady=self.hs*.2)




    def login(self,event=None):

        UserName = self.e1.get().lower()
        Password = self.e2.get()


        try :

            db = sql.connect('localhost','bank','bank','bank')
            c = db.cursor()
            cmd = "select * from user where name = '{}'".format(UserName)

            c.execute(cmd)
            data = c.fetchone()
            self.password.set('')
            if data :
                if Password == data[2] :

                    self.f.grid_forget()
                    self.user = UserName
                    if self.menu_forget :
                        self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)

                    else :
                        self.menu()

                else :

                    messagebox.showerror("Error","!!Invalid Password")

            else :

                messagebox.showerror("Error","!!No such user exists")
                self.username.set('')

        except Exception as e :

            messagebox.showerror("Error","!!Check Data BAse Connectivity {}".format(e))





