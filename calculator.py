import tkinter as tk

# Button grid configuration
def createButtons():
    
    button = [
        
        "7","8","9","/",
        "4","5","6","*",
        "1","2","3","-",
        "0",".","+","="  
    ]
    
    # CE button
    numbers = tk.Button(window, text="CE", font=("Helvetica", 18), command=lambda: removeValue("CE"), bg="#ff3b30", fg="white")
    numbers.grid(row=2, column=3, sticky="nsew")
    
    # numbers and operator buttons
    for i, val in enumerate(button):
        
        if val in ("+", "-", "*", "/", "="):
            numbers = tk.Button(window, text=val, font=("Helvetica", 18), command=lambda v=val: click(v), bg="#ff9500", fg="white")
        else:
            numbers = tk.Button(window, text=val, font=("Helvetica", 18), command=lambda v=val: click(v), bg="#333333", fg="white")
            
        numbers.grid(row=(i // 4) + 3, column=i % 4, sticky="nsew")
        
def click(value):
    
    global firstNumber, operator, expression,newNumber
    
    match value:
        
        #operator buttons
        case '+' | '-' | '*' | '/':
            
            if operator != "":
                
                secondNumber = display.get()
                expression+=secondNumber + value
                firstNumber = str(eval(firstNumber + operator + secondNumber))
                display.set(firstNumber)
            
            else:
                expression+=display.get() + value
                firstNumber = display.get()
                
            operator = value
            output_history.set(expression)
            newNumber = True
            
            
        case '=':
            
            try:
                if firstNumber == "":
                    display.set("Insert a value")
                    return
                
                secondNumber = display.get()
                expression+=secondNumber + "="
                output_history.set(expression)
                result = round(eval(firstNumber + operator + secondNumber),10)
                display.set(result)
                firstNumber = ""
                operator = ""
                expression = ""
                newNumber = True
                
            except ZeroDivisionError:
                display.set("Error")
                firstNumber = ""
                operator = ""
                expression = ""
                newNumber = True
                output_history.set("")
        
                
        # Number and decimal buttons
        case _:
            current_display = display.get()
    
            if current_display in ("Insert a value", "Error") or newNumber:
                display.set(value)
                newNumber = False
        
            elif operator == "":
                if current_display == "0":
                    display.set(value)
                else:
                    display.set(current_display + value)
            
            else:
                display.set(current_display + value)
        
                 
    
def removeValue(value):
    global expression,firstNumber,operator,newNumber
    
    if value == "CE":
        display.set(0)
        expression = ""
        firstNumber = ""
        operator = ""
        newNumber = False
        output_history.set("")
        
            



# Main window configuration
window = tk.Tk()

window.geometry("600x600")
window.title("calculator App")
window.resizable(False,False)
window.configure(bg="#1a1a1a")


# Global variables
firstNumber = ""
operator = ""
expression = ""
newNumber = False


# StringVar for display and history
display = tk.StringVar(value=0)
output_history = tk.StringVar(value="")


# history label - shows the expression
history_label = tk.Label(window, font=("Helvetica",12), anchor="e", bg="#1a1a1a", fg="white", textvariable=output_history)
history_label.grid(row=0, column=0, columnspan=4, sticky="nsew")


# main display label - shows current number
label = tk.Label(window, font=("Helvetica",24), anchor="e", bg="#1a1a1a", fg="white", bd=5, relief="sunken", textvariable=display)
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