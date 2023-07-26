from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


root = Tk()
root.title("BANKING MANAGEMENT SYSTEM")
root.geometry('500x1000')
root.resizable(True,False)
root.config(bg='black')

def connect_database():
    if name_entry.get() == '' or email_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror("Error",'All fields are required')
    elif country_entry.get() == '' or number_entry.get() == '' or gender_entry.get() == '':
        messagebox.showerror("Error",'All fields are required')
    elif account_num_entry.get() == '' or account_entry.get() == '':
        messagebox.showerror("Error",'All fields are required')
    elif '@' not in email_entry.get() or 'gmail.com' not in email_entry.get():
        messagebox.showerror("Error",'Invalid email address')
    else:
        try:
            mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
            #query = 'create database bankdb'
            #mycursor.execute(query)
            mycursor = mydb.cursor()
        except:
            messagebox.showerror('Error','Connection error! Please try again')
            
        try:
            query1 = 'CREATE TABLE bankdata2 (username VARCHAR(100) NOT NULL, CONSTRAINT user_acc PRIMARY KEY(username), email VARCHAR(100) NOT NULL, password TINYTEXT NOT NULL, nationality VARCHAR(100) NOT NULL, number VARCHAR(100) NOT NULL, gender VARCHAR(100) NOT NULL, dob DATE NOT NULL, account_num VARCHAR(15) NOT NULL)'
            query2 = 'CREATE TABLE amount(name Varchar(100), account_num VARCHAR(15), balance int'
            mycursor.execute(query1)
            mycursor.execute(query2)
            
            
        except:
            mycursor.execute('use bankdb')
        
        if mycursor.fetchall():
            messagebox.showerror('Error','User already exists')
        else:
            #query = 'ALTER TABLE bankdata2 CHANGE account_num account_balance INT NOT NULL'
            #mycursor.execute(query)
            
            #query = 'ALTER TABLE bankdata2 CHANGE dob account_num INT NOT NULL'
            #mycursor.execute(query)
            query1 = 'insert into bankdata2 (username,email,password,nationality,number,gender,account_num,account_balance) values (%s,%s,%s,%s,%s,%s,%s,%s)'
            query2 = 'insert into amount (username,account_num,balance) values (%s,%s,%s)'
            mycursor.execute(query1,(name_entry.get(),email_entry.get(),password_entry.get(),country_entry.get(),number_entry.get(),gender_entry.get(),account_num_entry.get(),account_entry.get()))
            mycursor.execute(query2,(name_entry.get(),account_num_entry.get(),account_entry.get()))
            
            mydb.commit()
            mydb.close()
            clear()
            messagebox.showinfo('Success','Your account is created successfully')
            root.destroy()
            import log

def clear():
    name_entry.delete(0,END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)
    country_entry.delete(0,END)
    number_entry.delete(0,END)
    gender_entry.delete(0,END)
    account_num_entry.delete(0,END)
    account_entry.delete(0,END)    
    
    
    
def show_pass():
    if checkvar.get() == 1:
        password_entry.config(show='')
    elif checkvar.get() == 0:
        password_entry.config(show='*')

def login():
    root.destroy()
    import log     
    

    #if email_entry.get() == '' or name_entry.get() == '' or password_entry.get() == '' or confirmpassword_label_entry.get() == '':
     #   messagebox.showerror('Error','All fields are required')
    #elif password_entry.get() != confirmpassword_label_entry.get():
     #   messagebox.showerror('Error','Password mismatch')
    #elif '@' not in email_entry.get() or 'gmail.com' not in email_entry.get():
     #   messagebox.showerror('Error','Invalid email address')
    #else:
        

systemlabel = Label(root,text="BANKING MANAGEMENT SYSTEM",font=('Arial',20,'bold'),fg='firebrick2',bg='black')
systemlabel.pack(fill=X)

signuplabel = Label(root,text="CREATE YOUR ACCOUNT",font=('Arial',15,'bold'),fg='firebrick2',bg='black')
signuplabel.place(x=120,y=50)

namelabel = Label(root,text="Username:",font=('Arial',18,'bold'),fg='white',bg='black')
namelabel.place(x=50,y=120)
name_entry = Entry(root,font=('Arial',15,'bold'),width=35)
name_entry.place(x=55,y=150)

email_label = Label(root,text="Email:",font=('Arial',18,'bold'),fg='white',bg='black')
email_label.place(x=50,y=190)
email_entry = Entry(root,font=('Arial',15,'bold'),width=35)
email_entry.place(x=55,y=220)

password_var = StringVar()
checkvar = IntVar(value=0)
password_label = Label(root,text="Password:",font=('Arial',18,'bold'),fg='white',bg='black')
password_label.place(x=50,y=260)
password_entry = Entry(root,font=('Arial',15,'bold'),show='*',width=35,textvariable=password_var)
password_entry.place(x=55,y=290)

showpassword = Checkbutton(root,variable=checkvar,font=('Arial',10,'bold'),fg='white',bg='black',activebackground='black',
                           command=show_pass,activeforeground='white')
showpassword.place(x=320,y=320)
showpassword = Label(root,text="Show Password",font=('Arial',10,'bold'),fg='white',bg='black')
showpassword.place(x=340,y=323)


country_label = Label(root,text="Nationality:",font=('Arial',18,'bold'),fg='white',bg='black')
country_label.place(x=50,y=340)
country_entry = Entry(root,font=('Arial',15,'bold'),width=35)
country_entry.place(x=55,y=370)

gender_label = Label(root,text="Gender:",font=('Arial',18,'bold'),fg='white',bg='black')
gender_label.place(x=50,y=410)
gender_entry = Entry(root,font=('Arial',15,'bold'),width=35)
gender_entry.place(x=55,y=440)

#account_var = IntVar()
account_num_label = Label(root,text="Account Number:",font=('Arial',18,'bold'),
                    fg='white',bg='black')
account_num_label.place(x=50,y=480)
account_num_entry = Entry(root,font=('Arial',15,'bold'),width=35)
account_num_entry.place(x=55,y=510)

num_var = StringVar()
number_label = Label(root,text="Phone Number:",font=('Arial',18,'bold'),fg='white',bg='black')
number_label.place(x=50,y=550)
number_entry = Entry(root,font=('Arial',15,'bold'),width=35,textvariable=num_var)
number_entry.place(x=55,y=580)

account_label = Label(root,text="Account Deposit:",font=('Arial',18,'bold'),fg='white',bg='black')
account_label.place(x=50,y=620)
account_entry = Entry(root,font=('Arial',15,'bold'),width=35)
account_entry.place(x=55,y=650)

signbtn = Button(root,text='Sign Up',font=('Arial',13,'bold'),width=10,fg='white',bg='firebrick2',
                 command=connect_database,cursor='hand2',height=2)
signbtn.place(x=200,y=730)

alreadylabel = Label(root,text="Already have an account?",font=('Arial',13),fg='white',bg='black')
alreadylabel.place(x=120,y=795)

loginbtn = Button(root,text='Login',font=('Arial',13,'bold underline'),bd=0,fg='firebrick2',bg='black',cursor='hand2',activebackground='black',
                 activeforeground='firebrick2',command=login)
loginbtn.place(x=315,y=792)

root.mainloop()




    
 

    
