from customtkinter import *
import customtkinter as tk

app = tk.CTk()
app.title("Calculator")
app.geometry("700x700")

def clear():
    entery.delete(0,END)

def  entryy():
    var1 = entery.get()
    print("hello",var1)
    my_label.configure(text=entery.get())

entery=tk.CTkEntry(app,placeholder_text="enter the number:")
entery.pack(pady="40")

my_label=tk.CTkLabel(app,text="")
my_label.pack(pady="40")

calculatebt=tk.CTkButton(app,width=100,height=20,corner_radius=10,text="Calculate",command=entryy)
calculatebt.pack(pady="20")

my_clear = tk.CTkButton(app,text="Clear",command=clear)
my_clear.pack(pady="20")







app.mainloop()
