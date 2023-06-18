from tkinter import *

FONT = 'bahnschirift 8'

def send():
    send = "You: " + input.get()
    txt.insert(END, "\n" + send)
    user = input.get()
    if (user == 'Zdarova'):
        txt.insert(END, "\n" + "Bot: Darova")
    input.delete(0, END)

display = Tk()
display.title("Bot")
display.resizable(0, 0)
display.geometry("300x500")
display['bg'] = 'gray'
input = Entry(display, bg="gray", fg="black", width=43)
input.place(x = 2, y = 460)
txt = Text(display, bg="white", fg="black", width=40, height=27)
txt.place(x = 0, y = 0)
send = Button(display, font = FONT, text="Send", command=send).place(x = 266, y = 456)

display.mainloop()
