from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

root = Tk()
root.title("BANKING MANAGEMENT SYSTEM")
root.geometry('500x700')
root.resizable(True,False)
root.config(bg='black')

def clear():
    name_entry.delete(0,END)
    password_entry.delete(0,END)
    
def log_database():
    if name_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('error','All fields are Required')
    else:
        try:
            mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
            mycursor = mydb.cursor()
        except:
            messagebox.showerror('Error','Connection error! Please try again')
            return
    
    query = 'use bankdb'
    mycursor.execute(query)
    query = 'select * from bankdata2 where password=%s and username=%s'
    mycursor.execute(query,(password_entry.get(), name_entry.get()))
    row = mycursor.fetchone()
    if row == None:
        messagebox.showerror('Error','Invalid user or password')
    else:
        clear()
        messagebox.showerror('Success','Login successful')
        root.destroy()
        import create
    

def show_pass():
    if checkvar.get() == 1:
        password_entry.config(show='')
    elif checkvar.get() == 0:
        password_entry.config(show='*')

def sign_up():
    root.destroy()
    import signup

def forgot():
    top = Toplevel()
    top.title("Change Password")
    top.geometry('400x600')
    top.config(bg='black')
    
    reset = Label(top,text="RESET PASSWORD",font=('ariel',15,'bold'),bg='black',fg='white')
    reset.pack()
    def submit():
        if userlabel_entry.get() == '' or newpasswordlabel_entry.get() == '' or confirmpasswordlabel_entry.get() == '':
            messagebox.showerror('Error','All fields are Required',parent=top)
        elif newpasswordlabel_entry.get() != confirmpasswordlabel_entry.get():
            messagebox.showerror('Error','Password mismatch',parent=top)
        else:
            
            mydb = mysql.connector.connect(host='localhost',user='root',password='Cwbetrand29',database='bankdb')
            mycursor = mydb.cursor()
            query = 'select * from bankdata2 where username=%s'
            mycursor.execute(query,(userlabel_entry.get(),))
            
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error',"User doesn't exist")
            else:
                query = 'update bankdata2 set password=%s where username=%s'
                mycursor.execute(query,(newpasswordlabel_entry.get(),userlabel_entry.get()))
                mydb.commit()
                mydb.close()
                clear()
                messagebox.showinfo('Success','Password is reset successfully! please login with your new password',parent=top)
                top.destroy()
        
    
    usernamelabel = Label(top,text='Username:',font=('ariel',15,'bold'),fg='white',bg='black')
    usernamelabel.place(x=10,y=80)
    userlabel_entry = Entry(top,width=40,font=('ariel',12,'bold'),bd=0)
    userlabel_entry.place(x=15,y=120)
    
    newpass_var = StringVar()  
    newpasswordlabel = Label(top,text='New Password:',font=('ariel',15,'bold'),fg='white',bg='black')
    newpasswordlabel.place(x=10,y=170)
    newpasswordlabel_entry = Entry(top,width=40,fg='magenta2',font=('ariel',12,'bold'),textvariable=newpass_var,bd=0)
    newpasswordlabel_entry.place(x=15,y=210)
    
    confirmpass_var = StringVar()
    confirmpasswordlabel = Label(top,text='Confirm Password:',font=('ariel',15,'bold'),fg='white',bg='black')
    confirmpasswordlabel.place(x=10,y=260)
    confirmpasswordlabel_entry = Entry(top,width=40,fg='magenta2',font=('ariel',12,'bold'),textvariable=confirmpass_var,bd=0)
    confirmpasswordlabel_entry.place(x=14,y=300)
    
    submitbtn = Button(top,text="Submit",bg='firebrick2',activebackground='firebrick2',command=submit,
                   fg='white',height=2,bd=0,activeforeground='white',width=15,cursor='hand2',font=('Arial',15,'bold'))
    submitbtn.place(x=110,y=410)
    
    
    top.mainloop()    
             

systemlabel = Label(root,text="BANKING MANAGEMENT SYSTEM",font=('Arial',20,'bold'),fg='firebrick2',bg='black')
systemlabel.pack(fill=X)

signuplabel = Label(root,text="Login",font=('Arial',20,'bold'),fg='firebrick2',bg='black')
signuplabel.place(x=200,y=70)

namelabel = Label(root,text="Username:",font=('Arial',18,'bold'),fg='white',bg='black')
namelabel.place(x=50,y=150)
name_entry = Entry(root,font=('Arial',15,'bold'),width=35)
name_entry.place(x=55,y=190)

password_var = StringVar()
checkvar = IntVar(value=0)
password_label = Label(root,text="Password:",font=('Arial',18,'bold'),fg='white',bg='black')
password_label.place(x=50,y=250)
password_entry = Entry(root,font=('Arial',15,'bold'),show='*',width=35,textvariable=password_var)
password_entry.place(x=55,y=290)

showpassword = Checkbutton(root,variable=checkvar,font=('Arial',10,'bold'),bd=0,fg='white',bg='black',
                           command=show_pass,activeforeground='white')
showpassword.place(x=320,y=340)
showpassword = Label(root,text="Show Password",font=('Arial',10,'bold'),fg='white',bg='black')
showpassword.place(x=340,y=340)

forgetbtn = Button(root,text='Forgot Password?',fg='firebrick2',bg='black',
                  activebackground='black',command=forgot,activeforeground='firebrick2',cursor='hand2',
                   font=('ariel',10,'bold underline'),bd=0)
forgetbtn.place(x=50,y=340)


logbtn = Button(root,text='Login',font=('Arial',13,'bold'),width=10,fg='white',bg='firebrick2',cursor='hand2',command=log_database,height=2)
logbtn.place(x=200,y=430)

dontlabel = Label(root,text="Don't have an account?",font=('Arial',13),fg='white',bg='black')
dontlabel.place(x=75,y=570)

signbtn = Button(root,text='Create a New one',font=('Arial',13,'bold underline'),bd=0,fg='firebrick2',bg='black',cursor='hand2',activebackground='black',
                 activeforeground='firebrick2',command=sign_up)
signbtn.place(x=250,y=567)

root.mainloop()