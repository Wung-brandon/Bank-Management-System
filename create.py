from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
#from datetime import date

# A BANK MANAGEMENT SYSTEM
root = Tk()
root.title('ZENVA BANK SYSTEM')
root.geometry('1100x800')
root.config(bg='black')

#FUNCTIONALITY PART

#FUNCTION TO CHECK BALANCE OF A USER  
def balance():
    top = Toplevel()
    top.title('Withdraw Money')
    top.geometry('500x500')
    top.config(bg='black')
    #FUNCTION TO SHOW BALANCE
    def show_balance():
        #Connect to the database
        try:
            mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
            #query = 'create database bankdb'
            #mycursor.execute(query)
            mycursor = mydb.cursor()
        
        except:
            messagebox.showerror('Error','Connection Error! Please try again',parent=top)
        #if an entry field is empty a message will show that all fields are required
        if balance_label_entry.get() == '':
            messagebox.showerror('Error','All fields are required',parent=top)
        else:
            #Use the bankdb database
            mycursor.execute('use bankdb')
            a = 'select balance from amount where account_num=%s'
            #mycursor = mydb.cursor()
            mycursor.execute(a,(balance_label_entry.get(),))
            result = mycursor.fetchone()
            if result == None:
                messagebox.showerror('Error','Account Number does not exist',parent=top)
                return
            else:
                balance = float(result[0])
                messagebox.showinfo("Balance",f'The Account Balance for Account Number {balance_label_entry.get()} is {balance} Frs',parent=top)
                balance_label_entry.delete(0,END)
        
    withdrawlabel = Label(top,text='Show Account Balance',bg='black',fg='firebrick2',font=('ariel',20,'bold'))
    withdrawlabel.pack(fill=X)
    
    balance_label = Label(top,text='Enter Account Number:',bg='black',fg='white',font=('ariel',15,'bold'))
    balance_label.place(x=57,y=180)
    
    balance_label_entry = Entry(top,font=('ariel',15,'bold'),width=30)
    balance_label_entry.place(x=60,y=220)
        
    balance_btn = Button(top,text='Show Balance',fg='white',bg='firebrick2',activebackground='firebrick2',activeforeground='white',cursor='hand2',
                         font=('ariel',15,'bold'),bd=0,width=15,height=2,command=show_balance)
    balance_btn.place(x=160,y=380)

    
    
    top.mainloop()

#FUNCTION TO SHOW ALL USERS INFORMATION
def show_all():
    try:
        mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
        #query = 'create database bankdb'
        #mycursor.execute(query)
        mycursor = mydb.cursor()
           
    except:
        messagebox.showerror('Error','Connection Error! Please try again')
            
    mycursor.execute('use bankdb')
    query = 'SELECT * FROM amount'
    mycursor.execute(query)
    show = mycursor.fetchall()
    #print(show)
    f = '%8s %33s %38s '
    details_area.insert(END,(f % ("UserName", "AccountNo", "AccountBal")))
    for records in show:
        #print(records[0])
        details_area.insert(END,f'\n\n{records[0]} \t\t\t{records[1]} \t\t\t{records[2]}Frs')
        #details_area.delete(1.0,records)
    
#FUNCTION TO CLOSE A USER ACCOUNT        
def close_account():
    top = Toplevel()
    top.title('Delete Account')
    top.geometry('500x500')
    top.config(bg='black')
    
    def delete():
        try:
            mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
            #query = 'create database bankdb'
            #mycursor.execute(query)
            mycursor = mydb.cursor()
           
        except:
            messagebox.showerror('Error','Connection Error! Please try again',parent=top)
            
        mycursor.execute('use bankdb')
        delete_mess = messagebox.askyesno('Delete','Are you sure you want to Delete this Account?',parent=top)
        if delete_mess:
            account_num = del_accountNu_entry.get()
            query1 = 'delete from bankdata2 where account_num=%s'
            query2 = 'delete from amount where account_num=%s'
            data = (account_num,)
            mycursor.execute(query1, data)
            mycursor.execute(query2, data)
            messagebox.showinfo('Success','Account Deleted Successfully',parent=top)
            del_accountNu_entry.delete(0,END)
            mydb.commit()
            mydb.close()
        else:
            pass
        
        
    deletelabel = Label(top,text='Delete Account',bg='black',fg='firebrick2',font=('ariel',20,'bold'))
    deletelabel.pack(fill=X)
    
    del_acc_label = Label(top,text='Enter Account Number:',bg='black',fg='white',font=('ariel',15,'bold'))
    del_acc_label.place(x=70,y=190)
    
    del_accountNu_entry = Entry(top,font=('ariel',15,'bold'),width=30)
    del_accountNu_entry.place(x=73,y=230)
    

    delete_btn = Button(top,text='Delete',fg='white',bg='firebrick2',activebackground='firebrick2',activeforeground='white',cursor='hand2',
                         font=('ariel',15,'bold'),bd=0,width=10,height=2,command=delete)
    delete_btn.place(x=175,y=380)
        
        
    top.mainloop() 

