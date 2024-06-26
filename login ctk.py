import tkinter
import customtkinter
from CTkMessagebox import CTkMessagebox
from PIL import ImageTk, Image
import os
import smtplib , ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# set the theme and color options
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("python/python/P-CTK/custom_theme.json")

# setting up the main window
root = customtkinter.CTk()
root.geometry("600x450")
root.title("LOGIN UI")

# txt file to save user information
credentials_file = "credentials.txt"
rec = []

# background image
bg_img = ImageTk.PhotoImage(
    Image.open("python/python/P-CTK/blue_flower.png"))

def validate_login_fields():
    '''Function to check if username and password fields are filled'''
    if entry1.get() and entry2.get():
        button1.configure(state="normal")
    else:
        button1.configure(state="disabled")

# function to verify if both passwords match or not
def validate_pass_fields():
        '''Function to check if new_password and confirm_password fields are same'''
        if entryy1.get() == entryy2.get():
            buton1.configure(state="normal")
            label4.configure(text=" ")
        else:
            buton1.configure(state="disabled")
            label4.configure(text="Passwords don't match. Try Again")

# to handle user login 
def login(event=None) : 
    
    global rem_me 
    global email
    global password
    rem_me = rem_var.get()
    email = "rude@sassy.com"
    password = "thandibotal"
    
    if email == entry1.get() and password == entry2.get():
        send_notification()
        CTkMessagebox(message='''LOGIN SUCCESSFUL !! Check email for account verification. ''' , title="INFO" , fg_color="#adb5bd" , bg_color="#42474d" , text_color="#343a40" , button_color="#adb5bd" , button_hover_color="#6c757d")
        clear_entry()
        if rem_me :
            save_info(email,password,rem_me)
        else :
            if os.path.exists(credentials_file) :
                os.remove(credentials_file)
    elif email != entry1.get() and password == entry2.get():
        CTkMessagebox(message="WRONG EMAIL !!", title="ERROR" , icon="cancel" , fg_color="#adb5bd" , bg_color="#42474d" , text_color="#343a40" , button_color="#adb5bd" , button_hover_color="#6c757d")
        clear_entry()
    elif email == entry1.get() and password != entry2.get():
        CTkMessagebox(message="WRONG PASSWORD !!", title="ERROR" , icon="cancel" , fg_color="#adb5bd" , bg_color="#42474d" , text_color="#343a40" , button_color="#adb5bd" , button_hover_color="#6c757d")
        clear_entry()
    else:
        CTkMessagebox(message="INVALID USERNAME OR PASSWORD!!", title="ERROR", icon="cancel" , fg_color="#adb5bd" , bg_color="#42474d" , text_color="#343a40" , button_color="#adb5bd" , button_hover_color="#6c757d")
        clear_entry()


# to clear entries either after logging in or error
def clear_entry() : 
        entry1.delete(0,customtkinter.END)
        entry2.delete(0,customtkinter.END)
        checkbox_rem.deselect()

# function to toggle password visibility
def show_pass():
    if sho_var.get() :
        entry2.configure(show="")
    else :
        entry2.configure(show="*")

# saving user information in txt file
def save_info(email,password,rem_me) :
    with open(credentials_file,'w') as fy :
        rec.append(email+"\n")
        rec.append(password+"\n")
        rec.append(f"{rem_me}"+"\n")
        fy.writelines(rec)

# to initialize already saved information for login ui
def initiatilize() :
    email,password,rem_me = load_info()
    if rem_me :
        entry1.insert(0,email)
        entry2.insert(0,password)
    rem_var.set(True)

# reading user information from txt file
def load_info() :
    if os.path.exists(credentials_file) :
        with open(credentials_file,'r') as fy :
            lines = fy.readlines()
            if len(lines) == 3 :
                return lines[0].strip(),lines[1].strip(),lines[2].strip() == 'True'
    return None , None ,False

# function to send verification email
def send_notification():
            reciever_email = 'shashwat24baheti@gmail.com'
            sender_email = 'loginn.verfication@gmail.com'
            password = 'pkca gjfz fpwh acdw'

            # Email configuration
            msg = MIMEMultipart()
            msg["To"] = reciever_email
            msg["From"] = "sundarlal logins"+"<"+sender_email+">"
            msg["Subject"] = "Login Verification."
            msg_body = MIMEText("Dear User,\n\nWe want to ensure the security of your account by implementing a login verification process.\n\nProceed on the following link to verify your login :-\n\nhttps://cl.gy/XWop")
            msg.attach(msg_body)

            context_data = ssl.create_default_context() 
            with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context_data) as server :
                server.login(sender_email, password)
                server.sendmail(sender_email, reciever_email, msg.as_string())

