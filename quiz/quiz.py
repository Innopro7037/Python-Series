import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

# Fuction to display the current question and choices
def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text='')
    next_btn.config(state="disabled")

def check_answer(i):
    question = quiz_data[current_question]
    selected_choice = choice_btns[i].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text='Correct!', foreground="green")
    else: 
        feedback_label.config(text="Incorrect!", foreground="red")

    for button in choice_btns:
        button.config(state='disabled')
        next_btn.config(state="normal")

def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        show_question()

    else: 
        messagebox.showinfo("Quiz Completed",
                            "Quiz Complted! Final Score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

root = tk.Tk()
root.title('Simple Quiz App')
root.geometry('600x500')
style = Style(theme='flatly')

style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the question label
qs_label = ttk.Label(
    root, anchor='center', wraplength=500, padding=10
)
qs_label.pack(pady=10)

# Create choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root, command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root, anchor='center', padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root, text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root, text='Next', command=next_question, state='disabled'
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

root.mainloop()
