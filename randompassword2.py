from tkinter import *
import string
import random
import pyperclip


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_box.get())

    if choice.get()==1:
        passwordfield.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordfield.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordfield.insert(0,random.sample(all,password_length))

def copy():
    random_password=passwordfield.get()
    pyperclip.copy(random_password)

root=Tk()
root.config(bg='#800000')
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='#800000',fg='white')
passwordLabel.grid()

weakradioButton=Radiobutton(root,text='Weak Password',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=7)

mediumradioButton=Radiobutton(root,text='Medium Password',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=7)

strongradioButton=Radiobutton(root,text='Strong Password',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=7)


lengthLabel=Label(root,text='Password Length',font=('times new roman',20,'bold'),bg='#800000',fg='white')
lengthLabel.grid()

length_box=Spinbox(root,from_=5,to_=20,width=5,font=Font)
length_box.grid(pady=7)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=7)

passwordfield=Entry(root,width=25,bd=2,font=Font)
passwordfield.grid(pady=7)

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=7)

root.mainloop()
