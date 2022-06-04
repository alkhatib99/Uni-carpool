from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
import mysql.connector 

help_str = '''
ScreenManager:
    MainScreen:
    LoginScreen:
    SignupScreen:
<LoginScreen>:
    name:'loginscreen'
    MDCard:
        orientation:'vertical'
        size_hint:None,None
        size:320, 400
        pos_hint:{'center_x':.5, 'center_y':.5}
        padding:15
        spacing:10
        Image:
            source:'assets//unicarpooltext.png'
            halign:"center"
            size_hint_y: None
            height:self.texture_size[1]
            padding:20
            pos_hint:{"center_x":.5, "center_y":.5}
        MDTextFieldRound:
            id:login_email
            hint_text:"username"
            icon_right:"account"
            size_hint_x: None
            width: 220
            font_size:20
            md_bg_color:[0/255, 0/255, 0/255, 1]
            color_active:[1,1,1,1]
            pos_hint:{"center_x":.5}
        MDTextFieldRound:
            id:login_password
            hint_text:"password"
            icon_right:"eye-off"
            size_hint_x: None
            width: 220
            font_size:20
            pos_hint:{"center_x":.5}
        MDLabel:
            text: "Forget Password?"
            # on_press:()
            font_size: 16
            font_name: 'SegoeUI'
            font_style:"Subtitle1"
            color:[245/255, 149/255, 35/255, 1]
        MDLabel:
            text: "Don't have an account? Sign up"
            # on_press:()
            font_size: 16
            font_name: 'SegoeUI'
            font_style:"Subtitle1"
            color:[245/255, 149/255, 35/255, 1]

        MDRaisedButton:
            md_bg_color: app.theme_cls.primary_light
            text:'Login'
            pos_hint: {'center_x':0.5}
            on_press:
                app.login()
                # app.username_changer() 
            
        
        Widget:
            size_hint_y:None
            height: 3                   

<SignupScreen>:
    name:'signupscreen'
    Image:
        source:'assets//unicarpooltext.png'
        halign:"center"
        size_hint_y: None
        height:self.texture_size[1]
        padding:20
        pos_hint:{"center_x":.5, "center_y":.9}
    MDTextField:
        id:user_email
        hint_text:" Email"
        icon_right:"account"
        size_hint_x: None
        width: 220
        font_size:20
        pos_hint:{"center_x":.5,'center_y':0.8}
    MDTextField:
        id:user_reemail
        hint_text:" Confirm Email"
        icon_right:"account"
        size_hint_x: None
        width: 220
        font_size:20
        pos_hint:{"center_x":.5, "center_y":0.7}
    MDTextField:
        id:user_passsword
        hint_text:" Password"
        icon_right:"eye-off"
        size_hint_x: None
        width: 220
        font_size:20
        pos_hint:{"center_x":.5, "center_y":0.6}
    MDTextField:
        id:user_repassword
        hint_text:"Confirm Password"
        icon_right:"account"
        size_hint_x: None
        width: 220
        font_size:20
        pos_hint:{"center_x":.5, "center_y":0.5}
    MDTextField:
        id:user_phone
        hint_text:"Mobile number"
        # icon_right:"account"
        size_hint_x: None
        width: 220
        font_size:20
        pos_hint:{"center_x":.5, "center_y":0.4}

    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()

    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'

    

    
<MainScreen>:
    name: 'mainscreen'
    MDRaisedButton:
        pos_hint: {'center_x':0.5,'center_y':0.5}

        text:'Login'

        on_press:
            root.manager.current='loginscreen'
    
    MDRaisedButton:
        text:'SignUp'
        pos_hint: {'center_x':0.5,'center_y':0.6}

        on_press:
            root.manager.current='signupscreen'

'''


class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))


class LoginApp(MDApp):
    database=mysql.connector.Connect(host='localhost', user="root", password="root", database="unicarpool")
    cursor=database.cursor(buffered=True)
    cursor.execute("select * from user")
        
    def build(self):
        
        # self.theme_cls.primary_light='Lime'
        self.strng = Builder.load_string(help_str)
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.user_email.text
        signupReEmail = self.strng.get_screen('signupscreen').ids.user_reemail.text
        signupPassword = self.strng.get_screen('signupscreen').ids.user_passsword.text
        signupRePassword = self.strng.get_screen('signupscreen').ids.user_repassword.text
        signupPhone = self.strng.get_screen('signupscreen').ids.user_phone.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupPhone.split() == []:
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2))
            self.dialog.open()
        if signupEmail!= signupReEmail:
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please confirm the email and confirm email are equal',size_hint = (0.7,0.2))
            self.dialog.open()
            
        if signupPassword!= signupRePassword:
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please confirm the password and confirm password are equal',size_hint = (0.7,0.2))
            self.dialog.open()
            
        else:
            try:
                self.cursor.execute(f"insert into user values('{signupEmail}', '{signupPassword}', '{signupPhone}')")
                self.database.commit()
                self.strng.get_screen('signupscreen').ids.user_email.text=""
                self.strng.get_screen('signupscreen').ids.user_reemail.text=""
                self.dialog = MDDialog(text = 'Successfull signup',size_hint = (0.7,0.2))

            finally:
                self.dialog = MDDialog(text = 'Error',size_hint = (0.7,0.2))
                self.dialog.open()
                
        
    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text
        check=False
        
        self.cursor.execute("select * fom user")
        email_list=[]
        for i in self.cursor.fetchall():
            email_list.append(i[0])
        if loginEmail in email_list and loginEmail!="":
            self.cursor.execute(f"select password from user where emai='{loginEmail}'")
            for j in self.cursor:
                if loginPassword==j[0]:
                    self.dialog=MDDialog(
                text="Sucessfull Login"
                        )
                    self.dialog.open()
                else :
                    self.dialog=MDDialog(text="Unsecuccsfull login ")
                    self.dialog.open()
                    print("user no longer exists")

LoginApp().run()