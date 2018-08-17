from tkinter import *
import tkinter as tk
import pymysql as sql
from tkinter import messagebox



class DEBIT():
    
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


