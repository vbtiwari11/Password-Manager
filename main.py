from tkinter import *
from tkinter import messagebox
import pyperclip
import json

JADE='#68A7AD'
SKIN='#E5CB9F'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
  
    password_letter=[random.choice(letters) for _ in range(nr_letters)]
    passowrd_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    passowrd_numbers=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list=passowrd_numbers+passowrd_symbols+password_letter
    
    random.shuffle(password_list)
    
    password ="".join(password_list)
    
    pass_inp.insert(0,password)
    pyperclip.copy(password)
   
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_data=web_inp.get()
    pass_data=pass_inp.get()
    email_data=email_inp.get()
    new_data={web_data:{'email':email_data,
            'password':pass_data,  
            }
        }
    if len(web_data)==0 or len(pass_data)==0:
        messagebox.showinfo(title="error",message="Please enter info")
    else:
        try:

            with open("password_store.json","r") as data_file:
                    
                    #json.dump(new_data,data_file,indent=4)
                    data=json.load(data_file)
        except FileNotFoundError:
            with open("password_store.json","w") as data_file:
                    #print(data)
                    json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data) 
                    

            with open("password_store.json","w") as data_file:
                   json.dump(data,data_file,indent=4)
        finally:
                   web_inp.delete(0,END)
                   pass_inp.delete(0,END)
                    
def search():
    website=web_inp.get()
    try:
        with open("password_store.json","r") as data_file:
            data=json.load(data_file)
            
    except FileNotFoundError:
        messagebox.showinfo(title="error",message="No file found")
    else:
        if website in data:
                email=data[website]["email"]
                password=data[website]['password']
                messagebox.showinfo(title="website",message=f"email:{email}\n password:{password}")
        else:
            messagebox.showinfo(title="error",message="There is no data added for this")
            

# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("MyPassword Manager")
window.config(padx=30,pady=30)
img=PhotoImage(file="logo.png")

canvas=Canvas(width=200,height=200)
canvas.create_image(100,100,image=img) 
#timer_canva=canvas.create_text(100,130,text="00:00",font=("Arial",35,"bold"),fill="white")
canvas.grid(row=0,column=1)

website_label=Label(text="Website Name:")
website_label.grid(row=1,column=0)

web_inp=Entry(width=25)
web_inp.grid(row=1,column=1)

search_button=Button(text="Search",command=search)
search_button.grid(row=1,column=2)

email_label=Label(text="Email Id:")
email_label.grid(row=2,column=0)

email_inp=Entry(width=35,)
email_inp.insert(0,"vbtiwari11@gmail.com")
email_inp.grid(row=2,column=1,columnspan=2)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

pass_inp=Entry(width=25)
pass_inp.grid(row=3,column=1)

generate_password=Button(text="Generate",command=pass_gen)
generate_password.grid(row=3,column=2)

save=Button(width=35,height=1,text="Save",command=save)
save.grid(row=4,column=1,columnspan=2)





window.mainloop()