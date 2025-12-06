
import tkinter as tk

# --- Theme Colors ---
FOREST_GREEN = "#2F4F2F"
WOOD_BROWN = "#8B4513"
HONEYDEW = "#F0FFF0"
LIGHT_GREEN = "#90EE90"

class ForestCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Forest Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg=FOREST_GREEN)
        self.root.resizable(False, False)

        self.expression = ""

        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            self.root, 
            textvariable=self.display_var, 
            font=('Arial', 28, 'bold'), 
            bg=HONEYDEW, 
            fg=FOREST_GREEN,
            bd=10, 
            justify='right',
            relief=tk.SUNKEN
        )
        self.display.pack(padx=10, pady=20, fill='x', expand=True)

        self.buttons_frame = tk.Frame(self.root, bg=FOREST_GREEN)
        self.buttons_frame.pack(fill='both', expand=True, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['%', '=']
        ]

        for i, row in enumerate(buttons):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
            for j, text in enumerate(row):
                self.buttons_frame.grid_columnconfigure(j, weight=1)
                command = lambda t=text: self.on_button_click(t)
                
                if text == '=':
                    btn = self.create_button(text, WOOD_BROWN, command)
                    btn.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky='nsew')
                elif text == '%':
                    btn = self.create_button(text, WOOD_BROWN, command)
                    btn.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')
                elif text in ['/', '*', '-', '+', 'C']:
                    btn = self.create_button(text, LIGHT_GREEN, command)
                    btn.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')
                else:
                    btn = self.create_button(text, WOOD_BROWN, command)
                    btn.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')

    def create_button(self, text, bg_color, command):
        """Creates a styled button with a command."""
        return tk.Button(
            self.buttons_frame, 
            text=text, 
            font=('Arial', 18, 'bold'), 
            bg=bg_color, 
            fg=HONEYDEW, 
            relief=tk.RAISED, 
            bd=3,
            command=command
        )

    def on_button_click(self, char):
        """Handles button clicks and updates the display."""
        if self.expression == "Error":
            self.expression = ""

        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif char == '%':
            try:
                self.expression = str(eval(self.expression) / 100)
            except:
                self.expression = "Error"
        else:
            self.expression += str(char)
        
        self.display_var.set(self.expression)

if __name__ == "__main__":
    main_window = tk.Tk()
    app = ForestCalculator(main_window)
    main_window.mainloop()
