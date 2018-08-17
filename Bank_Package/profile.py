from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox


class PROFILE():
    
    def show_m(self):
        self.profframe.grid_forget()
        self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)


    def show_profile(self):

        self.menu.grid_forget()
        self.profframe = tk.Frame(self.master,bg="gray")
        try :
            db = sql.connect('localhost','bank','bank','bank')
            c = db.cursor()
            c.execute('select * from user where name="{}"'.format(self.user))
            data = c.fetchone()
            self.udname = StringVar()
            self.udpass = StringVar()
            self.udacc = StringVar()
            self.udbal = StringVar()

            self.udname.set(data[1])
            self.udpass.set(data[2])
            self.udacc.set(data[0])
            self.udbal.set(data[3])



        except Exception as e :
            messagebox.showerror("DataBASE Connectivity","!!Error!!Database Connection!!{}".format(e))
            exit(0)

        self.p_l1 = Label(self.profframe,text='Account No:{}'.format(self.udacc.get()),bg="gray",font=('Times','18','bold'),fg="#ffffff")
        self.p_l1.grid(row=0,column=0,columnspan=2,padx=64)

        self.p_l2 = Label(self.profframe,text='User Name:{}'.format(self.udname.get()),bg="gray",font=('Times','18','bold'),fg="#ffffff")
        self.p_l2.grid(row=1,column=0,columnspan=2,padx=64)

        self.p_l3 = Label(self.profframe,text='Balance:{}'.format(self.udbal.get()),bg="gray",font=('Times','18','bold'),fg="#ffffff")
        self.p_l3.grid(row=2,column=0,columnspan=2,padx=64)


        self.p_b1 = tk.Button(self.profframe,text='Change Name',bg="#777777",font=('Times','20','bold'),width=13,command=self.updatename,fg="#003b8b")
        self.p_b1.grid(row=3,column=0,padx=64,pady=19)

        self.p_b2 = tk.Button(self.profframe,text='Change Password',bg="#777777",font=('Times','20','bold'),width=13,command=self.change_password,fg="#003b8b")
        self.p_b2.grid(row=4,column=0,padx=64,pady=10)

        self.p_b3 = tk.Button(self.profframe,text='<<Back',width=10,bg="#777777",font=('Times','18','bold'),command=self.show_m,fg="#000000")
        self.p_b3.grid(row=5,column=1,padx=64,pady=18)

        self.profframe.grid(padx=self.ws*.3,pady=self.hs*.2)


    def update_password(self):
        old = self.Old_Password.get()
        new = self.New_Password.get()
        self.Old_Password.set('')
        self.New_Password.set('')
        if old and new :
            try :
                db = sql.connect('localhost','bank','bank','bank')
                c = db.cursor()
                c.execute('select * from user where name="{}"'.format(self.user))
                data = c.fetchone()
                if old != data[2] :
                    messagebox.showerror("!!Invalid Error!!","!!Error!!\nOld Password does not\nPlease Try Again")
                elif old == new :
                    messagebox.showerror("!!Invalid Error!!","!!Error!!\nPassword is Same as Old Password\nPlease Choose Different Password")
                elif old == data[2] :
                    c.execute('update user set password="{}" where name="{}"'.format(new,self.user))
                    db.commit()
                    messagebox.showinfo("!!Sucess!!","Your Password is sucessfully updated")
                    self.show_m3()

                else :
                    messagebox.showerror("!!Invalid Error!!","!!Error!!\nSomething Went Wrong\nTry Again")



            except Exception as e :
                messagebox.showerror("!!DataBase Error!!","Error!!{}".format(e))

        else :
            messagebox.showerror("Input Error","Error!!Please Fill Passwords Properly")



    def change_password(self):
        self.profframe.grid_forget()
        self.passupdate = tk.Frame(self.master,bg="gray")
        self.up_opass_lbl1 = Label(self.passupdate,text='Welcome to Password Update Service',bg="gray",font=('Times','20','bold'),fg="#abcdef")
        self.up_opass_lbl1.grid(row=0,column=0,columnspan=3,padx=20,pady=20)

        self.up_opass_lbl = Label(self.passupdate,text='Old password:',bg="gray",font=('Times','25','bold'),fg="#FFFFFF")
        self.up_opass_lbl.grid(row=1,column=0,padx=21,pady=22)

        self.Old_Password  = StringVar()
        self.New_Password = StringVar()
        self.old_password = Entry(self.passupdate,textvariable=self.Old_Password,bg='#123456',show="*",width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.old_password.grid(row=1,column=1,padx=31,pady=22)

        self.up_npass_lbl = Label(self.passupdate,text='New password:',bg="gray",font=('Times','25','bold'),fg="#FFFFFF")
        self.up_npass_lbl.grid(row=2,column=0,padx=30,pady=20)

        self.new_password = Entry(self.passupdate,bg='#123456',textvariable=self.New_Password,width=20,show="*",font=('Times','20','bold'),fg='#FFFFFF')
        self.new_password.grid(row=2,column=1,padx=30,pady=21)

        self.pass_b1=tk.Button(self.passupdate,text="Update",width=10,bg="gray",font=('Times','20','bold'),command=self.update_password,fg="#000000")
        self.pass_b1.grid(row=3,column=1,columnspan=2,padx=30,pady=22)

        self.pass_b2=tk.Button( self.passupdate,text="<<Back",bg="gray",font=('Times','18','bold'),command=self.show_m3,fg="#000000")
        self.pass_b2.grid(row=3,column=0,pady=15,padx=30)

        self.passupdate.grid(padx=self.ws*.3,pady=self.hs*.2)

    def show_m3(self):

        self.passupdate.grid_forget()
        self.profframe.grid(padx=self.ws*.3,pady=self.hs*.2)


    def change_name(self):
        try :
            if self.up_name.get() :
                name = self.up_name.get()
                db = sql.connect('localhost','bank','bank','bank')
                c  = db.cursor()
                c.execute('update user set name="{}" where name="{}"'.format(name,self.user))
                db.commit()
                c.close()
                db.close()
                messagebox.showinfo("!!Sucess!!","Updated User Name Sucessfully")
                self.nameupdate.grid_forget()
                self.user = name
                self.udname.set(name)
                self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)

            else :
                messagebox.showerror("NameError","Error!!Please Enter new username")
        except Exception as e :
            messagebox.showerror("Error!!",e)

    def updatename(self):

        self.profframe.grid_forget()

        self.nameupdate = tk.Frame(self.master,bg="gray")

        self.up_name_lbl1 = Label(self.nameupdate,text="Welcome to Update Name Facility",bg="gray",font=('Times','20','bold'),fg="#ffffff")
        self.up_name_lbl1.grid(row=0,column=0,columnspan=2,pady=18)

        self.up_name_lbl2 = Label(self.nameupdate,text="Your Current Name is : {}".format(self.user),bg="gray",font=('Times','20','bold'),fg="#ffffff")
        self.up_name_lbl2.grid(row=1,column=0,columnspan=2,pady=20)

        self.up_name_lbl = Label( self.nameupdate,text='New UserName:',bg="gray",font=('Times','20','bold'),fg="#ffffff")
        self.up_name_lbl.grid(row=2,column=0,padx=30)

        self.up_name = Entry( self.nameupdate,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.up_name.grid(row=2,column=1,padx=40)

        self.name_b1=tk.Button( self.nameupdate,text="Update",bg="gray",width=14,font=('Times','20','bold'),command=self.change_name,fg="#000000")
        self.name_b1.grid(row=3,column=1,padx=67,pady=10,columnspan=2)
        self.name_b2=tk.Button( self.nameupdate,text="<<Back",bg="gray",font=('Times','20','bold'),command=self.show_m1,fg="#000000")
        self.name_b2.grid(row=4,column=0,pady=15,padx=10)

        self.nameupdate.grid(padx=self.ws*.3,pady=self.hs*.2)

    def show_m1(self):
        self.nameupdate.grid_forget()
        self.profframe.grid(padx=self.ws*.3,pady=self.hs*.2)

