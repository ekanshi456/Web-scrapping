import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

def question_answer():
    # print("i work")
    question=e1.get()
    answer=wikipedia.summary(question)
    showinfo("answer", answer)
    e1["text"] = "You have to press enter"

    print(answer)

#create GUI
root = Tk()
root.geometry("400x300")
root.title('Q&A')

#create buttons
question = StringVar()

L1 = Label(text="Ques:", font=("Helvetica",18,"bold"))
L1.grid(pady=16)

e1 = Entry(root,width=50,textvariable=question, font=("Helvetica",10), bd=8)
e1.grid(pady=14 , padx=14)
e1.bind('<Return>', question_answer)

b1=Button(root,width=14,command=question_answer, text="Search", font=("Helvetica", 12, "bold"), bd=8)
b1.grid(pady=16)

root.mainloop()