#gui implementation
from tkinter import Label
import tkinter
import imageTesting
import application
from tkinter import *

def GUI():
    root = Tk()
    pssword_var= tkinter.StringVar()
    input_var = tkinter.StringVar()
    #makes the encrypt file
    root.title("My password encryptr")
    root.geometry('300x120')

    lbl = Label(root, text = "What would you like to do?")
    lbl.grid()

    #chooseing to decrypt
    def clickDecrypt():
        dec = Label(root, text = "paste image file location")
        dec.grid(column = 0, row = 3)
        
        image = Entry(root, width = 10)
        image.grid(column = 1, row = 3)

        btn1 = Button(root, text = "   Decrypt   ", fg = "red", command = clickDecrypt)
        btn1.grid(column = 1, row = 2)

        btn2 = Button(root, text = "Execute Decryption", fg = "red", command = clickExeDecrypt)
        btn2.grid(column = 1, row = 4)
    
    #executes a decryption on supplied image
    #NEED TO EXECUTE DECRYPTION AFTER CLICK OF THIS BUTTON
    def clickExeDecrypt():
        lbl = Label(root, text = "DECRYPTING")
        imageTesting.unsaltPassword()
        lbl.grid()


    #choose to encrypt and produces the texts for it
    def clickEncrypt():
        enc = Label(root, text = "enter desired image and desired password")
        enc.grid(column = 0, row = 3)
        imageIN = Entry(root,textvariable=input_var,width=20)
        imageIN.grid(column=1,row=3)

        password = Entry(root,textvariable = pssword_var,width = 20)
        password.grid(column = 2, row = 3)
        
        btn2 = Button(root, text = "Execute Encryption", fg = "blue", command = clickExeEncrypt)
        btn2.grid(column = 1, row = 4)

    #execute the encryption after entered text
    #NEED TO EXECUTE ENCRYTION AFTER THE CLICK OF THIS BUTTON
    def clickExeEncrypt():
        lbl = Label(root, text = "ENCRYPTING")
        img = input_var.get()
        url = application.pullImage(img)
        psswrd = pssword_var.get()
        imageTesting.saltedPassword(url,psswrd)
        lbl.grid()


    #creates the button for encryption
    btn1 = Button(root, text = "encryption" , fg = "blue", command = clickEncrypt)
    btn1.grid(column = 1, row = 2)
    
    #creates the button for decryption
    btn2 = Button(root, text = "decryption" , fg = "red", command = clickDecrypt)
    btn2.grid(column = 1, row = 4)

    root.mainloop()


GUI()