from tkinter import *

class NLPApp:
    def __init__(self) :
        self.root=Tk()
        self.root.title('NLP APP')
        self.root.iconbitmap('/resources.favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg="#34495E")
        
        self.login_gui()

        self.root.mainloop()
        
    def login_gui(self):
        self.clearScreen()
        heading=Label(self.root,text='NLP APP',bg="#34495E",fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        email_label=Label(self.root,text='Enter Email',bg="#34495E",fg='white')
        email_label.pack(pady=(10,10))
        self.email_input=Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10),ipady=4)

        password_label=Label(self.root,text='Enter password',bg="#34495E",fg='white')
        password_label.pack(pady=(10,10))
        self.password_input=Entry(self.root,width=30,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn=Button(self.root,text='Login',width=10,height=2)
        login_btn.pack(pady=(30,10))

        label1=Label(self.root,text='Not a Member?',bg="#34495E",fg='yellow')
        label1.pack(pady=(10,10))
        
        register_btn=Button(self.root,text='Register',command=self.register_gui)
        register_btn.pack(pady=(10,10))
    
    def register_gui(self):
        self.clearScreen()

        heading=Label(self.root,text='NLP APP',bg="#34495E",fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        name_label=Label(self.root,text='Enter Name',bg="#34495E",fg='white')
        name_label.pack(pady=(10,10))
        self.name_input=Entry(self.root,width=30)
        self.name_input.pack(pady=(5,10),ipady=4)

        email_label=Label(self.root,text='Enter Email',bg="#34495E",fg='white')
        email_label.pack(pady=(10,10))
        self.email_input=Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10),ipady=4)

        password_label=Label(self.root,text='Enter password',bg="#34495E",fg='white')
        password_label.pack(pady=(10,10))
        self.password_input=Entry(self.root,width=30,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        register_btn=Button(self.root,text='Register',width=10,height=2)
        register_btn.pack(pady=(30,10))

        label1=Label(self.root,text='Already a Member?',bg="#34495E",fg='yellow')
        label1.pack(pady=(10,10))
        
        login_btn=Button(self.root,text='Login',command=self.login_gui)
        login_btn.pack(pady=(10,10))


    def clearScreen(self):
        for i in self.root.pack_slaves():
            i.destroy()


nlp=NLPApp()