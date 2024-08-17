from customtkinter import *
import customtkinter as tk
import webbrowser

app = tk.CTk() 
app.title("Calculator")
app.geometry("600x560")
tk.set_appearance_mode("System")
tk.set_default_color_theme("green")

FontApp = ('Poppins',20,)

for i in range(7):  # Configure rows 0 to 6
    app.grid_rowconfigure(i, weight=1)
for j in range(4):  # Configure columns 0 to 3
    app.grid_columnconfigure(j, weight=1)

def website():
    mtmsite= "https://mtm-x.github.io/"
    webbrowser.open(mtmsite)

def web():
    git = "https://github.com/mtm-x"
    webbrowser.open(git)


def clear():
    out.delete('0.0','end')

def calculate():
    try:
        cal= out.get('0.0', 'end').strip()
        result = eval(cal)
        out.delete('0.0', 'end')
        out.insert('0.0', result)
    except Exception :
        out.delete('0.0','end')
        out.insert('0.0',"Invalid!!")

out=tk.CTkTextbox(app,
                  width=560,
                  height=50,
                  font=(('Arial', 50)),
                  corner_radius=10,
                  border_color="white",
                  border_width=2,
                  )
out.grid(row=0, column=0, columnspan=4, padx=15, pady=15,sticky="nsew")


bt1=tk.CTkButton(app,
                 text="1",
                 width=130,
                 height=60,
                 command=lambda:out.insert('end',1),
                 corner_radius=10,
                 fg_color=("transparent"),
                 border_color="white",
                 border_width=2,
                 text_color="white",
                 font=("",20))
bt1.grid(row=1, column=0, padx=15, pady=2,sticky="nsew")

bt2=tk.CTkButton(app,
                 text="2",
                 width=130,
                 height=60,
                 command=lambda:out.insert('end',2),
                 fg_color=("transparent"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="white",
                 font=("",20))
bt2.grid(row=1, column=1, padx=15, pady=2,sticky="nsew")

bt3=tk.CTkButton(app,
                 text="3",
                 width=130,
                 height=60,
                 command=lambda:out.insert('end',3),
                 fg_color=("transparent"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="white",
                 font=("",20))
bt3.grid(row=1, column=2, padx=15, pady=2,sticky="nsew")

bt4=tk.CTkButton(app,
                 text="+",
                 width=60,
                 height=60,
                 command=lambda:out.insert('end','+'),
                 fg_color=("orange"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="black",
                 font=("",20))
                
bt4.grid(row=1, column=3, padx=15, pady=2,sticky="nsew")

bt5=tk.CTkButton(app,
                 text="4",
                 width=130,
                 height=60,
                 command=lambda:out.insert('end',4),
                 fg_color=("transparent"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="white",
                 font=("",20))
bt5.grid(row=2, column=0, padx=15, pady=2,sticky="nsew")

bt6=tk.CTkButton(app,
                 text="5",
                 width=130,
                 height=60,
                 command=lambda:out.insert('end',5),
                 fg_color=("transparent"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="white",
                 font=("",20))
bt6.grid(row=2, column=1, padx=15, pady=2,sticky="nsew")

bt7=tk.CTkButton(app,
                 text="6",
                 width=130,
                 height=60,
                 command=lambda:out.insert('end',6),
                 fg_color=("transparent"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="white",
                 font=("",20))
bt7.grid(row=2, column=2, padx=15, pady=2,sticky="nsew")

bt8=tk.CTkButton(app,
                 text="-",
                 width=60,
                 height=60,
                 command=lambda:out.insert('end','-'),
                 fg_color=("orange"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="black",
                 font=("",20))
bt8.grid(row=2, column=3, padx=15, pady=2,sticky="nsew")


bt9=tk.CTkButton(app,
                 text="7",
                 width=130,
                 height=60,
                 command=lambda:out.insert('end',7),
                 fg_color=("transparent"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="white",
                 font=("",20))
bt9.grid(row=3, column=0, padx=15, pady=2,sticky="nsew")

bt10=tk.CTkButton(app,
                 text="8",
                 width=130,
                 height=60,
                 command=lambda:out.insert('end',8),
                 fg_color=("transparent"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="white",
                 font=("",20))
bt10.grid(row=3, column=1, padx=15, pady=2,sticky="nsew")

bt11=tk.CTkButton(app,
                 text="9",
                 width=130,
                 height=60,
                 command=lambda:out.insert('end',9),
                 fg_color=("transparent"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="white",
                 font=("",20))
bt11.grid(row=3, column=2, padx=15, pady=2,sticky="nsew")


bt12=tk.CTkButton(app,
                 text="x",
                 width=60,
                 height=60,
                 command=lambda:out.insert('end','*'),
                 fg_color=("orange"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="black",
                 font=("",20))
bt12.grid(row=3, column=3, padx=15, pady=2,sticky="nsew")


bt13=tk.CTkButton(app,
                 text="0",
                 width=130,
                 height=60,
                 command=lambda:out.insert('end',0),
                 fg_color=("transparent"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="white",
                 font=("",20))
bt13.grid(row=4, column=0, padx=15, pady=2,sticky="nsew")

bt14=tk.CTkButton(app,
                 text="÷",
                 width=60,
                 height=60,
                 command=lambda:out.insert('end', '/'),
                 fg_color=("orange"),
                 corner_radius=10,
                 border_color="white",
                 border_width=2,
                 text_color="black",
                 font=("",20))
bt14.grid(row=4, column=3, padx=15, pady=2,sticky="nsew")

calculatebt=tk.CTkButton(app,
                         width=130,
                         height=60,
                         corner_radius=10,
                         text="=",
                         command=calculate,
                         #font=('',20),
                         border_color="white",
                         border_width=2,
                         text_color="white",
                         fg_color=("transparent"),
                         font = FontApp)
calculatebt.grid(row=4, column=2, padx=15,pady=2,sticky="nsew")

my_clear = tk.CTkButton(app,
                        text="Clear",
                        command=clear,
                        width=130,
                        height=60,
                        fg_color=("transparent"),
                        corner_radius=10,
                        font=('',20),
                        border_color="white",
                        border_width=2,
                        text_color="white",
                        )
my_clear.grid(row=4, column=1, padx=15,pady=2,sticky="nsew")


mtm=tk.CTkButton(app,
                 text="GitHub",
                 border_color="white",
                 width=400,
                 height=40,
                 border_width=2,
                 text_color="black",
                 fg_color="lightblue",
                 command=web,
                 corner_radius=10,
                 font = FontApp
                 )
mtm.grid(row=5,columnspan=5,pady=15,)

myweb=tk.CTkButton(app,
                   text="My Website",
                   font = FontApp,
                   border_color="white",
                   width=400,
                   height=30,
                   border_width=2,
                   text_color="black",
                   fg_color="lightblue",
                   command=website,
                   corner_radius=10)
myweb.grid(row=6, columnspan=5,pady=5,)

app.mainloop()
