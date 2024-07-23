import customtkinter as ctk
from tkinter.filedialog import askopenfilename
import sys

def qbutton():
    sys.exit()

def start_progress():
    progress.place(x=100, y=150)
    if progress.get() < 1:
        progress.set(progress.get() + .02)
        frame.after(3, start_progress)
    else:
        text.pack(side='bottom', pady=40)
        frame.update_idletasks()
        frame.after(1200, text.configure(text='Program Ending...'))
        frame.update_idletasks()
        frame.after(1200, command=qbutton())

def selact():
    global act
    actions = askopenfilename()
    if actions:
        actbut.configure(fg_color='green', text='Actions Selected ✅', 
                         hover_color='dark green', state="disabled")
        act = True
        try:
            if sta:
                start_button.configure(state="normal")
        except: return

def selsta():
    global sta
    statements = askopenfilename()
    if statements:
        stabut.configure(fg_color='green', text='Statements Selected ✅', 
                         hover_color='dark green', state="disabled")
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
        if sta: stabut.configure(fg_color='green', hover_color='dark green')
        if act: actbut.configure(fg_color='green', hover_color='dark green')
        m.update_idletasks()
    if switch_var.get() == "on":
        m.update_idletasks()
        stabut.configure(fg_color='firebrick1', hover_color='firebrick3')
        actbut.configure(fg_color='firebrick1', hover_color='firebrick3')
        start_button.configure(fg_color='firebrick1', hover_color='firebrick3')
        if sta: stabut.configure(fg_color='green', hover_color='dark green')
        if act: actbut.configure(fg_color='green', hover_color='dark green')
        m.update_idletasks()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

m = ctk.CTk()
m.geometry("400x300")
m.title("Expensive Statements Summary")
switch_var = ctk.StringVar(value="off")

# Frame
frame = ctk.CTkFrame(master=m, width=380, height=280, border_color='red')
frame.place(x=10, y=10)
frame.pack_propagate(0)  # Prevent frame from resizing 

# Widgets
actions = ''; statements = ''
actbut = ctk.CTkButton(frame, text="Select Actions", command=selact)
stabut = ctk.CTkButton(frame, text="Select Statements", command=selsta)
button = ctk.CTkButton(frame, text="End Process", command=qbutton, fg_color='gray', hover_color='dim gray')
switch = ctk.CTkSwitch(frame, text="", command=switch_event, variable=switch_var, offvalue="off", onvalue="on")

# Progress bar
progress = ctk.CTkProgressBar(frame, width=180, progress_color='SeaGreen1')
start_button = ctk.CTkButton(frame, text="Create Summary", command=start_progress, state='disabled')
text = ctk.CTkLabel(frame, text='Summary Created!')

# Window Packing
m.minsize(400, 300)
m.maxsize(400, 300)

stabut.place(x=20,y=20)
actbut.place(x=220,y=20)
start_button.place(x=120,y=100)
progress.set(0); progress.pack_forget()
text.pack_forget()
switch.place(x=335, y=245)
button.pack(side='bottom', pady=10)

m.mainloop()