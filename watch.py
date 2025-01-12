from customtkinter import CTk, CTkLabel
import time

class DigitalClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Digital Clock")
        self.master.geometry("300x100")
        self.master.resizable(False, False)
        self.master.eval('tk::PlaceWindow . center')

        self.time_label = CTkLabel(self.master, text="", font=("Arial", 48))
        self.time_label.pack(pady=20)

        self.update_time()
        self.master.after(1000, self.update_time)

    def update_time(self):  
        current_time = time.strftime("%H:%M:%S")
        self.time_label.configure(text=current_time)
        self.master.after(1000, self.update_time)

if __name__ == "__main__":
    app = CTk()
    DigitalClock(app)
    app.mainloop()