#FUNCTION TO UPDATE OR CHANGE DETAILS 
""" def update():
    top = Toplevel()
    top.title('Withdraw Money')
    top.geometry('500x500')
    top.config(bg='black')
    
    def update_customer():
        try:
            mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
            mycursor = mydb.cursor()
            if update_accountNu_entry.get() == '':
                messagebox.showerror('Error','All fields are required',parent=top)
                return
            else:  
                a = 'select balance from amount where account_num=%s'
                    #mycursor = mydb.cursor()
                mycursor.execute(a,(update_accountNu_entry.get(),))
                result = mycursor.fetchone()
                if result == None:
                    messagebox.showerror('Error','Account Number does not exist',parent=top)
                    return
        except:
            messagebox.showerror('Error','Connection Error! Please try again',parent=top)
    
        top.destroy()
        top1 = Toplevel()
        top1.title('Update Customer Details')
        top1.geometry('500x700')
        top1.config(bg='black')
        
        def change_details():
            try:
                mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
                mycursor = mydb.cursor()
            except:
                messagebox.showerror('Error','Connection Error! Please try again')
            
            #if 
            #else:
            mycursor.execute('use bankdb')
            query = 'select * from bankdata2'
            mycursor.execute(query)
            num = update_accountNu_entry.get()
            for i in mycursor:
                i = list(i)
                print(i[6])
                if i[6] == num:
                    pass
                    
                
                                    
            #mycursor = mydb.cursor()
        deletelabel = Label(top1,text='Change User Details',bg='black',fg='firebrick2',font=('ariel',20,'bold'))
        deletelabel.pack(fill=X)
        
        namelabel = Label(top1,text="Enter Account Number:",font=('Arial',18,'bold'),fg='white',bg='black')
        namelabel.place(x=50,y=120)
        name_entry = Entry(top1,font=('Arial',15,'bold'),width=35)
        name_entry.place(x=55,y=150)

        email_label = Label(top1,text="Change UserName:",font=('Arial',18,'bold'),fg='white',bg='black')
        email_label.place(x=50,y=190)
        email_entry = Entry(top1,font=('Arial',15,'bold'),width=35)
        email_entry.place(x=55,y=220)
        
        password_label = Label(top1,text="Change Password:",font=('Arial',18,'bold'),fg='white',bg='black')
        password_label.place(x=50,y=260)
        password_entry = Entry(top1,font=('Arial',15,'bold'),width=35)
        password_entry.place(x=55,y=290)
        
        country_label = Label(top1,text="Change Email:",font=('Arial',18,'bold'),fg='white',bg='black')
        country_label.place(x=50,y=340)
        country_entry = Entry(top1,font=('Arial',15,'bold'),width=35)
        country_entry.place(x=55,y=370)
        
        account_num_label = Label(top1,text="Change Account Number:",font=('Arial',18,'bold'),
                    fg='white',bg='black')
        account_num_label.place(x=50,y=420)
        account_num_entry = Entry(top1,font=('Arial',15,'bold'),width=35)
        account_num_entry.place(x=55,y=450)

        num_var = StringVar()
        number_label = Label(top1,text="Change Phone Number:",font=('Arial',18,'bold'),fg='white',bg='black')
        number_label.place(x=50,y=500)
        number_entry = Entry(top1,font=('Arial',15,'bold'),width=35,textvariable=num_var)
        number_entry.place(x=55,y=530)
        
        change_btn = Button(top1,text='Change',fg='white',bg='firebrick2',activebackground='firebrick2',activeforeground='white',cursor='hand2',
                         font=('ariel',15,'bold'),bd=0,width=10,height=2,command=change_details)
        change_btn.place(x=185,y=605)

        
        top1.mainloop()
        
    updatelabel = Label(top,text='Update Customer Details',bg='black',fg='firebrick2',font=('ariel',20,'bold'))
    updatelabel.pack(fill=X)
    

    update_account_no_label = Label(top,text='Enter Account Number:',bg='black',fg='white',font=('ariel',15,'bold'))
    update_account_no_label.place(x=57,y=240)
    
    global update_accountNu_entry
    update_accountNu_entry = Entry(top,font=('ariel',15,'bold'),width=30)
    update_accountNu_entry.place(x=60,y=280)
    #update_accountNu_entry.delete(0,END)
        
    withdraw_btn = Button(top,text='Update',fg='white',bg='firebrick2',activebackground='firebrick2',activeforeground='white',cursor='hand2',
                         font=('ariel',15,'bold'),bd=0,width=10,height=2,command=update_customer)
    withdraw_btn.place(x=175,y=380)

        
    top.mainloop()

 """

