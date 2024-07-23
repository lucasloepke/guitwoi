import customtkinter as ctk
from tkinter.filedialog import askopenfilename
import sys

def qbutton():
    m.title('Goodbye!')
    button.configure(text="  Goodbye!  ")
    frame.update_idletasks()
    frame.after(350)
    sys.exit()

def start_progress():
    progress.place(x=185, y=210)
    if progress.get() < 1:
        progress.set(progress.get() + .02)
        frame.after(3, start_progress)
    else:
        text.pack(side='bottom', pady=10)
        frame.update_idletasks()
        frame.after(1200, text.configure(text='Program Ending...'))
        frame.update_idletasks()
        frame.after(1200, command=qbutton())

def selact():
    global act
    actions = askopenfilename()
    if actions:
        actbut.configure(fg_color='green', text='Actions ✅', 
                         hover_color='dark green', state="disabled",
                         font=ctk.CTkFont(family='72', weight="normal"))
        act = True
        try:
            if sta:
                start_button.configure(state="normal")
        except: return

def selsta():
    global sta
    statements = askopenfilename()
    if statements:
        stabut.configure(fg_color='forest green', text='Statements ✅', 
                         hover_color='dark green', state="disabled",
                         font=ctk.CTkFont(family='72', weight="normal"))
        sta = True
        try:
            if act:
                start_button.configure(state="normal")
        except: return

def switch_event():
    if switch_var.get() == "off":
        stabut.configure(fg_color='#1F6AA5', hover_color='#144870')
        actbut.configure(fg_color='#1F6AA5', hover_color='#144870')
        start_button.configure(fg_color='#1F6AA5', hover_color='#144870')
        progress.configure(progress_color='blue violet')
        try:
            if sta: stabut.configure(fg_color='green', hover_color='dark green')
        except: pass
        try: 
            if act: actbut.configure(fg_color='green', hover_color='dark green')
        except: pass
        m.update_idletasks()
    if switch_var.get() == "on":
        m.update_idletasks()
        stabut.configure(fg_color='SpringGreen3', hover_color='SpringGreen4')
        actbut.configure(fg_color='SpringGreen3', hover_color='SpringGreen4')
        start_button.configure(fg_color='SeaGreen3', hover_color='SeaGreen4')
        progress.configure(progress_color='goldenrod1')
        try:
            if sta: stabut.configure(fg_color='green', hover_color='dark green')
        except: pass
        try:
            if act: actbut.configure(fg_color='green', hover_color='dark green')
        except: pass
        m.update_idletasks()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

m = ctk.CTk()
m.geometry("400x300")
m.title("Expensive Statements Summary")
switch_var = ctk.StringVar(value="off")

# Frames
frame = ctk.CTkFrame(master=m, width=380, height=280, border_color='red')
sframe = ctk.CTkFrame(master=m, width=160, height=260, border_color='red', fg_color='gray25')
ssframe = ctk.CTkFrame(master=m, width=140, height=40, border_color='gold', fg_color='gray45')
ssframe.place(x=30, y=230); ssframe.pack_propagate(0)
sframe.place(x=20, y=20); sframe.pack_propagate(0)
frame.place(x=10, y=10); frame.pack_propagate(0)  # Prevent frame from resizing 

# Widgets
actions = ''; statements = ''
actbut = ctk.CTkButton(sframe, text="Select Actions", command=selact, 
                       font=ctk.CTkFont(family='72', weight="bold"))
stabut = ctk.CTkButton(sframe, text="Select Statements", command=selsta, 
                       font=ctk.CTkFont(family='72', weight="bold"))
button = ctk.CTkButton(frame, text="End Process", command=qbutton, fg_color='gray', 
                       hover_color='dim gray', font=ctk.CTkFont(family='72', weight="bold"))
switch = ctk.CTkSwitch(frame, text="", command=switch_event, variable=switch_var, 
                       offvalue="off", onvalue="on", progress_color='SeaGreen3')

# Progress bar
progress = ctk.CTkProgressBar(frame, width=180, progress_color='blue violet', height=20)
start_button = ctk.CTkButton(sframe, text="Create Summary", command=start_progress, 
                             state='disabled', font=ctk.CTkFont(family='72'))
text = ctk.CTkLabel(ssframe, text='Summary Created!')

# Window Packing
m.minsize(400, 300)
m.maxsize(400, 300)

stabut.place(x=10,y=10)
actbut.place(x=10,y=50)
start_button.place(x=10,y=90)
progress.set(0); progress.pack_forget()
text.pack_forget()
switch.place(x=335, y=245)
button.place(x=185, y=242)

m.mainloop()