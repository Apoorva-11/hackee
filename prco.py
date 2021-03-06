from tkinter import *
from tkinter import filedialog

import PyPDF2
import pyttsx3
from PIL import Image, ImageTk

import speech_recognition as sr
import pyaudio

root = Tk()

root.title("Book Byte")
root.minsize(width=400, height=400)
root.geometry("450x321+500+100")
bg = Image.open("book.png")
r = ImageTk.PhotoImage(bg)
img = Label(root, image=r)
img.place(x=0, y=25)

hf1 = Frame(root, bg="#FFBB00", bd=5)
hf1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
hl = Label(hf1, text=" Welcome to \nBook Byte", bg='black', fg='white', font=('Courier', 15))
hl.place(relx=0, rely=0, relwidth=1, relheight=1)


def text_to_speech():
    book = filedialog.askopenfilename(title="Select a PDF")
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    for num in range(0, pages):
        page = pdfreader.getPage(num)
        txt = page.extractText()
        ra = pyttsx3.init()
        ra.say(txt)
        ra.runAndWait()
    pass


b1 = Button(root, text="Listen to PDF", bg='black', fg='white', command=text_to_speech)
b1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)


def speech_to_text():
    rs = sr.Recognizer()
    with sr.Microphone() as source:
        rs.adjust_for_ambient_noise(source)
        print("Please speak")
        audio = rs.listen(source)
        try:
            print("you have written : \n "+ rs.recognize_google(audio))
        except Exception as e:
            print("Error : " +str(e))
    pass


b2 = Button(root, text="Speak Notes", bg='black', fg='white', command=speech_to_text)
b2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

root.mainloop()
