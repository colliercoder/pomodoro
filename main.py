from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
X="✔️"
check_count = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS,check_count
    REPS,check_count =0,0
    window.after_cancel(timer)
    title_label.config(text = "Timer",bg=YELLOW, fg=GREEN)
    canvas.config(bg=YELLOW)
    window.config(bg=YELLOW)
    checkmarks.config(bg=YELLOW,text="")
    canvas.itemconfig(timer_text, text="00:00")




# ---------------------------- TIMER MECHANISM ------------------------------- #



def start_timer():
    global REPS
    global X
    global check_count
    REPS+=1
    work = [1,3,5,7]
    short_break = [2,4,6]
    print(REPS)
    if REPS in work:
        title_label.config(bg=YELLOW,fg=GREEN,text="Work")
        canvas.config(bg=YELLOW)
        window.config(bg=YELLOW)
        checkmarks.config(bg=YELLOW)
        count_down(5)
        check_count += 1
    elif REPS in short_break:
        title_label.config(bg=RED, fg=GREEN,text="Break")
        canvas.config(bg=RED)
        window.config(bg=RED)
        checkmarks.config(text=check_count*X, bg=RED)
        count_down(2)
    elif REPS == 8:
        title_label.config(bg=RED, fg=GREEN,text="Break")
        canvas.config(bg=RED)
        window.config(bg=RED)
        checkmarks.config(text=check_count*X,bg=RED)
        count_down(10)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg = YELLOW)



#Title
title_label = Label(text="Timer",fg=GREEN,bg = YELLOW,font=(FONT_NAME,35,"bold"))
title_label.grid(row =1, column = 2)

#tomato and time
canvas = Canvas(width = 200 , height= 224,bg=YELLOW, highlightthickness=0 )
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(103,130,text="00:00",fill = "white",font=(FONT_NAME,35,"bold"))
canvas.grid(row = 2,column=2)

#start and stop

start = Button(text="Start", command=start_timer,highlightthickness=0)
start.grid(row=3,column=1)
reset = Button(text="Reset", command=reset,highlightthickness=0)
reset.grid(column=3, row=3)


checkmarks = Label(text=X*check_count, fg=GREEN, bg=YELLOW)
checkmarks.grid(row=4, column=2)








window.mainloop()

