import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        window_width = 800
        window_height = 600

        self.title("HL7 Generator")
        self.geometry(str(window_width)+"x"+str(window_height))
        self.resizable(True,True)
        #todo add icon here

        container = tk.Frame(self, bg="#2d2e30")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        message_window = tk.Text(container, bg="white", fg="black", height=window_height*.75, width=int(window_width*.75), font="Monospaced")
        message_window.pack()

        new_message_button = tk.Button(container, text="New HL7",command= None)
        new_message_button.pack()



if __name__ == "__main__":
    app = App()
    app.mainloop()
