#!/usr/bin/env python
from tkinter import *
import webhook

root = Tk()

root.wm_title("Discord Roflz Webhook Poster")

class ButtonCommands:

    def webhookPost():
        webhook = webhook.Webhook(https://discordapp.com/api/webhooks/430687214549204993/KeRt_krZwouxhHNDrbkbg64HXgZdUM2XQlqL3Ny5SFusM-I-U79wbGaqqxy4UdF_kSB3, a.mbox_text, a.username_text, a.imgurl_text)
        


class EntryForm:

    def __init__(self, master):
        frameTop = Frame(master)
        frameTop.grid(row=0, column=0, columnspan=3, padx=10)

        frameBot = Frame(master)
        frameBot.grid(row=2, column=0, sticky=W, padx=10, pady=5)

        frameLabe = Frame(master)
        frameLabe.grid(row=1, column=0, sticky=W, padx=10)

        self.label1 = Label(frameTop, text="User Name:")
        self.label1.pack(side=LEFT)

        self.username_text = StringVar()
        self.entry1 = Entry(frameTop, textvariable=self.username_text)
        self.entry1.pack(side=LEFT, padx=2)
        self.entry1.insert(END, "Roflz")

        self.label2 = Label(frameTop, text="Image Url:")
        self.label2.pack(side=LEFT)

        self.imgurl_text = StringVar()
        self.entry2 = Entry(frameTop, textvariable=self.imgurl_text)
        self.entry2.pack(side=LEFT, padx=2)

        self.mbox = Text(frameBot, maxundo=10, height=10, width=50, wrap=WORD)
        self.mbox.pack(side=LEFT)
        self.mbox_text = self.mbox.get(ANCHOR)

        self.label3 = Label(frameLabe, text="Message:")
        self.label3.pack(side=LEFT)


class Buttons:

    def __init__(self, master):
        frame = Frame(master)
        frame.grid(row=2, column=1, rowspan=2, padx=5, sticky=N, pady=10)

        self.postButton = Button(frame, text="Post", width=12)
        self.postButton.pack(side=TOP)

        self.clearButton = Button(frame, text="Clear All", width=12)
        self.clearButton.pack(side=TOP, pady=4)

        self.closeButton = Button(frame, text="Close", width=12)
        self.closeButton.pack(side=TOP)


a = EntryForm(root)
b = Buttons(root)

root.mainloop()
