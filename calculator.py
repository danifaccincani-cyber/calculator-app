import tkinter as tk


# Main window configuration
window = tk.Tk()

window.geometry("600x600")
window.title("calculator App")
window.resizable(False,False)


# Global variables
firstNumber = ""
operator = ""
expression = ""


# StringVar for display and history
display = tk.StringVar(value=0)
output_history = tk.StringVar(value="")


# history label - shows the expression
history_label = tk.Label(window, textvariable=output_history)
history_label.grid(row=0, column=0, columnspan=4, sticky="nsew")


# main display label - shows current number
label = tk.Label(window, textvariable=display)
label.grid(row=1, column=0, columnspan=4, sticky="nsew")


# grid configuration
for i in range(4):
    window.columnconfigure(i, weight=1)

    
window.rowconfigure(0, weight=1)
window.rowconfigure(1,weight=2)



if __name__ == "__main__":
    window.mainloop()       