def withdraw_account():
    top = Toplevel()
    top.title('Withdraw Money')
    top.geometry('500x500')
    top.config(bg='black')
    
    def withdraw_money():
        try:
            mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
            #query = 'create database bankdb'
            #mycursor.execute(query)
            mycursor = mydb.cursor()
           
        
        except:
            messagebox.showerror('Error','Connection Error! Please try again',parent=top)
        
        if withdraw_amountentry.get() == '' or withdraw_accountNu_entry.get() == '':
            messagebox.showerror('Error','All fields are required',parent=top)
        else:
            mycursor.execute('use bankdb')
            a = 'select balance from amount where account_num=%s'
            #mycursor = mydb.cursor()
            mycursor.execute(a,(withdraw_accountNu_entry.get(),))
            result = mycursor.fetchone()
            if result == None:
                messagebox.showerror('Error','Account Number does not exist',parent=top)
                return
            else:
                balance = float(result[0])
                #print(balance)
                withdraw_amt = float(withdraw_amountentry.get())
                #print(withdraw_amt)
                if withdraw_amt > balance:
                    messagebox.showerror('Error','Insufficient funds to withdraw',parent=top)
                    return
                else:
                    combined_amt = balance - withdraw_amt
                    sql = 'update amount set balance=%s where account_num=%s'
                    d = (combined_amt,withdraw_accountNu_entry.get())
                    mycursor.execute(sql,d)
                    messagebox.showinfo('Success',f'{withdraw_amountentry.get()} Frs is Successfully Withdrawn from Account Number {withdraw_accountNu_entry.get()}',parent=top)
                    withdraw_amountentry.delete(0,END)
                    withdraw_accountNu_entry.delete(0,END)
                    mydb.commit()
                    mydb.close()
                
        
    withdrawlabel = Label(top,text='Withdraw Money',bg='black',fg='firebrick2',font=('ariel',20,'bold'))
    withdrawlabel.pack(fill=X)
    
    withdraw_amountlabel = Label(top,text='Enter Amount:',bg='black',fg='white',font=('ariel',15,'bold'))
    withdraw_amountlabel.place(x=55,y=140)
    #withdraw_amount_var = IntVar()
    withdraw_amountentry = Entry(top,font=('ariel',15,'bold'),width=30)#textvariable=withdraw_amount_var)
    withdraw_amountentry.place(x=60,y=180)
    

    withdraw_account_no_label = Label(top,text='Enter Account Number:',bg='black',fg='white',font=('ariel',15,'bold'))
    withdraw_account_no_label.place(x=57,y=240)
    
    withdraw_accountNu_entry = Entry(top,font=('ariel',15,'bold'),width=30)
    withdraw_accountNu_entry.place(x=60,y=280)
    
        

    withdraw_btn = Button(top,text='Withdraw',fg='white',bg='firebrick2',activebackground='firebrick2',activeforeground='white',cursor='hand2',
                         font=('ariel',15,'bold'),bd=0,width=10,height=2,command=withdraw_money)
    withdraw_btn.place(x=175,y=380)

        
        
    top.mainloop()

