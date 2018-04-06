#!/usr/bin/env python
from tkinter import *
import tooltip
import webhook

root = Tk()

root.wm_title("Discord Roflz Webhook Poster")


class ButtonCommands:

    def webhookPost():
#        url = "https://discordapp.com/api/webhooks/430687214549204993/KeRt_krZwouxhHNDrbkbg64HXgZdUM2XQlqL3Ny5SFusM-I-U79wbGaqqxy4UdF_kSB3"
        url = "https://discordapp.com/api/webhooks/431783097521143810/Gm58CDhYUXJBcAImv5lrzaPSS8l7fAlVgVUELWs_LiyrmKMHv3mgr4_Rs8IrKPLAG6d8"
        mbox_text = a.mbox.get(1.0, END)
        username_text = a.entry1.get()
        imgurl_text = a.entry2.get()
        if username_text == "":
            username_text = None
        if imgurl_text == "":
            imgurl_text = None
        wb = webhook.Webhook(url, mbox_text, username_text, imgurl_text)
        try:
            wb.post()
        except Exception as err:
            print(err)

    def deleteContent():
        a.entry1.delete(0, END)
        a.entry2.delete(0, END)
        a.mbox.delete(1.0, END)


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
        self.ttip_label1 = tooltip.ToolTip(self.label1, "This field may be left blank")

        self.username_text = StringVar()
        self.entry1 = Entry(frameTop, textvariable=self.username_text)
        self.entry1.pack(side=LEFT, padx=2)
        self.ttip_entry1 = tooltip.ToolTip(self.entry1, "This field may be left blank")

        self.label2 = Label(frameTop, text="Image Url:")
        self.label2.pack(side=LEFT)
        self.ttip_label2 = tooltip.ToolTip(self.label2, "This field may be left blank")

        self.imgurl_text = StringVar()
        self.entry2 = Entry(frameTop, textvariable=self.imgurl_text)
        self.entry2.pack(side=LEFT, padx=2)
        self.ttip_entry2 = tooltip.ToolTip(self.entry2, "This field may be left blank")

        self.mbox = Text(frameBot, maxundo=10, height=10, width=50, wrap=WORD)
        self.mbox.pack(side=LEFT)
        self.ttip_mbox = tooltip.ToolTip(self.mbox, "This field is required")

        self.label3 = Label(frameLabe, text="Message:")
        self.label3.pack(side=LEFT)
        self.ttip_label3 = tooltip.ToolTip(self.label3, "This field is required")


class Buttons:

    def __init__(self, master):
        frame = Frame(master)
        frame.grid(row=2, column=1, rowspan=2, padx=5, sticky=N, pady=10)

        self.postButton = Button(frame, text="Post", width=12, command=ButtonCommands.webhookPost)
        self.postButton.pack(side=TOP)

        self.clearButton = Button(frame, text="Clear All", width=12, command=ButtonCommands.deleteContent)
        self.clearButton.pack(side=TOP, pady=4)

        self.closeButton = Button(frame, text="Close", width=12, command=master.destroy)
        self.closeButton.pack(side=TOP)


a = EntryForm(root)
b = Buttons(root)

root.mainloop()
