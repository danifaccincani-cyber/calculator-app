import tkinter as tk

# Button grid configuration
def createButtons():
    
    button = [
        
        "7","8","9","*",
        "4","5","6","-",
        "1","2","3","+",
        "+/-","0",".","="   
    ]
    
    # CE button
    numbers = tk.Button(window, text="CE", command=lambda: removeValue("CE"))
    numbers.grid(row=2, column=3, sticky="nsew")
    
    # numbers and operator buttons
    for i, val in enumerate(button):
        numbers = tk.Button(window, text=val, command=lambda v=val: click(v))
        numbers.grid(row=(i // 4) + 3, column=i % 4,sticky="nsew") 
    
    


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


# Row configuration for buttons
for i in range(2,7):
    window.rowconfigure(i, weight=2)


createButtons()    



if __name__ == "__main__":
    window.mainloop()       