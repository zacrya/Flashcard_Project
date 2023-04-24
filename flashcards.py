import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# constants
LARGE_FONT = ("Verdana", 12)


class Flashcard_App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, default="flashcards.ico")
        tk.Tk.wm_title(self, "Flashcards")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        # configure the root window
        # self.title("Flashcards")
        # self.geometry("750x500+10+10")
        # self.resizable(False, False)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start Page", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne)
        )
        button1.pack()

        button2 = ttk.Button(
            self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()

    # def button_clicked(self):
    # howinfo(title="Information", message="Hello, Tkinter!")


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page One", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        button2 = ttk.Button(
            self, text="Page Two", command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page Two", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        button2 = ttk.Button(
            self, text="Page One", command=lambda: controller.show_frame(PageOne)
        )
        button2.pack()


app = Flashcard_App()
app.mainloop()
