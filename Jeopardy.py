from tkinter import *

root = Tk()
root.title("Jeopardy")
root.configure(background = 'navy blue')
root.geometry("1920x1250")

# Text for manipulation

# Categories
category_0_text = "Category 0"
category_1_text = "Category 1"
category_2_text = "Category 2"
category_3_text = "Category 3"
category_4_text = "Category 4"
category_5_text = "Category 5"

# Category 0 Questions
question_0_1_text = "question_0_1_text"
question_0_2_text = "question_0_2_text"
question_0_3_text = "question_0_3_text"
question_0_4_text = "question_0_4_text"
question_0_5_text = "question_0_5_text"

# Category 1 Questions
question_1_1_text = "question_1_1_text"
question_1_2_text = "question_1_2_text"
question_1_3_text = "question_1_3_text"
question_1_4_text = "question_1_4_text"
question_1_5_text = "question_1_5_text"

# Category 2 Questions
question_2_1_text = "question_2_1_text"
question_2_2_text = "question_2_2_text"
question_2_3_text = "question_2_3_text"
question_2_4_text = "question_2_4_text"
question_2_5_text = "question_2_5_text"

# Category 3 Questions
question_3_1_text = "question_3_1_text"
question_3_2_text = "question_3_2_text"
question_3_3_text = "question_3_3_text"
question_3_4_text = "question_3_4_text"
question_3_5_text = "question_3_5_text"

# Category 4 Questions
question_4_1_text = "question_4_1_text"
question_4_2_text = "question_4_2_text"
question_4_3_text = "question_4_3_text"
question_4_4_text = "question_4_4_text"
question_4_5_text = "question_4_5_text"

# Category 5 Questions
question_5_1_text = "question_5_1_text"
question_5_2_text = "question_5_2_text"
question_5_3_text = "question_5_3_text"
question_5_4_text = "question_5_4_text"
question_5_5_text = "question_5_5_text"

# Category 0 Answers
answer_0_1_text = "answer_0_1_text"
answer_0_2_text = "answer_0_2_text"
answer_0_3_text = "answer_0_3_text"
answer_0_4_text = "answer_0_4_text"
answer_0_5_text = "answer_0_5_text"

# Category 1 Answers
answer_1_1_text = "answer_1_1_text"
answer_1_2_text = "answer_1_2_text"
answer_1_3_text = "answer_1_3_text"
answer_1_4_text = "answer_1_4_text"
answer_1_5_text = "answer_1_5_text"

# Category 2 Answers
answer_2_1_text = "answer_2_1_text"
answer_2_2_text = "answer_2_2_text"
answer_2_3_text = "answer_2_3_text"
answer_2_4_text = "answer_2_4_text"
answer_2_5_text = "answer_2_5_text"

# Category 3 Answers
answer_3_1_text = "answer_3_1_text"
answer_3_2_text = "answer_3_2_text"
answer_3_3_text = "answer_3_3_text"
answer_3_4_text = "answer_3_4_text"
answer_3_5_text = "answer_3_5_text"

# Category 4 Answers
answer_4_1_text = "answer_4_1_text"
answer_4_2_text = "answer_4_2_text"
answer_4_3_text = "answer_4_3_text"
answer_4_4_text = "answer_4_4_text"
answer_4_5_text = "answer_4_5_text"

# Category 5 Answers
answer_5_1_text = "answer_5_1_text"
answer_5_2_text = "answer_5_2_text"
answer_5_3_text = "answer_5_3_text"
answer_5_4_text = "answer_5_4_text"
answer_5_5_text = "answer_5_5_text"

# Question label
global question_label
question_label = Label(root,bg = "navy blue",fg = "yellow", text = "",font=("Monokai", 50),justify = "center")
question_label.grid(column = 2,row = 6,columnspan = 2)

# Answer label
global answer_label
answer_label = Label(root,bg = "navy blue",fg = "yellow", text = "",font=("Monokai", 50),justify = "center")
answer_label.grid(column = 4,row = 7,columnspan = 2)

# Current selected question
global current_question
current_question = (0,0)

