import tkinter as tk
from PIL import ImageTk as itk
import math
from playsound import playsound as ps

#constants

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SHORT_BREAK_MIN = 5 * 60
WORK_MIN = 25 * 60
LONG_BREAK_MIN = 20 * 60
timer = None

# Sounds

def sound():
    ps("./python/pomodoro/pikachu_.mp3")

# Timer Reset

def stop():
    windows.after_cancel(timer)
    l1.config(text="Timer", fg=GREEN)
    canvas.itemconfig(count, text="00:00")
    checkmark.config(text="")
    global i
    i=0

# Timer Mechanism

i = 0
def starttime():
    global i
    i += 1
    if i%8 == 0:
        countdownsec(LONG_BREAK_MIN)
        l1.config(text="Long Break", fg=GREEN)
    elif i%2 == 1:
        countdownsec(WORK_MIN)
        l1.config(text="Work", fg=RED)
    elif i%2 == 0:
        countdownsec(SHORT_BREAK_MIN)
        l1.config(text="Short Break", fg=PINK)

# Countdown Mechanism

def countdownsec(n):
    global timer
    countmin = math.floor(n/60)
    countsec = math.floor(n%60)
    if countsec<10:
        countsec = f"0{countsec}"
    canvas.itemconfig(count, text=f"{countmin}:{countsec}")
    if n>0:
        timer = windows.after(1000, countdownsec, n-1)
    else:
        sound()
        starttime()
        mark = ""
        for _ in range(math.floor(i/2)):
            mark += "✔"
        checkmark.config(text=mark)

# UI Setup

windows = tk.Tk()
windows.title("Pomodoro")
windows.config(padx=50, pady=50, bg=YELLOW)

l1 = tk.Label(text="Timer",bg=YELLOW, font=(FONT_NAME, 25, "bold"), fg=GREEN)
l1.grid(column=2, row=1)

canvas = tk.Canvas(windows, width=220, height=223, bg=YELLOW, highlightthickness=0)
canvas.grid(column=2, row=2)

bg = itk.PhotoImage(file="./python/pomodoro/tomato.png")
canvas.create_image(110, 111.5, image = bg)

count = canvas.create_text(110, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))


startbtn = tk.Button(text="Start", command=starttime, bd=0, highlightthickness=0, bg="white", activebackground=RED,)
startbtn.grid(column=1, row=3)

resetbtn = tk.Button(text="Reset", command=stop, bd=0, highlightthickness=0, bg="white", activebackground=RED)
resetbtn.grid(column=3, row=3)

checkmark = tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
checkmark.grid(column=2, row=4)

windows.mainloop()