#FUNCTION TO DEPOSIT MONEY INTO A USER ACCOUNT AND THE GUI        
def depoAmt():
    top = Toplevel()
    top.title('Deposit Money')
    top.geometry('500x500')
    top.config(bg='black')
    
    def deposit_money():
        try:
            mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
            #query = 'create database bankdb'
            #mycursor.execute(query)
            mycursor = mydb.cursor()
           
        
        except:
            messagebox.showerror('Error','Sorry Amount not deposited! Please try again',parent=top)
        
        if amountentry.get() == '' or accountNu_entry.get() == '':
            messagebox.showerror('Error','All fields are required',parent=top)
        else:
            mycursor.execute('use bankdb')
            a = 'select balance from amount where account_num=%s'
            #mycursor = mydb.cursor()
            mycursor.execute(a,(accountNu_entry.get(),))
            result = mycursor.fetchone()
            if result == None:
                messagebox.showerror('Error','Account Number does not exist',parent=top)
                return
            else:
                balance = float(result[0])
                deposit_amt = float(amountentry.get())
                combined_amt = balance + deposit_amt
                sql = 'update amount set balance=%s where account_num=%s'
                d = (combined_amt,accountNu_entry.get())
                mycursor.execute(sql,d)
                messagebox.showinfo('Success',f'{amountentry.get()} Frs deposited Successfully into Account Number {accountNu_entry.get()}',parent=top)
                amountentry.delete(0,END)
                accountNu_entry.delete(0,END)
                mydb.commit()
                mydb.close()
            
        
    depolabel = Label(top,text='Deposit Money',bg='black',fg='firebrick2',font=('ariel',20,'bold'))
    depolabel.pack(fill=X)
    
    amountlabel = Label(top,text='Enter Amount:',bg='black',fg='white',font=('ariel',15,'bold'))
    amountlabel.place(x=55,y=140)
    
    amountentry = Entry(top,font=('ariel',15,'bold'),width=30)
    amountentry.place(x=60,y=180)
    
   
    account_no_label = Label(top,text='Enter Account Number:',bg='black',fg='white',font=('ariel',15,'bold'))
    account_no_label.place(x=57,y=240)
    
    accountNu_entry = Entry(top,font=('ariel',15,'bold'),width=30)
    accountNu_entry.place(x=60,y=280)

    deposit_btn = Button(top,text='Deposit',fg='white',bg='firebrick2',activebackground='firebrick2',activeforeground='white',cursor='hand2',
                         font=('ariel',15,'bold'),bd=0,width=10,height=2,command=deposit_money)
    deposit_btn.place(x=175,y=380)
  
    top.mainloop()

#FUNCTION TO EXIT 
def exit_page():
    exit_account = messagebox.askyesno('Exit',"Are you sure you want to exit?")
    if exit_account:
        root.destroy()
    else:
        pass

#FUNCTION TO LOGOUT FROM ACCOUNT
def logout():
    
    log = messagebox.askyesno("logout",'Are you sure you want to logout?')
    if log:
        messagebox.showinfo("Success",'Logout successfully')
        root.destroy()
        import log
    else:
       pass
    
def show_records():
    try:
        mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
        #query = 'create database bankdb'
        #mycursor.execute(query)
        mycursor = mydb.cursor()
        
    except:
        messagebox.showerror('Error','Connection Error! Please try again')
    
    #option_combo.delete(0,END)
    options = option_combo.get()
    if options == 'Account Number':
        #search_entry.delete(0,END)
        value = search_entry.get()
        query = 'SELECT * FROM bankdata2 where account_num=%s'
        data = (value,)
        mycursor = mydb.cursor()
        mycursor.execute(query,data)
        result = mycursor.fetchone()
        #print(result)
        #print(result[0])
        
        
        if result == None:
            messagebox.showerror('Error','Record does not Exist')
        else:
            f = '%8s %20s %20s %24s %24s '
            details_area.insert(END,(f % ("UserName", "Nationality", "Gender", "AccountNo", "AccountBal")))
            details_area.insert(END,f'\n\n{result[0]}\t\t{result[3]}\t\t{result[5]}\t\t{result[6]}\t\t{result[7]}Frs')

    elif options == 'Name':
        value = search_entry.get()
        query = 'SELECT * FROM bankdata2 where username=%s'
        data = (value,)
        mycursor = mydb.cursor()
        mycursor.execute(query,data)
        result = mycursor.fetchone()
        #print(result)
        if result == None:
            messagebox.showerror('Error','Record does not Exist')
        else:
            f = '%8s %20s %20s %24s %24s '
            details_area.insert(END,(f % ("UserName", "Nationality", "Gender", "AccountNo", "AccountBal")))
            details_area.insert(END,f'\n\n{result[0]}\t\t{result[3]}\t\t{result[5]}\t\t{result[6]}\t\t{result[7]}Frs')
        
    elif options == 'Balance':
        value = search_entry.get()
        query = 'SELECT * FROM bankdata2 where account_balance=%s'
        data = (value,)
        mycursor = mydb.cursor()
        mycursor.execute(query,data)
        result = mycursor.fetchone()
        print(result)
        
        if result == None:
            messagebox.showerror('Error','Record does not Exist')
        else:
            f = '%8s %20s %20s %24s %24s '
            details_area.insert(END,(f % ("UserName", "Nationality", "Gender", "AccountNo", "AccountBal")))
            details_area.insert(END,f'\n\n{result[0]}\t\t{result[3]}\t\t{result[5]}\t\t{result[6]}\t\t{result[7]}Frs')
    else:
        messagebox.showerror("Error",'Invalid Option')
    
def clear():
    details_area.delete(1.0,END)
    search_entry.delete(0,END)
    