# Functions
def display_question(column,row):
	''' The display_question function is used to display the appropriate question for each button press'''
	global current_question
	if column == 0:
		if row == 1:
			question_label.config(text = category_0_text + " for $200 \n" + question_0_1_text)
			button_0_1.config(state = "disabled")
			current_question = (0,1)
		if row == 2:
			question_label.config(text = category_0_text + " for $400 \n" + question_0_2_text)
			button_0_2.config(state = "disabled")
			current_question = (0,2)
		if row == 3:
			question_label.config(text = category_0_text + " for $600 \n" + question_0_3_text)
			button_0_3.config(state = "disabled")
			current_question = (0,3)
		if row == 4:
			question_label.config(text = category_0_text + " for $800 \n" + question_0_4_text)
			button_0_4.config(state = "disabled")
			current_question = (0,4)
		if row == 5:
			question_label.config(text = category_0_text + " for $1000 \n" + question_0_5_text)
			button_0_5.config(state = "disabled")
			current_question = (0,5)

	if column == 1:
		if row == 1:
			question_label.config(text = category_1_text + " for $200 \n" + question_1_1_text)
			button_1_1.config(state = "disabled")
			current_question = (1,1)
		if row == 2:
			question_label.config(text = category_1_text + " for $400 \n" + question_1_2_text)
			button_1_2.config(state = "disabled")
			current_question = (1,2)
		if row == 3:
			question_label.config(text = category_1_text + " for $600 \n" + question_1_3_text)
			button_1_3.config(state = "disabled")
			current_question = (1,3)
		if row == 4:
			question_label.config(text = category_1_text + " for $800 \n" + question_1_4_text)
			button_1_4.config(state = "disabled")
			current_question = (1,4)
		if row == 5:
			question_label.config(text = category_1_text + " for $1000 \n" + question_1_5_text)
			button_1_5.config(state = "disabled")
			current_question = (1,5)

	if column == 2:
		if row == 1:
			question_label.config(text = category_2_text + " for $200 \n" + question_2_1_text)
			button_2_1.config(state = "disabled")
			current_question = (2,1)
		if row == 2:
			question_label.config(text = category_2_text + " for $400 \n" + question_2_2_text)
			button_2_2.config(state = "disabled")
			current_question = (2,2)
		if row == 3:
			question_label.config(text = category_2_text + " for $600 \n" + question_2_3_text)
			button_2_3.config(state = "disabled")
			current_question = (2,3)
		if row == 4:
			question_label.config(text = category_2_text + " for $800 \n" + question_2_4_text)
			button_2_4.config(state = "disabled")
			current_question = (2,4)
		if row == 5:
			question_label.config(text = category_2_text + " for $1000 \n" + question_2_5_text)
			button_2_5.config(state = "disabled")
			current_question = (2,5)

	if column == 3:
		if row == 1:
			question_label.config(text = category_3_text + " for $200 \n" + question_3_1_text)
			button_3_1.config(state = "disabled")
			current_question = (3,1)
		if row == 2:
			question_label.config(text = category_3_text + " for $400 \n" + question_3_2_text)
			button_3_2.config(state = "disabled")
			current_question = (3,2)
		if row == 3:
			question_label.config(text = category_3_text + " for $600 \n" + question_3_3_text)
			button_3_3.config(state = "disabled")
			current_question = (3,3)
		if row == 4:
			question_label.config(text = category_3_text + " for $800 \n" + question_3_4_text)
			button_3_4.config(state = "disabled")
			current_question = (3,4)
		if row == 5:
			question_label.config(text = category_3_text + " for $1000 \n" + question_3_5_text)
			button_3_5.config(state = "disabled")
			current_question = (3,5)

	if column == 4:
		if row == 1:
			question_label.config(text = category_4_text + " for $200 \n" + question_4_1_text)
			button_4_1.config(state = "disabled")
			current_question = (4,1)
		if row == 2:
			question_label.config(text = category_4_text + " for $400 \n" + question_4_2_text)
			button_4_2.config(state = "disabled")
			current_question = (4,2)
		if row == 3:
			question_label.config(text = category_4_text + " for $600 \n" + question_4_3_text)
			button_4_3.config(state = "disabled")
			current_question = (4,3)
		if row == 4:
			question_label.config(text = category_4_text + " for $800 \n" + question_4_4_text)
			button_4_4.config(state = "disabled")
			current_question = (4,4)
		if row == 5:
			question_label.config(text = category_4_text + " for $1000 \n" + question_4_5_text)
			button_4_5.config(state = "disabled")
			current_question = (4,5)

	if column == 5:
		if row == 1:
			question_label.config(text = category_5_text + " for $200 \n" + question_5_1_text)
			button_5_1.config(state = "disabled")
			current_question = (5,1)
		if row == 2:
			question_label.config(text = category_5_text + " for $400 \n" + question_5_2_text)
			button_5_2.config(state = "disabled")
			current_question = (5,2)
		if row == 3:
			question_label.config(text = category_5_text + " for $600 \n" + question_5_3_text)
			button_5_3.config(state = "disabled")
			current_question = (5,3)
		if row == 4:
			question_label.config(text = category_5_text + " for $800 \n" + question_5_4_text)
			button_5_4.config(state = "disabled")
			current_question = (5,4)
		if row == 5:
			question_label.config(text = category_5_text + " for $1000 \n" + question_5_5_text)
			button_5_5.config(state = "disabled")
			current_question = (5,5)

