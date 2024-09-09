import tkinter as tk

LIGHT_GRAY="#f5f5f5"

class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667") 
        self.window.resizable(0, 0)
        self.window.title("GUI Calculator")
    
        self.display_frame=self.create_display_frame()
        self.buttons_frame=self.create_buttons_frame()
        
    def run(self):
        self.window.mainloop()

    def create_display_frame(self):
        frame=tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

if __name__=="__main__":

    calc=Calculator()
    calc.run()