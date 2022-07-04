from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from playsound import playsound
import os

class GUI(Tk):

    def __init__(self):
        super().__init__()

    def window(self):
        """This will manage window resources"""
        width = 733
        height = 455
        self.geometry(f"{width}x{height}")
        self.title("Untitled - Notepad(KOD)")
        self.wm_iconbitmap("icon.ico")
        self.config(background="#1c1c1c")

    def menu(self):
        """This will create a menu"""
        myMenu = Menu(self)

        self.FileMenu = Menu(myMenu, tearoff=0)
        EditMenu = Menu(myMenu, tearoff=0)
        FormatMenu = Menu(myMenu, tearoff=0)
        helpMenu = Menu(myMenu, tearoff=0)

        fileMenuOptions = {"New": self.newFile, "Open": self.openFile, "Save": self.save, "Save as": self.saveAs, "Blast": self.exit}
        for key, value in fileMenuOptions.items():
            if key == "Blast":
                self.FileMenu.add_separator()
            self.FileMenu.add_command(label=key, command=value)

        editMenuOptions = {"Cut": self.cut, "Copy": self.copy, "Paste": self.paste}
        for key, value in editMenuOptions.items():
            EditMenu.add_command(label=key, command=value)

        FormatMenu.add_command(label="Font", command=lambda: print("x"))
        helpMenu.add_command(label="About KOD pad", command=self.about)

        myMenu.add_cascade(label="File", menu=self.FileMenu)
        myMenu.add_cascade(label="Edit", menu=EditMenu)
        myMenu.add_cascade(label="Format", menu=FormatMenu)
        myMenu.add_cascade(label="Help", menu=helpMenu)

        self.FileMenu.entryconfig("Save", state=DISABLED)
        FormatMenu.entryconfig("Font", state=DISABLED)
        self.config(menu=myMenu)

    def writting_place(self):
        """This will create a writting place"""
        scrollBar = Scrollbar()
        scrollBar.pack(side=RIGHT, fill=Y)

        self.place = Text(self, yscrollcommand=scrollBar.set, bg="#1c1c1c", fg="White",
                     borderwidth=0, font=("Consolus", 11, "bold"), insertbackground="White")
        self.file = None
        self.place.pack(fill=BOTH, expand=True)
        scrollBar.configure(command=self.place.yview)

    # <----- FUNCTIONS FOR PERFORMING MENU TASKS ----->

    # FILE MENU FUNCTIONS
    def newFile(self):
        self.file = None
        self.place.delete(1.0, END)
        self.anableSave()
        self.title("Untitled - Notepad(KOD)")

    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.place.delete(1.0, END)
            with open(self.file, "r") as f:
                self.place.insert(1.0, f.read())
        self.anableSave()
        self.title(os.path.basename(self.file) + " - Notepad(KOD)")

    def save(self):
        with open(self.file, "w") as f:
            f.write(self.place.get(1.0, END))

    def saveAs(self):
        self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                    filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            with open(self.file, "w") as f:
                f.write(self.place.get(1.0, END))
        self.anableSave()
        self.title(os.path.basename(self.file) + " - Notepad(KOD)")

    def exit(self):
        try:
            playsound("blast.wav")
        except Exception as err:
            print(err)
        self.destroy()

    def anableSave(self):
        if self.file != None:
            self.FileMenu.entryconfig("Save", state=NORMAL)
        else:
            self.FileMenu.entryconfig("Save", state=DISABLED)

    # EDIT MENU FUNCTIONS
    def cut(self):
        self.place.event_generate(("<<Cut>>"))

    def copy(self):
        self.place.event_generate(("<<Copy>>"))

    def paste(self):
        self.place.event_generate(("<<Paste>>"))

    # HELP MENU FUNCTIONS
    def about(self):
        showinfo("About Notepad - KOD", "Notepad made by Taha Tariq(KOD)")

if __name__ == '__main__':
    windw = GUI()
    windw.window()
    windw.menu()
    windw.writting_place()
    windw.mainloop()