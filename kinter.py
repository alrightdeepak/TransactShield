from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
def callback(selection):
    print(selection)
def isFraud():
    amount= amt_input.get()
    old_balance=oldbal_input.get()
    new_balance=newbal_input.get()
    print(amount, old_balance, new_balance)
    messagebox.showinfo('Prediction:', 'Fraud')
root= Tk()
root.title('TransactShield')
root.minsize(600,600)
root.iconbitmap('icon.ico')
root.geometry("600x650")
root.maxsize(600,800)
root.configure(background='#0096DC')

text_label=Label(root, text='TransactShield- Fraud Detector', fg='white', bg='#0096DC')
text_label.pack(pady=(10,10))
text_label.config(font=('verdana', 20))

img= Image.open('banner.png')
img1=img.resize((450,150))
img= ImageTk.PhotoImage(img1)
img_label= Label(root, image=img)
img_label.pack(pady=(10,10))

type_label=Label(root, text='Enter type of transaction', fg='white', bg='#0096DC')
type_label.pack(pady=(5,5))
type_label.config(font=('verdana', 10))
transact= StringVar(root)
transact.set('PAYMENT')
type_input= OptionMenu(root, transact,"PAYMENT" ,"CASH IN", "CASH OUT", "DEBIT", "TRANSFER", command=callback)
type_input.pack(pady=(10,10))

amt_label=Label(root, text='Enter the amount of payment', fg='white', bg='#0096DC')
amt_label.pack(pady=(5,5))
amt_label.config(font=('verdana', 10))
amt_input= Entry(root, width=50)
amt_input.pack(ipady=6,pady=(1,15))

oldbal_label=Label(root, text='Enter the old balance in account', fg='white', bg='#0096DC')
oldbal_label.pack(pady=(5,5))
oldbal_label.config(font=('verdana', 10))
oldbal_input= Entry(root, width=50)
oldbal_input.pack(ipady=6,pady=(1,15))

newbal_label=Label(root, text='Enter the new balance in account', fg='white', bg='#0096DC')
newbal_label.pack(pady=(5,5))
newbal_label.config(font=('verdana', 10))
newbal_input= Entry(root, width=50)
newbal_input.pack(ipady=6,pady=(1,15))

check_fraud= Button(root, text="Check", bg='white', fg='black', command=isFraud)
check_fraud.pack(pady=(10, 10))

root.mainloop()