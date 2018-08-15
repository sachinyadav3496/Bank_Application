from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox
from signup import Signup

class Bank(Signup):

    def __init__(self,master):
        Signup.__init__(self)
        self.master = master()
        self.master.title('BANK Application')
        self.ws=self.master.winfo_screenwidth()
        self.hs=self.master.winfo_screenheight()
        self.master.wm_minsize(self.ws,self.hs)
        self.master.configure(background='#666666')
        self.menu_forget = False
        self.upd_pass=False
        self.upd_name=False

    def run(self):
        self.main_frame()

    def menu(self):

        self.menu = tk.Frame(self.master,bg="#777777")

        self.m_l1 = Label(self.menu,text='Welcome {}'.format(self.user),bg="#777777",font=('Times','20','bold'),fg="#ffffff")
        self.m_l1.grid(row=0,column=0,padx=60,pady=10)

        self.m_b1 = tk.Button(self.menu,text='DEBIT',bg="#777777",width=10,font=('Times','20','bold'),command=self.debframe,fg="#003b8b")
        self.m_b1.grid(row=1,column=0,padx=60,pady=10)

        self.m_b2 = tk.Button(self.menu,text='CREDIT',width=10,bg="#777777",font=('Times','20','bold'),command=self.credit_Balance,fg="#003b8b")
        self.m_b2.grid(row=2,column=0,padx=76,pady=20)

        self.m_b3 = tk.Button(self.menu,text='Profile',bd=0,bg="#777777",font=('Times','20','bold'),command=self.show_profile,fg="#aadcba")
        self.m_b3.grid(row=0,column=1,padx=76,pady=25)


        self.m_b4 = tk.Button(self.menu,text='LOGOUT',width=10,bg="#777777",font=('Times','18','bold'),command=self.show_f,fg="#ff0000")

        self.m_b4.grid(row=3,column=1,padx=76,pady=15)
        self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)

    def credit_Balance(self):

        self.menu.grid_forget()

        self.credframe = tk.Frame(self.master,bg="#777777")

        self.up_amnt_lbl1 = Label(self.credframe,text='Welcome {} to Credit Services'.format(self.user),bg="#777777",font=('Times','20','bold'),fg="#ffffff")
        self.up_amnt_lbl1.grid(row=0,column=0,columnspan=2,pady=10)

        self.up_amnt_lbl2 = Label(self.credframe,text='Enter amount to credit',bg="#777777",font=('Times','26','bold'),fg="#ffffff")
        self.up_amnt_lbl2.grid(row=1,column=0,columnspan=2,pady=10)

        self.up_amnt_lbl = Label(self.credframe,text='Amount',bg="#777777",font=('Times','25','bold'),fg="#ffffff")
        self.up_amnt_lbl.grid(row=2,column=0,pady=10)

        self.up_amnt = Entry(self.credframe,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.up_amnt.grid(row=2,column=1,pady=10,padx=30)

        self.up_amnt_btn = tk.Button(self.credframe,text='update balance',bg="#777777",font=('Times','20','bold'),width=15,command=self.credit,fg="#000000")
        self.up_amnt_btn.grid(row=3,column=1,pady=13,padx=72)

        self.up_amnt_btn1 = tk.Button(self.credframe,text='<<Back',bg="#777777",font=('Times','18','bold'),command=self.show_m5,fg="#000000",width=10)
        self.up_amnt_btn1.grid(row=4,column=0,pady=16,padx=40)

        self.credframe.grid(padx=self.ws*.3,pady=self.hs*.2)

    def credit(self):
        if self.up_amnt.get():
            try :
                amount = float(self.up_amnt.get())
                amnt=self.up_amnt.get()
                db = sql.connect('localhost','bank','bank','bank')
                c = db.cursor()
                c.execute('select balance from user where name="{}"'.format(self.user))
                bal = c.fetchone()[0]
                cmd="update user SET balance=balance+{} where name='{}'".format(amnt,self.user)
                c.execute(cmd)
                db.commit()
                c.close()
                db.close()
                s='Sucessfully {} rs credited to the account associated with {}.\nYour Updated Balance is now {}.'.format(amount,self.user,amount+bal)
                messagebox.showinfo("CREDIT",s)
                self.credframe.grid_forget()
                self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)

            except ValueError as e :
                messagebox.showerror("!!Input Error!!","Please Enter a Valid Amount")
        else :
            messagebox.showerror("!!Input Error!!","Please Enter Some Amount to Credit")

    def show_m5(self):
        self.credframe.grid_forget()
        self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)


    def debframe(self):

        self.menu.grid_forget()
        self.debit_Balance = tk.Frame(self.master,bg="#777777")

        self.up_amnt_lbl1 = Label(self.debit_Balance,text='Welcome {} to Debit Services'.format(self.user),font=('Times','20','bold'),fg="#ffffff",bg='#777777')
        self.up_amnt_lbl1.grid(row=0,column=0,columnspan=2,pady=10,padx=30)

        self.up_amnt_lbl = Label(self.debit_Balance,text='Enter amount to debit ',font=('Times','23','bold'),fg="#ffffff",bg='#777777')
        self.up_amnt_lbl.grid(row=1,column=0,columnspan=2,pady=10,padx=30)

        self.up_amnt_lbl2 = Label(self.debit_Balance,text='Amount',font=('Times','20','bold'),fg="#ffffff",bg='#777777')
        self.up_amnt_lbl2.grid(row=2,column=0,pady=10,padx=30)


        self.up_amnt = Entry(self.debit_Balance,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.up_amnt.grid(row=2,column=1,pady=12,padx=55)

        self.up_amnt_btn = tk.Button(self.debit_Balance,text='update',bg="#777777",font=('Times','20','bold'),command=self.update_balance,fg="#000000",width=12)
        self.up_amnt_btn.grid(row=3,column=1,pady=16)

        self.up_amnt_btn1 = tk.Button(self.debit_Balance,text='<<Back',bg="#777777",font=('Times','18','bold'),command=self.show_m4,fg="#000000",width=10)
        self.up_amnt_btn1.grid(row=4,column=0,pady=17,padx=40)


        self.debit_Balance.grid(padx=self.ws*.3,pady=self.hs*.2)

    def show_m4(self):
        self.debit_Balance.grid_forget()
        self.menu.grid(padx=self.ws*.3,pady=self.hs*.2)



    def update_balance(self):
        if self.up_amnt.get() :
            try :
                amnt=float(self.up_amnt.get())
                db = sql.connect('localhost','bank','bank','bank')
                c = db.cursor()
                c.execute('select balance from user where name="{}"'.format(self.user))
                bal = c.fetchone()[0]
                if bal :
                    if amnt <= bal:

                        cmd="update user SET balance=balance-{} where name='{}'".format(amnt,self.user)
                        c.execute(cmd)
                        db.commit()
                        s='!!DEBITED SUCESSFULLY!! \n {}rs debited from Your Account\nYour Updated Balance is now {}.'.format(amnt,bal-amnt)
                        messagebox.showinfo("!!Sucess!!",s)

                    else:

                        s='\nInsufficient account balance\nyou only have {}rs in your account'.format(bal)
                        messagebox.showinfo("!!DEBIT ERROR!!",s)


                else :
                    messagebox.showerror("!!UNKOWN ERROR!!","DATABASE LOOKUP Error \nSomething WEnt Wrong")
            except ValueError as e :
                messagebox.showerror("!!Value Error!!","!!ERROR!!Enter Vaid Amount to Debit\n")

            except Exception as error :
                messagebox.showerror("!!DataBase Connectivity Error!!","!!ERROR!!{}".format(error))

        else :
            messagebox.showerror("!!Input Error!!","Please Enter Amount to Debit")


    def show_f(self):
        self.menu.grid_forget()
        self.menu_forget = True
        self.f.grid(padx=self.ws*.3,pady=self.hs*.2)

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




root = Bank(Tk)
root.run()

mainloop()
