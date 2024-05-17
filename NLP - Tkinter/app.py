from tkinter import *
from tkinter import messagebox
from db import Database
from api import API

class NLPApp:
    def __init__(self) :
        self.root=Tk()
        self.root.title('NLP APP')
        self.root.iconbitmap('/resources.favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg="#34495E")
        self.dbo=Database()
        self.apio=API()
        
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

        login_btn=Button(self.root,text='Login',width=10,height=2,command=self.perform_login)
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

        register_btn=Button(self.root,text='Register',width=10,height=2,command=self.perform_registration)
        register_btn.pack(pady=(30,10))

        label1=Label(self.root,text='Already a Member?',bg="#34495E",fg='yellow')
        label1.pack(pady=(10,10))
        
        login_btn=Button(self.root,text='Login',command=self.login_gui)
        login_btn.pack(pady=(10,10))

    def home_gui(self):
        self.clearScreen()

        heading=Label(self.root,text='NLP APP',bg="#34495E",fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        ner_btn=Button(self.root,text='Name Entity Recognition',width=15,height=3,command=self.ner_gui)
        ner_btn.pack(pady=(30,10))

        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=15,height=3,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(30,10))

        emotion_btn=Button(self.root,text='Emotion Prediction',width=15,height=3,command=self.emotion_gui)
        emotion_btn.pack(pady=(30,10))

        logout_btn=Button(self.root,text='Logout',command=self.login_gui)
        logout_btn.pack(pady=(30,10))

    def sentiment_gui(self):
        self.clearScreen()

        heading=Label(self.root,text='NLP APP',bg="#34495E",fg='white')
        heading.pack(pady=(30,20))
        heading.configure(font=('verdana',24,'bold'))

        heading2=Label(self.root,text='Sentiment Analysis',bg="#34495E",fg='white')
        heading2.pack(pady=(10,30))
        heading2.configure(font=('verdana',20))

        sentiment_label=Label(self.root,text='Enter Text',bg="#34495E",fg='white')
        sentiment_label.pack(pady=(10,10))
        self.sentiment_input=Entry(self.root,width=30)
        self.sentiment_input.pack(pady=(5,10),ipady=4)

        self.sentiment_result=Label(self.root,text='',bg="#34495E",fg='white')
        self.sentiment_result.pack(pady=(10,10))

        sentiment_btn=Button(self.root,text='Analyse Sentiment',command=self.perform_sentiment)
        sentiment_btn.pack(pady=(10,10))

        goback_btn=Button(self.root,text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(30,10))

    def ner_gui(self):
        self.clearScreen()

        heading=Label(self.root,text='NLP APP',bg="#34495E",fg='white')
        heading.pack(pady=(30,20))
        heading.configure(font=('verdana',24,'bold'))

        heading2=Label(self.root,text='Name Entity Recognition',bg="#34495E",fg='white')
        heading2.pack(pady=(10,30))
        heading2.configure(font=('verdana',20))

        ner_label=Label(self.root,text='Enter Text',bg="#34495E",fg='white')
        ner_label.pack(pady=(10,10))
        self.ner_input=Entry(self.root,width=30)
        self.ner_input.pack(pady=(5,10),ipady=4)

        self.ner_result=Label(self.root,text='',bg="#34495E",fg='white')
        self.ner_result.pack(pady=(10,10))

        ner_btn=Button(self.root,text='NER',command=self.perform_ner)
        ner_btn.pack(pady=(10,10))

        goback_btn=Button(self.root,text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(30,10))



    def emotion_gui(self):
        self.clearScreen()

        heading=Label(self.root,text='NLP APP',bg="#34495E",fg='white')
        heading.pack(pady=(30,20))
        heading.configure(font=('verdana',24,'bold'))

        heading2=Label(self.root,text='Emotion Prediction',bg="#34495E",fg='white')
        heading2.pack(pady=(10,30))
        heading2.configure(font=('verdana',20))

        emotion_label=Label(self.root,text='Enter Text',bg="#34495E",fg='white')
        emotion_label.pack(pady=(10,10))
        self.emotion_input=Entry(self.root,width=30)
        self.emotion_input.pack(pady=(5,10),ipady=4)

        self.emotion_result=Label(self.root,text='',bg="#34495E",fg='white')
        self.emotion_result.pack(pady=(10,10))

        emotion_btn=Button(self.root,text='Emotion Prediction',command=self.perform_emotion)
        emotion_btn.pack(pady=(10,10))

        goback_btn=Button(self.root,text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(30,10))



    def clearScreen(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password = self.password_input.get()
        res = self.dbo.registration(name,email,password)
        if res:
            messagebox.showinfo("Success",'Registration Successfull! Please do Login')
        else :
            messagebox.showerror("Error","Email Already Exists!")
    
    def perform_login(self):
        email=self.email_input.get()
        password = self.password_input.get()
        res = self.dbo.login(email,password)
        if res:
            messagebox.showinfo("Success",'Login Successfull!!!')
            self.home_gui()
        else :
            messagebox.showerror("Error","Invalid Email/Password!!")

    def perform_sentiment(self):
        text=self.sentiment_input.get()
        res=self.apio.sentiment_analysis(text)
        result=""
        for i in res['sentiment']:
          result+=i+"--->"+str(res['sentiment'][i]) + '\n'
        
        self.sentiment_result['text']=result

    def perform_ner(self):
        text=self.ner_input.get()
        res=self.apio.ner(text)
        result=""
        for i in res['ner']:
          result+=i+"--->"+res['ner'][i] + '\n'
        
        self.ner_result['text']=result

    def perform_emotion(self):
        text=self.emotion_input.get()
        res=self.apio.emotion(text)
        print(res)
        result=""
        for i in res['emotion']:
          result+=i+"--->"+str(res['emotion'][i]) + '\n'
        
        self.emotion_result['text']=result


nlp=NLPApp()