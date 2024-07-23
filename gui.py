import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import time

def start_progress():
    progress.start()

    # Simulate a task that takes time to complete
    for i in range(101):
      # Simulate some work
        time.sleep(0.005)  
        progress['value'] = i
        # Update the GUI
        m.update_idletasks()
    time.sleep(0.2)
    complete = True
    if complete:
        text.pack(side='bottom', pady=10)
        m.update_idletasks()
        m.after(1200, text.config(text='Program Ending...'))
        m.title('Goodbye!')
        button.config(text='Goodbye!')
        m.update_idletasks()
        time.sleep(1)
        quit()
    progress.stop()

def selact():
    global act
    actions = askopenfilename()
    if actions:
        actbut.config(bg='spring green', text='Actions Selected ✅')
        act = True
        try:
            if sta:
                start_button.config(state="normal")
        except: return

def selsta():
    global sta
    statements = askopenfilename()
    if statements:
        stabut.config(bg='spring green', text='Statements Selected ✅')
        sta = True
        try:
            if act:
                start_button.config(state="normal")
        except: return

m = tk.Tk(screenName=None,  baseName=None,  className='Tk',  useTk=1)
m.title('SAC Expensive Statements Tool')
complete = False

# Select files button widgets
actions = ''; statements = ''
actbut = tk.Button(m, text="Select Actions", command=selact, pady=5, padx=5)
stabut = tk.Button(m, text="Select Statements", command=selsta, activebackground='white', padx=5, pady=5)

# Create a progressbar widget
progress = ttk.Progressbar(m, style='', length=300, mode="determinate")

# Button to start progress
start_button = tk.Button(m, text="Create Summary", command=start_progress, 
                         bg='turquoise', activebackground='dark turquoise', state='disabled')

label = tk.Label(m, text='Select Files and Create Summary!')
text = tk.Label(m, text='Summary Created!')
button = tk.Button(m, text='End Process', width=25, command=m.destroy, background='lightgray')

m.minsize(400, 300)
m.maxsize(400, 300)
label.pack(anchor='n')
stabut.place(x=50,y=25)
actbut.place(x=50,y=70)
start_button.place(x=150,y=150)
progress.place(x=50, y=190)
button.pack(side='bottom', pady=10)
m.mainloop()