def display_answer():
	''' The display_answer function is used to display the appropriate question for the show answer button'''
	global current_question
	column = current_question[0]
	row = current_question[1]

	if column == 0:
		if row == 0:
			answer_label.config(text = "Answer:\nNo Question\nSelected!")
		if row == 1:
			answer_label.config(text = "Answer:\n" + answer_0_1_text)
		if row == 2:
			answer_label.config(text = "Answer:\n" + answer_0_2_text)
		if row == 3:
			answer_label.config(text = "Answer:\n" + answer_0_3_text)
		if row == 4:
			answer_label.config(text = "Answer:\n" + answer_0_4_text)
		if row == 5:
			answer_label.config(text = "Answer:\n" + answer_0_5_text)

	if column == 1:
		if row == 1:
			answer_label.config(text = "Answer:\n" + answer_1_1_text)
		if row == 2:
			answer_label.config(text = "Answer:\n" + answer_1_2_text)
		if row == 3:
			answer_label.config(text = "Answer:\n" + answer_1_3_text)
		if row == 4:
			answer_label.config(text = "Answer:\n" + answer_1_4_text)
		if row == 5:
			answer_label.config(text = "Answer:\n" + answer_1_5_text)

	if column == 2:
		if row == 1:
			answer_label.config(text = "Answer:\n" + answer_2_1_text)
		if row == 2:
			answer_label.config(text = "Answer:\n" + answer_2_2_text)
		if row == 3:
			answer_label.config(text = "Answer:\n" + answer_2_3_text)
		if row == 4:
			answer_label.config(text = "Answer:\n" + answer_2_4_text)
		if row == 5:
			answer_label.config(text = "Answer:\n" + answer_2_5_text)

	if column == 3:
		if row == 1:
			answer_label.config(text = "Answer:\n" + answer_3_1_text)
		if row == 2:
			answer_label.config(text = "Answer:\n" + answer_3_2_text)
		if row == 3:
			answer_label.config(text = "Answer:\n" + answer_3_3_text)
		if row == 4:
			answer_label.config(text = "Answer:\n" + answer_3_4_text)
		if row == 5:
			answer_label.config(text = "Answer:\n" + answer_3_5_text)

	if column == 4:
		if row == 1:
			answer_label.config(text = "Answer:\n" + answer_4_1_text)
		if row == 2:
			answer_label.config(text = "Answer:\n" + answer_4_2_text)
		if row == 3:
			answer_label.config(text = "Answer:\n" + answer_4_3_text)
		if row == 4:
			answer_label.config(text = "Answer:\n" + answer_4_4_text)
		if row == 5:
			answer_label.config(text = "Answer:\n" + answer_4_5_text)

	if column == 5:
		if row == 1:
			answer_label.config(text = "Answer:\n" + answer_5_1_text)
		if row == 2:
			answer_label.config(text = "Answer:\n" + answer_5_2_text)
		if row == 3:
			answer_label.config(text = "Answer:\n" + answer_5_3_text)
		if row == 4:
			answer_label.config(text = "Answer:\n" + answer_5_4_text)
		if row == 5:
			answer_label.config(text = "Answer:\n" + answer_5_5_text)

