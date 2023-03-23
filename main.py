import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    __root = Tk()
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    # To Add Scroll Bar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs) -> None:
        # Set Icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set Window Size(The Default Size is 300x300)
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set The Window Text
        self.__root.title("Untitled - Notepad")

        # Center the Window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For Left-Align
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For Right-Align
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # For Top & Bottom
        self.__root.geometry('%dx%d+%d+%d' %
                             (self.__thisWidth, self.__thisHeight, left, top))

        # To Make The Textarea Auto Resizeable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add Controls (Widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)

        # To Open New File
        self.__thisFileMenu.add_command(label="New", command=self.__newFile)

        # To Open A Already Existing File
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)

        # To Save Current File
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)

        # To Create A Line In The Dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(
            label="Exit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        # To Give A Feature Of Cut
        self.__thisEditMenu.add_command(label='Cut', command=self.__cut)

        # To Give A Feature Of Copy
        self.__thisEditMenu.add_command(label='Copy', command=self.__copy)

        # To Give A Feature Of Paste
        self.__thisEditMenu.add_command(label='Paste', command=self.__paste)

        # To Give A Feature Of Editing
        self.__thisMenuBar.add_cascade(label='Edit', menu=self.__thisEditMenu)

        # To Create A Feature Of Description Of The Notepad
        self.__thisHelpMenu.add_command(
            label='About Notepad', command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)
        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar Will Adjust Automatically According To The Content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        showinfo("Notepad", "Deep Patel")

    def __openFile(self):
        self.__file = askopenfilename(defaultextension='.txt', filetypes=[
                                      ('All Files', '*.*'), ("Text Documents", '*.txt')])

        if self.__file == "":
            # No File To Open
            self.__file = None
        else:
            # Try To Open File
            # Set the Window Title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1, 0, END)
            file = open(self.__file, "r")
            self.__thisTextArea.insert(1.0, file.read())
            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):
        if self.__file == None:
            # Save as New File
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[
                                            ('all files', '*.*'), ("Text Documents", "*.txt")])
            if self.__file == "":
                self.__file = None
            else:
                # Try To Open A File
                file = open(self.__file, 'w')
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
        else:
            file = open(self.__file, 'w')
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):
        # Run Main Application
        self.__root.mainloop()


# Run Main Application
notepad = Notepad(width=680, height=400)
notepad.run()
