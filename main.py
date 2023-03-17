from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = .2
LONG_BREAK_MIN = .5
reps = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #



def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    ##If on 8th rep, call long break, if on even rep, call short break, else, then call work_sec
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK", bg=YELLOW, fg=RED, font=(FONT_NAME, 40, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK", bg=YELLOW, fg=PINK, font=(FONT_NAME, 40, "bold"))
    else:
        count_down(work_sec)
        timer_label.config(text="GET YOUR ASS TO WORK", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks = ""
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                marks += "✓"
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=105, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#Timer Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40,))
timer_label.config(text="Timer")
timer_label.grid(column=1, row= 0)

#Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

#Reset Button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

#Check Marks
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_marks.grid(column=1, row=3)


window.mainloop()