# Row 0
category_0_label = Label(root,bg = "navy blue",fg = "yellow", text = category_0_text,font=("Monokai", 26),width = 15,height = 2).grid(column = 0,row = 0)
category_1_label = Label(root,bg = "navy blue",fg = "yellow", text = category_1_text,font=("Monokai", 26),width = 16,height = 2).grid(column = 1,row = 0)
category_2_label = Label(root,bg = "navy blue",fg = "yellow", text = category_2_text,font=("Monokai", 26),width = 15,height = 2).grid(column = 2,row = 0)
category_3_label = Label(root,bg = "navy blue",fg = "yellow", text = category_3_text,font=("Monokai", 26),width = 16,height = 2).grid(column = 3,row = 0)
category_4_label = Label(root,bg = "navy blue",fg = "yellow", text = category_4_text,font=("Monokai", 26),width = 15,height = 2).grid(column = 4,row = 0)
category_5_label = Label(root,bg = "navy blue",fg = "yellow", text = category_5_text,font=("Monokai", 26),width = 16,height = 2).grid(column = 5,row = 0)

# Row 1
button_0_1 = Button(root, text = "$200",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(0,1))
button_0_1.grid(column = 0,row = 1)

button_1_1 = Button(root, text = "$200",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(1,1))
button_1_1.grid(column = 1,row = 1)

button_2_1 = Button(root, text = "$200",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(2,1))
button_2_1.grid(column = 2,row = 1)

button_3_1 = Button(root, text = "$200",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(3,1))
button_3_1.grid(column = 3,row = 1)

button_4_1 = Button(root, text = "$200",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(4,1))
button_4_1.grid(column = 4,row = 1)

button_5_1 = Button(root, text = "$200",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(5,1))
button_5_1.grid(column = 5,row = 1)

# Row 2
button_0_2 = Button(root, text = "$400",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(0,2))
button_0_2.grid(column = 0,row = 2)

button_1_2 = Button(root, text = "$400",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(1,2))
button_1_2.grid(column = 1,row = 2)

button_2_2 = Button(root, text = "$400",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(2,2))
button_2_2.grid(column = 2,row = 2)

button_3_2 = Button(root, text = "$400",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(3,2))
button_3_2.grid(column = 3,row = 2)

button_4_2 = Button(root, text = "$400",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(4,2))
button_4_2.grid(column = 4,row = 2)

button_5_2 = Button(root, text = "$400",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(5,2))
button_5_2.grid(column = 5,row = 2)

# Row 3
button_0_3 = Button(root, text = "$600",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(0,3))
button_0_3.grid(column = 0,row = 3)

button_1_3 = Button(root, text = "$600",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(1,3))
button_1_3.grid(column = 1,row = 3)

button_2_3 = Button(root, text = "$600",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(2,3))
button_2_3.grid(column = 2,row = 3)

button_3_3 = Button(root, text = "$600",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(3,3))
button_3_3.grid(column = 3,row = 3)

button_4_3 = Button(root, text = "$600",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(4,3))
button_4_3.grid(column = 4,row = 3)

button_5_3 = Button(root, text = "$600",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(5,3))
button_5_3.grid(column = 5,row = 3)

# Row 4
button_0_4 = Button(root, text = "$800",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(0,4))
button_0_4.grid(column = 0,row = 4)

button_1_4 = Button(root, text = "$800",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(1,4))
button_1_4.grid(column = 1,row = 4)

button_2_4 = Button(root, text = "$800",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(2,4))
button_2_4.grid(column = 2,row = 4)

button_3_4 = Button(root, text = "$800",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(3,4))
button_3_4.grid(column = 3,row = 4)

button_4_4 = Button(root, text = "$800",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(4,4))
button_4_4.grid(column = 4,row = 4)

button_5_4 = Button(root, text = "$800",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(5,4))
button_5_4.grid(column = 5,row = 4)


# Row 5
button_0_5 = Button(root, text = "$1000",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(0,5))
button_0_5.grid(column = 0,row = 5)

button_1_5 = Button(root, text = "$1000",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(1,5))
button_1_5.grid(column = 1,row = 5)

button_2_5 = Button(root, text = "$1000",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(2,5))
button_2_5.grid(column = 2,row = 5)

button_3_5 = Button(root, text = "$1000",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(3,5))
button_3_5.grid(column = 3,row = 5)

button_4_5 = Button(root, text = "$1000",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 15,height = 2,command = lambda: display_question(4,5))
button_4_5.grid(column = 4,row = 5)

button_5_5 = Button(root, text = "$1000",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_question(5,5))
button_5_5.grid(column = 5,row = 5)


# Answer Button
answer_button = Button(root, text = "Show Answer",font=("Monokai", 26),bg = "navy blue",fg = "yellow",width = 16,height = 2,command = lambda: display_answer()).grid(column = 4,row = 6,columnspan = 2)

# Run mainloop for TK
root.mainloop()