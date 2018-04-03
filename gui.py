#!/usr/bin/env python
from tkinter import *
import webhook

root = Tk()

root.wm_title("Discord Roflz Webhook Poster")

class EntryForm:

    def __init__(self, master):
        frameTop = Frame(master)
        frameTop.grid(row=0, column=0, columnspan=2)

        frameBot = Frame(master)
        frameBot.grid(row=1, column=0, columnspan=2)

        self.label1 = Label(frameTop, text="User Name")
        self.label1.pack(side=LEFT)

        self.username_text = StringVar()
        self.entry1 = Entry(frameTop, textvariable=self.username_text)
        self.entry1.pack(side=LEFT)

        self.label2 = Label(frameTop, text="Image Url")
        self.label2.pack(side=LEFT)

        self.imgurl_text = StringVar()
        self.entry2 = Entry(frameTop, textvariable=self.imgurl_text)
        self.entry2.pack(side=LEFT)

        self.mbox = Text(frameBot, maxundo=10, height=36, width=100, wrap=WORD)
        self.mbox_text = self.mbox.get(END)



a = EntryForm(root)

root.mainloop()
