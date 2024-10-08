import tkinter as tk

SMALL_FONT_STYLE=("Arial", 16)
LARGE_FONT_STYLE=("Arial", 40, "bold")
DIGITS_FONT_STYLE=("Arial", 24, "bold")
DEFAULT_FONT_STYLE=("Arial", 20)

WHITE="#ffffff"
OFF_WHITE="#f8faff"
LIGHT_GRAY="#f5f5f5"
LIGHT_BLUE="#ccedff"
LABEL_COLOR="#25265E"

class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667") 
        self.window.resizable(0, 0)
        self.window.title("GUI Calculator")

        self.total_expression = "0"
        self.current_expression = "0"

        self.display_frame=self.create_display_frame()
        self.buttons_frame=self.create_buttons_frame()
        self.total_label, self.label=self.create_display_labels()

        self.digits={
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        } # The keys are the coordinates on where each keys should be
        self.operations={"/":"\u00f7", "*":"\u00d7", "-":"-", "+":"+"}
        
        # make the buttons grow into the empty space
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digits_button()
        self.create_operators_button()
        self.create_special_buttons()
        


    def create_display_labels(self):
        total_label=tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE) # here, E in anchor means East
        total_label.pack(expand=True, fill="both")
        
        label=tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE) # here, E in anchor means East
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame=tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_digits_button(self):
        for digit, grid_value in self.digits.items():
            button=tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
            # using grids here because its easier to position in these cases

    def create_operators_button(self):
        i=0
        for operator, symbol in self.operations.items():
            button=tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i=i+1
    
    def create_clear_button(self):
        button=tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equals_button(self):
        button=tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
    
    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True, fill="both") #both meaning it should expand both horizontally and vertically
        return frame

    def run(self):
        self.window.mainloop()


if __name__=="__main__":
    calc=Calculator()
    calc.run()