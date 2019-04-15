from tkinter import *
import tkinter
from tkinter import messagebox
from appjar import gui
import mysql.connector

Information_match = FALSE
EnterIntoInterface = FALSE

class chat(object):


    def __init__(self):

        def pressEnter(btn):
            submit = self.app.getEntry("chatBox")
            self.app.addListItem("chatWindow", submit)


        self.app = gui("Chat Server")
        self.app.setFont(12)
        self.app.addLabelOptionBox("Servers", ["Default"])
        self.app.addListBox("chatWindow")


        self.app.addEntry("chatBox", 2)
        self.app.addButton("Send", pressEnter, 2, 1)
        self.app.setEntryDefault("chatBox", "/help for list of commands")
        self.app.go()

class Login(object):
    def __init__(self):


        #set up the window, also its name and size
        self.root= tkinter.Tk()
        self.root.title("User Login")
        self.root.geometry('450x300')

        #set up an image
        self.canvas = tkinter.Canvas(self.root, height=300, width=450)
        self.image_file = tkinter.PhotoImage(file='1.gif')
        self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)
        self.canvas.pack(side='top')

        #set up the label for account and password
        self.label_account = tkinter.Label(self.root, text = 'account:')
        self.label_password = tkinter.Label(self.root, text='Password: ')

        #set up the input for the user
        self.input_account = tkinter.Entry(self.root, width=30)
        self.input_password = tkinter.Entry(self.root, show='*',  width=30)

        #set up the button for users to click, first button used to login, second button used to create accound, the last one used to reset
        #your password
        self.login_button = tkinter.Button(self.root, command = self.backstage_interface, text = "Login", width=10)
        self.siginUp_button = tkinter.Button(self.root, command = self.siginUp_interface, text = "Sign up", width=10)
        self.reset_button = tkinter.Button(self.root, command = self.updateInterface,text = "Reset password",width =11)


    def gui_arrange(self):
        self.label_account.place(x=60, y= 170)
        self.label_password.place(x=60, y= 195)
        self.input_account.place(x=135, y=170)
        self.input_password.place(x=135, y=195)
        self.login_button.place(x=70, y=235)
        self.siginUp_button.place(x=170, y=235)
        self.reset_button.place(x=270,y=235)


    def siginUp_interface(self):

        self.window= tkinter.Tk()
        self.window.title("Create your account")
        self.window.geometry('450x300')


        self.label_account_1 = tkinter.Label(self.window, text = 'account:')
        self.label_password_1 = tkinter.Label(self.window, text='Password: ')

        #set up the input for the user
        self.input_account_1 = tkinter.Entry(self.window, width=30)
        self.input_password_1 = tkinter.Entry(self.window, show='*',  width=30)

        #set up the button for users to click, one for login, the other for create account
        self.create_button = tkinter.Button(self.window, command = self.createAccount, text = "Create", width=10)


        self.label_account_1.place(x=60, y= 170)
        self.label_password_1.place(x=60, y= 195)
        self.input_account_1.place(x=135, y=170)
        self.input_password_1.place(x=135, y=195)
        self.create_button.place(x=140, y=235)




    def createAccount(self):


        conn = mysql.connector.connect(user='root', password='Jack0105',
                              database='userDb')

        new_account = self.input_account_1.get()
        new_password = self.input_password_1.get()

        cursor = conn.cursor()

        cursor.execute('insert into users (account, password) values (%s, %s)', [new_account,new_password])

        conn.commit()

        conn.close()
        self.window.destroy()

        tkinter.messagebox.showinfo(title='Create Account', message='success')
    def resetPassword(self):
        conn = mysql.connector.connect(user='root', password='Jack0105',
                              database='userDb')
        old_account = self.input_account_1.get()
        new_password = self.input_password_1.get()

        cursor = conn.cursor()

        cursor.execute('update users set password = "%s" where account = "%s"' % (new_password,old_account))
        conn.commit()

        conn.close()



        self.window.destroy()
        tkinter.messagebox.showinfo(title='Reset Password', message='You have reset your password successfully')

    def updateInterface(self):
        self.window= tkinter.Tk()
        self.window.title("Reset password")
        self.window.geometry('450x300')


        self.label_account_1 = tkinter.Label(self.window, text = 'account:')
        self.label_password_1 = tkinter.Label(self.window, text='Password: ')

        #set up the input for the user
        self.input_account_1 = tkinter.Entry(self.window, width=30)
        self.input_password_1 = tkinter.Entry(self.window, show='*',  width=30)

        #set up the button for users to click, one for login, the other for create account
        self.reset_button = tkinter.Button(self.window, command = self.resetPassword, text = "reset", width=10)


        self.label_account_1.place(x=60, y= 170)
        self.label_password_1.place(x=60, y= 195)
        self.input_account_1.place(x=135, y=170)
        self.input_password_1.place(x=135, y=195)
        self.reset_button.place(x=140, y=235)
    def backstage_interface(self):

        #get the user input
        account = self.input_account.get()
        password = self.input_password.get()


        conn = mysql.connector.connect(user='root', password='Jack0105',
                                  database='userDb')


        cursor = conn.cursor()
        cursor.execute('select * from users')
        values = cursor.fetchall()
        print(values)


        for i in values:
            if i[0] == account and i[1] == password:
                print(i,"found it")

                global Information_match
                Information_match = TRUE
                break
            else:
                    print("still trying")
            #if the input matches what we have in our database
        if Information_match == TRUE:

                self.root.destroy()
                print("success")

                global EnterIntoInterface
                EnterIntoInterface = TRUE

        elif account == '' or password == '':
                tkinter.messagebox.showinfo(title='ERROR', message = 'please type your username or password')
        else:
                tkinter.messagebox.showinfo(title='ERROE',message = 'no account found')


def main():
    L = Login()

    L.gui_arrange()

    tkinter.mainloop()

    if EnterIntoInterface == TRUE:

        K = chat()

if __name__ == '__main__':
    main()