# function to form reset password window
def forgot_password(event=None):
        root.destroy()
        global f_window
        f_window = customtkinter.CTk()
        f_window.geometry("600x450")    
        f_window.title("RESET UI")
        fwg_img = ImageTk.PhotoImage(Image.open("python/python/P-CTK/blue_flower.png"))

        label = customtkinter.CTkLabel(master=f_window , image=fwg_img)
        label.pack()

        frame2 = customtkinter.CTkFrame(master=label , width=320 , height=380)
        frame2.place(relx=0.5 , rely = 0.5, anchor=tkinter.CENTER)

        label1 = customtkinter.CTkLabel(master=frame2 , text="RESET PASSWORD" , font=("Century Gothic",20) )
        label1.place(y=45,x=50)
        
        label2 = customtkinter.CTkLabel(master=frame2 , text="New password")
        label2.place(x=53,y=110)
        global entryy1
        entryy1 = customtkinter.CTkEntry(master=frame2 , placeholder_text="eg- 12334477" , width=220)
        entryy1.place(x=50,y=138)
        entryy1.bind("<KeyRelease>", lambda event: validate_pass_fields())

        label3 = customtkinter.CTkLabel(master=frame2 , text="Confirm password")
        label3.place(x=53,y=170)
        global entryy2
        entryy2 = customtkinter.CTkEntry(master=frame2 , width=220 , placeholder_text="************" , show="*")
        entryy2.place(x=50,y=198)
        entryy2.bind("<KeyRelease>", lambda event: validate_pass_fields())

        global label4
        label4 = customtkinter.CTkLabel(master=frame2 , text="" , font=("Algeria",8) , text_color="red")
        label4.place(x=95,y=230)

        global buton1
        buton1 = customtkinter.CTkButton(master=frame2 , corner_radius=6 , width=120 , text="Submit")
        buton1.place(x=100,y=260)
        buton1.bind("<Button-1>",save_new_pass)

        button2 = customtkinter.CTkButton(master=frame2 , corner_radius=6 , width=120 , text="Exit" , command=exit)
        button2.place(x=100,y=290)

        f_window.mainloop()

# function to exit password reset window
def exit() :
    f_window.destroy()


# function to get all the info to update password
def save_new_pass(event=None) :
    rec.clear()
    email = "rude@sassy.com"
    new_pass = entryy2.get()
    rem_me = rem_var.get()
    update_new_pass(email,new_pass,rem_me)

# function to update password in file
def update_new_pass(email,new_pass,rem_me) :
    try :
        with open(credentials_file,'w') as fy :
            rec.append(email+"\n")
            rec.append(new_pass+"\n")
            rec.append(f"{rem_me}"+"\n")
            fy.writelines(rec)
            if len(rec) == 3 :
                CTkMessagebox(message="PASSWORD RESET SUCCESSFULL !!", title="INFO" , icon="info" , fg_color="#adb5bd" , bg_color="#42474d" , text_color="#343a40" , button_color="#adb5bd" , button_hover_color="#6c757d")
            else :
                CTkMessagebox(message="SOME ERROR OCURRED !!", title="ERROR" , icon="cancel" , fg_color="#adb5bd" , bg_color="#42474d" , text_color="#343a40" , button_color="#adb5bd" , button_hover_color="#6c757d")
    except Exception as e :
        print(f"An error occurred:{e}")

# creating and packing widgets
label1 = customtkinter.CTkLabel(master=root , image=bg_img)
label1.pack()

frame = customtkinter.CTkFrame(master=label1 , width=320 , height=380)
frame.place(relx=0.5 , rely = 0.5, anchor=tkinter.CENTER)

label2 = customtkinter.CTkLabel(master=frame , text="LOGIN SYSTEM" , font=("Century Gothic",20) )
label2.place(y=45,x=50)

entry1 = customtkinter.CTkEntry(master=frame , placeholder_text="Email" , width=220)
entry1.place(x=50,y=110)
entry1.bind("<KeyRelease>", lambda event: validate_login_fields())

entry2 = customtkinter.CTkEntry(master=frame , placeholder_text="Password" , show="*" , width=220)
entry2.place(x=50,y=150)
entry2.bind('<Return>',login)
entry2.bind("<KeyRelease>", lambda event: validate_login_fields(),add='+')

label_f = customtkinter.CTkLabel(master=frame , text="Forgot Password ?", fg_color="#11212D")
label_f.place(x=165,y=185)
label_f.bind('<Button-1>',(forgot_password))

button1 = customtkinter.CTkButton(master=frame , text="Login" , command=login , state="normal" , width=220 , corner_radius=6)
button1.place(x=50,y=230)

img2 = customtkinter.CTkImage(Image.open("python/python/P-CTK/google.png").resize((20,20) , Image.ANTIALIAS))
img3 = customtkinter.CTkImage(Image.open("python/python/P-CTK/FACEBOOK.png").resize((20,20) , Image.ANTIALIAS))

button2 = customtkinter.CTkButton(master=frame , text="Google" , state="normal" , width=100 , corner_radius=6 , compound="left" , image=img2 , text_color="Black" , fg_color="#d8dbea" , hover_color="#A4A4A4")
button2.place(x=50,y=270)

button3 = customtkinter.CTkButton(master=frame , text="Facebook" , state="normal" , width=100 , corner_radius=6 , compound="left" , image=img3 , text_color="Black" , fg_color="#d8dbea" , hover_color="#A4A4A4")
button3.place(x=170,y=270)

sho_var = customtkinter.BooleanVar(value=False)
checkbox_sho = customtkinter.CTkCheckBox(master=frame , text="Show password", variable=sho_var , command=show_pass , checkbox_height=20 , checkbox_width=20)
checkbox_sho.place(x=35,y=320)

rem_var = customtkinter.BooleanVar(value=False)
checkbox_rem = customtkinter.CTkCheckBox(master=frame , text="Remember me" , variable=rem_var , checkbox_height=20 , checkbox_width=20)
checkbox_rem.place(x=175,y=320)


initiatilize()
root.mainloop()