def toggle_menu():
    
    def collapse_toggle_menu():
        toggle_menu_frame.destroy()
        toggle_btn.config(text='=',font=100)
        toggle_btn.config(command=toggle_menu)
         
         
    toggle_menu_frame = Frame(root,bg='firebrick2')
    window_height = root.winfo_height()
    toggle_menu_frame.place(x=0,y=100,height=window_height,width=240)
    
    toggle_btn.config(text='X',font=30)
    toggle_btn.config(command=collapse_toggle_menu)
    
    #customer_btn = Button(toggle_menu_frame,text=' Update Details',font=('ariel',18,'bold'),fg='white',bd=0,bg='firebrick2',activebackground='firebrick2',
                         # activeforeground='white',cursor='hand2',command=update)
    #customer_btn.place(x=6,y=60)
    
    withdraw_btn = Button(toggle_menu_frame,text='Money Withdraw',font=('ariel',18,'bold'),fg='white',bd=0,bg='firebrick2',activebackground='firebrick2',
                          activeforeground='white',cursor='hand2',command=withdraw_account)
    withdraw_btn.place(x=10,y=160)
    
    deposit_btn = Button(toggle_menu_frame,text='Money Deposit',font=('ariel',18,'bold'),fg='white',bd=0,bg='firebrick2',activebackground='firebrick2',
                          activeforeground='white',cursor='hand2',command=depoAmt)
    deposit_btn.place(x=10,y=260)
    
    balance_btn = Button(toggle_menu_frame,text='Balance Equiry',font=('ariel',18,'bold'),fg='white',bd=0,bg='firebrick2',activebackground='firebrick2',
                          activeforeground='white',cursor='hand2',command=balance)
    balance_btn.place(x=10,y=360)
    
    close_account_btn = Button(toggle_menu_frame,text='Close Account',font=('ariel',18,'bold'),fg='white',bd=0,bg='firebrick2',activebackground='firebrick2',
                          activeforeground='white',cursor='hand2',command=close_account)
    close_account_btn.place(x=10,y=460)
    
    exit_btn = Button(toggle_menu_frame,text='Exit',font=('ariel',18,'bold'),fg='white',bd=0,bg='firebrick2',activebackground='firebrick2',
                          activeforeground='white',cursor='hand2',command=exit_page)
    exit_btn.place(x=10,y=560)
    
    logout_btn = Button(toggle_menu_frame,text='Logout ',font=('ariel',15),fg='black',bd=0,bg='firebrick2',activebackground='firebrick2',
                          activeforeground='black',cursor='hand2',command=logout)
    logout_btn.place(x=10,y=630)
    

header_frame = Frame(root,bg='firebrick2',highlightbackground='white',highlightthickness=1)

toggle_btn = Button(header_frame,text='=',fg='white',bg='firebrick2',font=100,activebackground='firebrick2',bd=0,activeforeground='white',cursor='hand2',
                    command=toggle_menu)
toggle_btn.pack(side=LEFT)
welcomelabel = Label(header_frame,text='Welcome To Zenva Bank',fg='white',bg="firebrick2",font=('ariel',30,'bold'))
welcomelabel.place(x=310,y=20)


show_allbtn = Button(root,text='Show All',bg='black',font=('ariel',15,'bold'),fg='white',cursor='hand2',activebackground='firebrick2',
                  activeforeground='white',bd=0,command=show_all)
show_allbtn.place(x=960,y=115)

search_btn = Button(root,text='Search',bg='black',font=('ariel',15,'bold'),fg='white',cursor='hand2',activebackground='firebrick2',
                  activeforeground='white',bd=0,command=show_records)
search_btn.place(x=510,y=115)

clear_btn = Button(root,text='Clear',bg='black',font=('ariel',18,'bold'),fg='firebrick2',cursor='hand2',activebackground='black',
                  activeforeground='white',bd=0,command=clear)
clear_btn.place(x=900,y=750)

search_entry = Entry(root,font=('ariel',15,'bold'),width=30)
search_entry.place(x=600,y=120)

searchby_label = Label(root,text='Search By',bg='black',font=('ariel',15,'bold'),fg='firebrick2')
searchby_label.place(x=250,y=120)

combo_var = StringVar()
option_combo = ttk.Combobox(root,width=20,textvariable=combo_var,state='readonly')
option_combo.place(x=360,y=125)
option_combo['values'] = ('Account Number','Balance','Name')
option_combo.set('Account Number')

details_area = Text(root,font='ariel',width=75,height=25,bg='white')
details_area.place(x=250,y=170)

header_frame.pack(side=TOP,fill=X)
header_frame.pack_propagate(False)
header_frame.configure(height=100)

root.mainloop()