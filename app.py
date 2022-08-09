from logging import root
import tkinter as tk
from turtle import update
import adt_generate

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

        def newMSG():
            message_window.delete(1.0, tk.END)
            hl7_message = ""
            hl7_message = adt_generate.newADT()
            message_window.insert(tk.INSERT, hl7_message)

        message_window = tk.Text(container, bg="white", fg="black")
        message_window.pack(pady=25, padx=15, fill="x")
        message_window.pack(side="top")

        new_message_button = tk.Button(container, text="New HL7",command=newMSG)
        new_message_button.pack(side="bottom", pady="25")



if __name__ == "__main__":
    app = App()
    app.mainloop()
