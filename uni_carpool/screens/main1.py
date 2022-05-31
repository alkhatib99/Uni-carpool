# import all the relevant classes
from distutils.command.build import build
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import pandas as pd
from kivymd.app import MDApp

import mysql.connector



class MainApp(MDApp):
    def build(self):
        self.theme_cls_style="Dark"
        self.theme_cls_palette="BlueGray"
        
        
    
        
        # create Database.Or.Connect.To.One
        # conn=sqlite3.connect("first_db.db")
        mydb=mysql.connector.connect(
                        host='localhost',
                        user="root",
                        passwd="root" ,
                        database="second_db",)
        
        # Create a Cursor 
        c=mydb.cursor()
        
        # Create A Database
        c.execute("CREATE DATABASE IF NOT exists second_db")
        
        # check if database is excuete 
        # c.execute("SHOW DATABASE")
        # for db in c:
        #     print(db)
        
        
        # Create A table 
        c.execute("""CREATE TABLE if not exists users(username VARCHAR(255), password VARCHAR(255))""")
        
        
        # Check if table created 
        # c.execute("SELECT * FROM users")
        # print(c.description)
        
        
        # Commit our changes 
        # conn.commit()
        mydb.commit()
        # # close our connection
        # conn.close()
        mydb.close()
        
        return Builder.load_file("second_db.kv")
    
    def submit(self):
        # Create Database or Connect To One
        # conn= sqlite3.connect('first_db.db')
        mydb=mysql.connector.connect(
                    host='localhost',
                    user="root",
                    passwd="root" ,
                    database="second_db",)
        # Create A Cursor 
        c= mydb.cursor()
        
        
    
        #Add A Record 
        sql_command="INSERT INTO users(username) VLAUES(%s)"
        values=(self.root.ids.word_input.text)
        
        
        #excuete the command 
        c.execute(sql_command,values)
        
        
        # Add a littile message
        self.root.ids.word_label.text=f'{self.root.ids.word_input}'
        
        # Clear the input text 
        self.root.ids.word_input.text=''
        
        # Commit pu changes 
        mydb.commit()
        
        # Close our connectio 
        mydb.close()
        
        
    def show_records(self):
        mydb=mysql.connector.connect(
                    host='localhost',
                    user="root",
                    passwd="root" ,
                    database="second_db",)
        
        c= mydb.cursor()
        
        # Grap records from database 
        c.excute("SELECT * FROM users")
        records=c.fetchall()
        word=''
        
        # Loop through records
        
        for record in records:
            word=f'{word}\n{record[0]}'
            self.root.ids.word_label.text=f'{word}'
        
        mydb.commit()
        
        mydb.close()
        
if __name__ == '__main__':
    MainApp.run()
# # class to call the popup function
# class PopupWindow(Widget):
# 	def btn(self):
# 		popFun()

# # class to build GUI for a popup window
# class P(FloatLayout):
# 	pass

# # function that displays the content
# def popFun():
# 	show = P()
# 	window = Popup(title = "popup", content = show,
# 				size_hint = (None, None), size = (300, 300))
# 	window.open()

# # class to accept user info and validate it
# class loginWindow(Screen):
# 	email = ObjectProperty(None)
# 	pwd = ObjectProperty(None)
# 	def validate(self):

# 		# validating if the email already exists
# 		if self.email.text not in users['Email'].unique():
# 			popFun()
# 		else:

# 			# switching the current screen to display validation result
# 			sm.current = 'logdata'

# 			# reset TextInput widget
# 			self.email.text = ""
# 			self.pwd.text = ""


# # class to accept sign up info
# class signupWindow(Screen):
# 	name2 = ObjectProperty(None)
# 	email = ObjectProperty(None)
# 	pwd = ObjectProperty(None)
# 	def signupbtn(self):

# 		# creating a DataFrame of the info
# 		user = pd.DataFrame([[self.name2.text, self.email.text, self.pwd.text]],
# 							columns = ['Name', 'Email', 'Password'])
# 		if self.email.text != "":
# 			if self.email.text not in users['Email'].unique():

# 				# if email does not exist already then append to the csv file
# 				# change current screen to log in the user now
# 				user.to_csv('login.csv', mode = 'a', header = False, index = False)
# 				sm.current = 'login'
# 				self.name2.text = ""
# 				self.email.text = ""
# 				self.pwd.text = ""
# 		else:
# 			# if values are empty or invalid show pop up
# 			popFun()
	
# # class to display validation result
# class logDataWindow(Screen):
# 	pass

# # class for managing screens
# class windowManager(ScreenManager):
# 	pass

# # kv file
# kv = Builder.load_file('login.kv')
# sm = windowManager()

# # reading all the data stored
# users=pd.read_csv('login.csv','wr')

# # adding screens
# sm.add_widget(loginWindow(name='login'))
# sm.add_widget(signupWindow(name='signup'))
# sm.add_widget(logDataWindow(name='logdata'))

# # class that builds gui
# class loginMain(App):
# 	def build(self):
# 		return sm

# # driver function
# if __name__=="__main__":
# 	loginMain().run()
